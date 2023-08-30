# Guide for project on LocalHost:
- Clone and download this repository
- Install requirements.txt file using (pip install -r requirements.txt)
- Run command in terminal (python3 ibm_app.py)
- Follow the Link given in terminal on port (5000)

The proposed solution of using the one-vs-all technique with Logistic Regression, Linear SVC, and similar algorithms to create an autonomous tagging system for Stack Overflow questions offers several novel and unique aspects:
## Dataset Link: 
#### [StackOverflow Labels Dataset](https://www.kaggle.com/datasets/stackoverflow/stacksample)
## APPROACH
- Automated Tagging Approach:
   While manual tagging has been the norm for categorizing content on platforms like Stack Overflow, your solution introduces automation to the tagging process. This represents a significant shift in how tags are assigned, making the process faster, more efficient, and less error.

- Machine Learning for Tagging:
   Leveraging machine learning algorithms like Logistic Regression and Linear SVC to predict tags based on question text and contextual information is a novel approach. It takes advantage of the algorithms' ability to learn patterns and relationships from large datasets, leading to accurate tag assignments.

-  One-vs-All Strategy:
   Treating each tag as a separate binary classification task (one-vs-all strategy) is an innovative approach to handling the multiclass tagging problem. This technique allows the system to focus on learning the specific characteristics of each tag, leading to more accurate predictions.

-  Scalability and Real-time Tagging:
   The automated tagging system is designed to scale seamlessly as the platform grows. The ability to tag new questions in real time as they are posted is a unique feature that ensures questions are categorized accurately and promptly.


- Combination of Algorithms:
   The combination of Logistic Regression and Linear SVC provides a versatile approach to solving the tagging challenge. Each algorithm has its strengths, and utilizing both can enhance the overall tagging accuracy.

- Adaptation to Platform Evolution
 As the platform's content and user behaviors evolve, the machine learning models can be retrained to adapt to changing patterns and trends. This   adaptability ensures that the tagging system remains effective over time.

- Accuracy and Relevance:
 If a machine learning model is properly trained and tuned, it can learn complex patterns of question text and contextual information. This allows the system to accurately predict relevant tags, improving tag assignment compared to purely manual tagging, which can introduce human error and subjectivity. 

- Real-time Tagging: 
 New questions are automatically tagged as soon as they are posted, ready for real-time categorization. This rapid tagging ensures that questions are available to users with the right expertise as soon as they are published. 



## Technology
-  We have chosen an efficient and well-rounded technology stack for our autonomous tagging system:

1. *Flask:* Lightweight Python web framework for building APIs.
2. *Scikit-learn:* Machine learning library for training and testing models.
3. *Pandas and NumPy:* Libraries for preprocessing and handling data.

## Scope of problem
 
 > Choose appropriate machine learning algorithms from Scikit-learn such as Logistic Regression and Linear SVC to binary classify the  tags. Use a one-for-all strategy to create separate templates for each tag. To evaluate the performance of the model, divide the data set into training and test sets. Model evaluation and tuning
 
>Evaluate models using metrics such as precision, recall, F1 score, and precision. Adjust hyperparameters to optimize model performance using methods such as grid search or random search. API development with Flask
 
 >Design and build API endpoints using Flask to serve models trained  for tag prediction.  Implement input validation and error handling mechanisms to ensure robust API functionality.  Integration with Stack Overflow
 
 > Develop mechanisms to extract query text and contextual information from Stack Overflow. Enable API calls to send queries to the autonomous tagging system and receive predicted tags.  Real-time prediction and detection 
 
 > Configure the system to predict and assign tags in real time when new questions are posted to Stack Overflow.  Feedback and continuous improvement
 
 > Incorporate user interaction and feedback to continually improve  tagging accuracy over time. Refine templates regularly to adapt to evolving community trends and patterns. Documentation and Implementation: 

