import os
import numpy as np
import pandas as pd
from variante import variante
from thompson_agent import thompson_agent
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/home')
def index():
    # Thompson Agent
    best_pege = thompson_agent.get_page()
    
    pages = {
        'blue': 'pg_layout_blue.html',
        'red': 'pg_layout_red.html'
    }
    
    return render_template(pages[best_pege])

@app.route('/yes', methods=['POST'])
def yes_event():
    
    page = request.form['forwardbtn']

    pages = {
        'blue': variante(1,1,'control'),
        'red' : variante(1,1,'treatment')
    }

    pages[page].salvar_experiment()
   
    return redirect(url_for('index'))

@app.route('/no', methods=['POST'])
def no_event():

    page = request.form['forwardbtn']

    pages = {
        'blue': variante(1,0,'control'),
        'red' : variante(1,0,'treatment')
    }
    
    pages[page].salvar_experiment()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)