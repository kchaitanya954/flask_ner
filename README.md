# Named Entity Recognition
Perform Named Entity Recognition on scrapped data and extract entities like city, person, organisation, Date, Geographical Entity, Product etc using spacy and flask.

### Import all the required 
```python
from flask import Flask, url_for, render_template, request
import spacy
from spacy import displacy
from flaskext.markdown import Markdown
import wikipedia
```

### Load the spacy english library
```python
nlp = spacy.load('en_core_web_sm')
```

### Extract the entities and labels using spacy npl.
```python
nlp=spacy.load('en_core_web_sm')
data = nlp(text)
```
There are two ways in which you can perform NER
1. Enter the text to which you want to perform NER

![alt text](https://github.com/kchaitanya954/NER-flask/blob/main/Screenshot%20at%202021-03-06%2023-55-25.png)

2. Enter the Name for which you want to perform NER based on wikipedia data. Using wikipedia api we can extract the data based on the given word.

```python
wikipedia.summary(word)
```

### We have used flask and Markdown module in flask to highlight all the entities.

```python
app=Flask(__name__)
Markdown(app))
```

We have used html templates for displaying 

