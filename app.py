# Import dependencies
from flask import Flask, render_template, request, jsonify
import nltk
import pickle
import numpy as np
from scipy.sparse import csr_matrix
from nltk.corpus import stopwords
import re
from nltk.stem.porter import PorterStemmer

# Initialize Flask app
app = Flask(__name__)

# Initialize PorterStemmer for text preprocessing
ps = PorterStemmer()

# Load pre-trained logistic regression model and TfidfVectorizer
model = pickle.load(open('Pickles/logisticreg_model.pkl', 'rb'))
check = pickle.load(open('Pickles/tfidfvect2.pkl', 'rb'))

# Define home route to display form
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Define function to preprocess text and make prediction
def predict(text):
    # Check if text is empty
    if text.strip() == "":
        return "EMPTY"
    # Preprocess text using regex, NLTK stopwords, and PorterStemmer
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    # Transform preprocessed text into feature matrix using TfidfVectorizer
    review_vect = check.transform([review]).toarray()
    # Make prediction using logistic regression model
    proba = model.predict_proba(review_vect)
    prediction = 'FAKE' if proba[0][0] < 0.5 else 'REAL'
    proba_percent = round(proba[0][0]*100, 2)
    # Return prediction and probability as a tuple
    return (prediction, proba_percent)

# Define webapp route to handle form submission
@app.route('/', methods=['POST'])
def webapp():
    # Get text input from form
    text = request.form['text']
    # Make prediction using text input
    prediction, proba = predict(text)
    # Render template with text input, prediction result, and probability
    return render_template('index.html', text=text, result=prediction, proba=proba)

# Define predict route to return prediction as JSON object
@app.route('/predict/', methods=['GET','POST'])
def api():
    # Get text input from query parameter
    text = request.args.get("text")
    # Preprocess text and transform into feature matrix using TfidfVectorizer
    review_vect = check.transform([text]).toarray()
    # Make prediction and calculate probability
    prediction = model.predict(review_vect)[0]
    probability = round(model.predict_proba(review_vect).max() * 100, 2)
    # Return prediction and probability as JSON object
    return jsonify({'prediction': prediction, 'probability': probability})

# Run Flask app if running script directly
if __name__ == "__main__":
    app.run()

# This code defines a Flask web application with three routes:

# The home route (/) displays an HTML form for user input.

# The webapp() function is called when the user submits the form. This function calls the predict() function to make a prediction based on the user's input, and then renders the index.html template with the user's input and the prediction result.

# The api() function is called when the user accesses the /predict/ endpoint with a query parameter for the input text. This function also calls the predict() function to make a prediction, but returns the result as a JSON object instead of rendering an HTML template.

# The predict() function preprocesses the input text using regex, NLTK stopwords, and a PorterStemmer. It then transforms the preprocessed text into a feature matrix using a pre-trained TfidfVectorizer, and makes a prediction using a pre-trained logistic regression model. The function returns the prediction result as a string.

# The web application loads the pre-trained logistic regression model and TfidfVectorizer from pickle files when the app is initialized, and uses a Flask server to run the application.