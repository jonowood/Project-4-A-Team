from flask import Flask, render_template, request, jsonify
import nltk
import pickle
import numpy as np
from scipy.sparse import csr_matrix
from nltk.corpus import stopwords
import re
from nltk.stem.porter import PorterStemmer

app = Flask(__name__)
ps = PorterStemmer()

model = pickle.load(open('Pickles/logisticreg_model.pkl', 'rb'))
check = pickle.load(open('Pickles/tfidfvect2.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

def predict(text):
    if text.strip() == "":
        return "EMPTY"
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    review_vect = check.transform([review]).toarray()
    prediction = 'FAKE' if model.predict(review_vect) == 0 else 'REAL'
    return prediction

@app.route('/', methods=['POST'])
def webapp():
    text = request.form['text']
    prediction = predict(text)
    return render_template('index.html', text=text, result=prediction)


@app.route('/predict/', methods=['GET','POST'])
def api():
    text = request.args.get("text")
    prediction = predict(text)
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run()
