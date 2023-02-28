<p align="center">
<img src="Static/Images/fake-new-facts.jpeg" alt="" title="" width="600" height="600">
</p>

# Fake News Identification using Machine Learning
This is our group's project for Project 4, where we were tasked to solve, analyze, or visualize a problem using machine learning (ML) with the other technologies we've learned. We chose to tackle the problem of identifying fake news using ML. 

## Project Overview
Fake news is a growing problem in today's society, and it can have serious consequences, including influencing public opinion and even shaping policy decisions. In this project, we aim to build a machine learning model that can accurately identify whether a given news article is fake or not.

## Technologies Used
We utilized the following technologies in our project:

- Scikit-learn for machine learning
- Python Pandas for data manipulation
- Python Matplotlib for data visualization
- HTML/CSS/Bootstrap for frontend web development
- JavaScript Plotly for interactive data visualization
- SQL Database for data storage and retrieval
- Google Cloud SQL for cloud-based SQL hosting

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

## Dataset
Our dataset contains 1000 news articles, 500 labeled as real news and 500 labeled as fake news. The data has been collected from various sources and preprocessed to remove any irrelevant information. The dataset is stored in a CSV file, which is included in the repository.

## Model Building
We have built a machine learning model using Scikit-learn to classify news articles as real or fake. We have used various techniques, such as text preprocessing, feature extraction, and model selection, to achieve high accuracy. The model is trained on 70% of the dataset and tested on the remaining 30%. We have achieved an accuracy of 95% on the test set.

## Group Members
- Johan Snyman
- Jon Wood 

## Group Presentation
We will be giving a group presentation on our project, where all members will speak and present the project's content, transitions, and conclusions smoothly within the allotted time. We will also ensure that the presentation maintains audience interest throughout.

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
