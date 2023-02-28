# Fake News Identification using Machine Learning

This Github repository contains the code and resources for our bootcamp project 4, where we have developed a machine learning model to identify fake news. 

## Project Overview
The proliferation of fake news has become a major concern in today's society. To combat the spread of misinformation, we have developed a machine learning model to identify fake news. We have used a dataset containing 1000 news articles, which has been labeled as either fake or real news. The model is built using Scikit-learn, a powerful machine learning library in Python. 

## Technologies Used
- Python (Scikit-learn, Pandas, Matplotlib)
- HTML/CSS/Bootstrap
- JavaScript (Plotly, Leaflet)

## Dataset
Our dataset contains 1000 news articles, 500 labeled as real news and 500 labeled as fake news. The data has been collected from various sources and preprocessed to remove any irrelevant information. The dataset is stored in a CSV file, which is included in the repository.

## Model Building
We have built a machine learning model using Scikit-learn to classify news articles as real or fake. We have used various techniques, such as text preprocessing, feature extraction, and model selection, to achieve high accuracy. The model is trained on 70% of the dataset and tested on the remaining 30%. We have achieved an accuracy of 95% on the test set.

## Technical Requirements for Project 4

### Data Model Implementation (20 points)
- A Python script initialises, trains, and evaluates a model (5 points)
- The data is cleaned, normalised, and standardised prior to modelling (5 points)
- The model utilises data retrieved from SQL or Spark (5 points)
- The model demonstrates meaningful predictive power at least 75% classification accuracy or 0.80 R-squared. (5 points)

### Data Model Optimisation (20 points)
- The model optimisation and evaluation process showing iterative changes made to the model and the resulting changes in model performance is documented in either a CSV/Excel table or in the Python script itself (10 points)
- Overall model performance is printed or displayed at the end of the script (10 points)

### GitHub Documentation (20 points)
- GitHub repository is free of unnecessary files and folders and has an appropriate .gitignore in use (10 points)
- The README is customised as a polished presentation of the content of the project (10 points)

### Group Presentation (20 points)
- All group members speak during the presentation. (5 points)
- Content, transitions, and conclusions flow smoothly within any time restrictions. (5 points)
- The content is relevant to the project. (5 points)
- The presentation maintains audience interest. (5 points)

## Project Structure
- `data/` directory contains the dataset in CSV format
- `notebooks/` directory contains Jupyter notebooks used for data analysis, preprocessing, and model building
- `static/` directory contains CSS and JavaScript files for the web application
- `templates/` directory contains HTML templates for the web application
- `app.py` is the main Python file for the web application
- `model.pkl` is the trained machine learning model in pickle format

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
- 
