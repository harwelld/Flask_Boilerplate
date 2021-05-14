# ------------------------------------------------------------
# Name:        controller.py
#
# Purpose:     Flask server routing
#
# Author:      Dylan Harwell
# -------------------------------------------------------------

from app import app
from app.models.exampleForm import ExampleForm
from app.includes.dbaccessor import *
from flask import Flask, request, render_template, redirect, url_for, flash, jsonify


@app.route("/")
def redirectHome():
    return redirect(url_for('home'))


@app.route("/home", methods=['GET', 'POST'])
def home():
    form = ExampleForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        flash('Message', 'success')
        return redirect(url_for('home'))

    return render_template('index.html', form=form)


###############################################################################
if __name__ == '__main__':
    pass
