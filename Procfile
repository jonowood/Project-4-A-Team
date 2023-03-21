web: gunicorn app:app
release: python -c 'import nltk;nltk.download('stopwords')'
heroku config:set NLTK_DATA='/app/static/nltk_data'