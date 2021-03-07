from flask import Flask, url_for, render_template, request
import spacy
from spacy import displacy
from flaskext.markdown import Markdown
import wikipedia

nlp=spacy.load('en_core_web_sm')

app=Flask(__name__)
Markdown(app)


@app.route('/')
def index():
    return render_template('index.html')
# method to render ner and to display it
@app.route('/', methods=["GET", "POST"])
def extract():
    if request.method == 'POST':
        if request.form['submit_button'] == 'NER Submit':
            rawtext = request.form['rawtext']
            
            
        elif request.form['submit_button'] == 'NER wiki Submit':
            rawtext = wikipedia.summary(request.form['rawtext'])

        docx = nlp(rawtext)
        html = displacy.render(docx, style='ent')
        result = html

    return render_template('results.html', rawtext=rawtext, result=result)




if __name__ == '__main__':

    app.run(debug=True)
