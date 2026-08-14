Got it — you want a short, clean GitHub README, not a detailed documentation-style one.

📱 Spam SMS Detection

A simple NLP and Machine Learning project that detects whether an SMS message is Spam or Ham.

🔧 Tech Stack
Python
NLTK
Scikit-learn
Bag of Words
Logistic Regression
Streamlit
🧠 Approach

The SMS text is cleaned and converted into numerical features using Bag of Words (CountVectorizer). A Logistic Regression model is then used to classify the message as Spam or Ham.

📊 Performance

Accuracy: 98.3%

🚀 Run Locally
pip install -r requirements.txt
streamlit run app.py
💡 Example

Input:
Congratulations! You have won a free prize!

Prediction: 🚨 Spam

Input:
Hey, are you coming today?

Prediction: ✅ Ham
