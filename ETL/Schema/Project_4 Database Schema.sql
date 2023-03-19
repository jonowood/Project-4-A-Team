DROP TABLE IF EXISTS User_Submit,Article_Date, Article_Text, Article_Author, Article_Title, Article_ID;

CREATE TABLE Article_ID (
    article_id INT PRIMARY KEY,
    article_label INT
);

CREATE TABLE Article_Title (
    article_id INT,
    title VARCHAR,
    FOREIGN KEY (article_id) REFERENCES Article_ID(article_id)
);

CREATE TABLE Article_Author (
    article_id INT,
    author VARCHAR,
    FOREIGN KEY (article_id) REFERENCES Article_ID(article_id)
);

CREATE TABLE Article_Text (
    article_id INT,
    text VARCHAR,
    FOREIGN KEY (article_id) REFERENCES Article_ID(article_id)
);

CREATE TABLE Article_Date (
    article_id INT,
    date DATE,
    FOREIGN KEY (article_id) REFERENCES Article_ID(article_id)
);

CREATE TABLE User_Submit (
    article_id INT,
    submit_id INT PRIMARY KEY,
    date DATE,
    article_label INT,
    FOREIGN KEY (article_id) REFERENCES Article_ID(article_id)
);
