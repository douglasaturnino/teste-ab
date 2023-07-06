import numpy as np
import pandas as pd
import os
from thompson_agent import thompson_agent
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/home')
def index():
    # Thompson Agent
    page = thompson_agent.get_page()
    
    pages = {
        'blue': 'pg_layout_blue.html',
        'red': 'pg_layout_red.html'
    }
    
    return render_template(pages[page])

@app.route('/yes', methods=['POST'])
def yes_event():

    if request.form['yescheckbox'] == 'red':
        visit = 1
        click = 1
        group = 'treatment'
    else:
        visit = 1
        click = 1
        group = 'control'

    df_raw = pd.DataFrame({
        'click': click,
        'visit': visit,
        'group': group}, index=[0])

    df_raw.to_csv('pa_bayesion/mab/data_experiment.csv', mode='a', index=False, header=False)


    return redirect(url_for('index'))

@app.route('/no', methods=['POST'])
def no_event():

    if request.form['nocheckbox'] == 'red':
        visit = 1
        click = 0
        group = 'treatment'
    else:
        visit = 1
        click = 0
        group = 'control'
    
    df_raw = pd.DataFrame({
        'click': click,
        'visit': visit,
        'group': group}, index=[0])
    
    df_raw.to_csv('pa_bayesion/mab/data_experiment.csv', mode='a', index=False, header=False)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)