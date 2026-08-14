Spam SMS Detection

A machine learning project that classifies SMS messages as Spam or Ham (Not Spam) using Natural Language Processing (NLP) and basic machine learning techniques.

Features
Text preprocessing and cleaning
Bag of Words using CountVectorizer
Logistic Regression for classification
Real-time SMS prediction
Streamlit web interface
Saved model and vectorizer using Joblib
Technologies Used
Python
Pandas
Scikit-learn
NLTK
Joblib
Streamlit
Machine Learning Workflow
SMS Message
    ↓
Text Cleaning
    ↓
Train/Test Split
    ↓
Bag of Words
    ↓
Logistic Regression
    ↓
Prediction
    ↓
Spam / Ham
Model Performance

The model achieved approximately:

Accuracy: 98.30%
Spam Precision: 97%
Spam Recall: 91%
Spam F1-Score: 94%
Project Structure
Spam-SMS-Detection/
│
├── app.py
├── spam_model.pkl
├── bow_vectorizer.pkl
├── requirements.txt
└── README.md
Installation

Clone the repository and install the required libraries:

pip install -r requirements.txt
Run the Application

Start the Streamlit application:

streamlit run app.py

The application allows the user to enter an SMS message and predicts whether it is Spam or Ham.

Example

Input:

Congratulations! You have won a free prize. Click now!

Output:

🚨 SPAM SMS

Input:

Hey, are you coming to the meeting today?

Output:

✅ HAM — Not Spam
Future Improvements
Compare Naive Bayes, Logistic Regression, and SVM
Improve spam recall
Experiment with TF-IDF
Add confusion matrix and performance visualization
Deploy the application online
Add a probability/confidence score
Author

Developed as a basic NLP and Machine Learning project for learning and practical application of text classification.
