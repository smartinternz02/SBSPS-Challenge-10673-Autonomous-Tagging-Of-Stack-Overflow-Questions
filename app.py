from flask import Flask, jsonify, request, render_template,session
from Preprocess import preprocess_text
from scipy.sparse import hstack


import pickle

app = Flask(__name__)
app.secret_key = "ParaMountIBM"
tags_features = pickle.load(open("./tags_featureFinal.pkl", 'rb'))
Total = []
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

        '''Loading TfIDF Vectorizer'''

        vectorizer = pickle.load(open("./tfidfVectorFinal.pkl", 'rb'))
        X1_pred = vectorizer.transform([title])
        X2_pred = vectorizer.transform([body])

        X_pred = hstack([X1_pred, X2_pred])


        with open('./clfFinal.pkl', 'rb') as model_file:
            loaded_model = pickle.load(model_file)
        

        '''Prediction'''

        prediction = loaded_model.predict(X_pred)
        # print("**********************",prediction)
        print(len(prediction))

        # Load the MultiLabelBinarizer
        multilabel_binarizer = pickle.load(open("./MultiLabelFinal.pkl", 'rb'))

        # Inverse transform the prediction to get predicted labels
        predicted_labels = multilabel_binarizer.inverse_transform(prediction)
        session['predicted_labels'] = {"title":t1, "body":t2,"predicted":predicted_labels[0]}#predicted_labels[0]
        Total.append({"title":t1, "body":t2,"predicted":predicted_labels[0]})
        print("**********************",Total)
        return {"title":title, "body":body,"predicted":predicted_labels[0]} 
    return render_template('ask.html')
    
@app.route('/output') # type: ignore
def output():
    predicted_lab = session.get('predicted_labels')
    # print(Total)
    return render_template('output.html',pred_lab = [predicted_lab])

if __name__ == '__main__':
    app.run(debug=True, port=5000)