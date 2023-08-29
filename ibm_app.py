import json
from flask import Flask, request, render_template, session
from Preprocess import preprocess_text
from scipy.sparse import hstack
import numpy as np
import pickle
import requests

app = Flask(__name__)
app.secret_key = "ParaMountIBM"

# Note: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "rsDrcthxqZ-DlojxpWZbQA8BPIw18Hm9k_ZgHQHXBjsC"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
multilabel_binarizer = pickle.load(open("./MultiLabelFinal.pkl", 'rb'))

@app.route('/',methods =["GET","POST"])
def tag():
    if request.method =='POST':
        session.clear()
        title=request.form.get('title') 
        body=request.form.get('body')
        t1 = title
        t2 = body
        title = preprocess_text(title)

        body = preprocess_text(body)

        # print("=====================================", title)
        # print("=====================================", body)

        '''Loading TfIDF Vectorizer'''

        vectorizer = pickle.load(open("./tfidfVectorFinal.pkl", 'rb'))
        X1_pred = vectorizer.transform([title])
        X2_pred = vectorizer.transform([body])

        X_pred = hstack([X1_pred, X2_pred])
        # print("================================ Xpred is done-===============")

# Note: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"field": [], "values": X_pred.toarray().tolist()}]}

        response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/3a3ca4d0-6ef4-45af-b42e-f2311064d4bb/predictions?version=2021-05-01', json=payload_scoring,headers={'Authorization': 'Bearer ' + mltoken})   
        prediction = response_scoring.json()
        print("Scoring response")
        print(prediction)
        predicted_array = [prediction['predictions'][0]['values'][0][0]]
        # print("************************************",predicted_array)  
        predicted_array = np.array(predicted_array)
        print("=====================================", predicted_array)
        predicted_labels = multilabel_binarizer.inverse_transform(predicted_array)
        session['predicted_labels'] = {"title":t1, "body":t2,"predicted":predicted_labels[0]}#predicted_labels[0]
        return {"title":title, "body":body,"predicted":predicted_labels[0]} 
    return render_template('ask.html')
    
@app.route('/output') # type: ignore
def output():
    predicted_lab = session.get('predicted_labels')
    # print(Total)
    # session.clear()
    return render_template('output.html',pred_lab = [predicted_lab])

if __name__ == '__main__':
    app.run(debug=True, port=5000)