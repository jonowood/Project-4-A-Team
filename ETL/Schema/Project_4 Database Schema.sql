DROP TABLE IF EXISTS article_id, article_title, article_date, article_author, user_submit, article_text, text_corpus;

CREATE TABLE Article_ID (
    article_id INT PRIMARY KEY,
    article_label INT
);

CREATE TABLE Article_Title (
    article_id INT,
    article_title VARCHAR,
    FOREIGN KEY (article_id) REFERENCES Article_ID(article_id)
);

CREATE TABLE Article_Author (
    article_id INT,
    article_author VARCHAR,
    FOREIGN KEY (article_id) REFERENCES Article_ID(article_id)
);

CREATE TABLE Article_Text (
    article_id INT,
    article_text VARCHAR,
    FOREIGN KEY (article_id) REFERENCES Article_ID(article_id)
);

CREATE TABLE Article_Date (
    article_id INT,
    article_date DATE,
    FOREIGN KEY (article_id) REFERENCES Article_ID(article_id)
);

CREATE TABLE User_Submit (
    article_id INT,
    submit_id INT PRIMARY KEY,
    submit_date DATE,
    article_label INT,
    FOREIGN KEY (article_id) REFERENCES Article_ID(article_id)
);

CREATE TABLE Text_Corpus (
    article_id INT,
	text_corpus VARCHAR,
    FOREIGN KEY (article_id) REFERENCES Article_ID(article_id)
);