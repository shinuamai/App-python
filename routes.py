from app import app
from flask import Flask, render_template

import forms

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    form = forms.addtaskform()
    return render_template('about.html', form=form)