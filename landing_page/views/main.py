"""
Use views to define routes:
In Flask, a view is a Python function that is mapped to a URL.
"""

from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    phone = request.form['phone']

    # Save the user's information to an Excel file
    data = {'Name': [name], 'Phone': [phone]}
    df = pd.DataFrame(data)
    df.to_excel('Students.xlsx', index=True)

    return 'Thank you for registering!'
