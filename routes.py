from app import app
from flask import Flask, render_template

import forms

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about', methods = ['GET', 'POST'])
def about():
    form = forms.addtaskform()
    if form.validate_on_submit():
        print("SUBMITTED TITLE", form.title.data)
        return render_template('about.html', form=form, title=form.title.data)
    return render_template('about.html', form=form)