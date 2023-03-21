<p align="center">
<img src="Static/Images/fake-new-facts.jpeg" alt="" title="" width="600" height="600">
</p>

# Fake News Identification using Machine Learning
This is our group's project for Project 4, where we were tasked to solve, analyze, or visualize a problem using machine learning (ML) with the other technologies we've learned. We chose to tackle the problem of identifying fake news using ML. 

## Project Overview
<p align="center">
<img src="static/Images/Project 4 outline.png" alt="" title="" width="600" height="600">
</p>
Fake news is a growing problem in today's society, and it can have serious consequences, including influencing public opinion and even shaping policy decisions. In this project, we aim to build a machine learning model that can accurately identify whether a given news article is fake or not.

## Technologies Used
We utilized the following technologies in our project:

- Scikit-learn for machine learning
- Python Pandas for data manipulation
- Python Matplotlib for data visualization
- HTML/CSS/Bootstrap for frontend web development
- JavaScript Plotly for data visualization
- SQL Database for data storage and retrieval

## Technical Requirements
Our project follows the technical requirements outlined in the assignment brief, including:

- Implementing a Python script to initialize, train, and evaluate our model
- Cleaning, normalizing, and standardizing our data prior to modeling
- Utilizing data retrieved from SQL or Spark
- Demonstrating meaningful predictive power with at least 75% classification accuracy or 0.80 R-squared
- Documenting our model optimization and evaluation process with iterative changes made to the model and the resulting changes in - - model performance in either a CSV/Excel table or in the Python script itself
- Printing or displaying overall model performance at the end of the script
- Maintaining a GitHub repository that is free of unnecessary files and folders and has an appropriate .gitignore in use
- Customizing the README as a polished presentation of the content of the project

## Group Members
- Johan Snyman
- Jon Wood 

## Dataset
The dataset used in this project consists of 20,00+ news articles labeled as either fake or real. We used 5000 of these for this project. The dataset is split into training and test sets to train and evaluate the machine learning models.

https://www.kaggle.com/c/fake-news/data

## Preprocessing
The preprocessing steps include:

Lowercasing the text

Tokenization

Removing stopwords

Stemming using the PorterStemmer algorithm

Vectorization

The text data is transformed into numerical features using the CountVectorizer class from the sklearn library. This is done to enable machine learning algorithms to process the text data.

## Model Training
Two classification models are used to identify fake news articles:

Logistic Regression

Passive Aggressive Classifier

Hyperparameter tuning is performed using GridSearchCV to optimize the models for the best performance.

## Model Evaluation
The performance of each model is evaluated using the following metrics:

Prediction Accuracy

Classification Report

Confusion Matrix


<p>
<img src="static/Images/logreg-results.jpg" alt="" title="" width="300" height="300">
</p>
<br>
<br>
<p>
<img src="static/Images/passive-aggressive-results.jpg" alt="" title="" width="300" height="300">
</p>

## Group Presentation
We will be giving a group presentation on our project, where all members will speak and present the project's content, transitions, and conclusions smoothly within the allotted time. We will also ensure that the presentation maintains audience interest throughout.

## Project Structure
```
Dataset
   |-- source-info.txt
   |-- test.csv
   |-- train.csv
ETL
   |-- ETL_Project_4.ipynb
   |-- Schema
   |   |-- Project 4 - DBD.png
   |   |-- Project_4 Database Schema.sql
   |   |-- QuickDBD-Project 4.pdf
   |-- cleanup.txt
ML
   |-- FAKE-NEWS-ML.ipynb
   |-- api_keys.py
   |-- logreg_model_optimization.png
   |-- model_optimization.png
Pickles
   |-- logisticreg_model.pkl
   |-- passive_aggressive_model.pkl
   |-- passiveagressive_model.pkl
   |-- tfidf_vectorizer.pkl
   |-- tfidfvect2.pkl
Presentation
   |-- Project-4-Presentation.pdf
Proposal
   |-- Project 4 - A-TEAM - Proposal.pdf
README.md
Static
   |-- Images
   |   |-- fake-new-facts.jpeg
app.py
requirements.txt
static
   |-- Images
   |   |-- Project 4 outline.png
   |   |-- fake.png
   |   |-- johan.jpg
   |   |-- jono.jpg
   |   |-- logreg-results.jpg
   |   |-- passive-aggressive-results.jpg
   |   |-- true.png
   |-- css
   |   |-- project4_style.css
templates
   |-- index.html
```   

## Running the Web Application
To run the web application, follow these steps:
1. Clone the repository
2. Install the required Python libraries using `pip install -r requirements.txt`
3. Run `python app.py` in the terminal
4. Open the web application in the browser at `http://localhost:5000`

## Future Work
- Improve the accuracy of the model by using more advanced techniques, such as deep learning
- Increase the size of the dataset to improve the generalization of the model
- Deploy the web application on a cloud platform, such as Google Cloud or Amazon AWS

## Acknowledgments
We would like to thank our bootcamp instructors for their guidance and support throughout this project. We would also like to thank the creators of the dataset used in this project. 

## References
- Scikit-learn documentation: https://scikit-learn.org/stable/documentation.html
- Bootstrap documentation: https://getbootstrap.com/docs/5.1/getting-started/introduction/
- Plotly documentation: https://plotly.com/javascript/
- Leaflet documentation: https://leafletjs.com/
