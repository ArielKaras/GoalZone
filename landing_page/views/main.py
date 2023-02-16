"""
Use views to define routes:
In Flask, a view is a Python function that is mapped to a URL.
"""

from flask import Flask, request, render_template
import pandas as pd
import os

app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    phone = request.form['phone']

    # Create a DataFrame with the new data
    data = {'Name': [name], 'Phone': [phone]}
    df = pd.DataFrame(data)

    # Check if the Excel file already exists
    if os.path.isfile('Students.xlsx'):
        # If it exists, load the existing data into a DataFrame
        existing_df = pd.read_excel('Students.xlsx')

        # Append the new data to the existing DataFrame
        df = pd.concat([existing_df, df])

    # Save the updated DataFrame to the Excel file
    df.to_excel('Students.xlsx', index=False)

    return 'Thank you for registering!'
