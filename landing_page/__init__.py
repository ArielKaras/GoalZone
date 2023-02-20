import time

from flask import Flask, request, render_template, redirect, url_for, flash
from landing_page.config import MAINTENANCE_MODE
import pandas as pd
import os

app = Flask(__name__)  # Create the Flask app
app.config.from_object('landing_page.config')  # Load the configuration from the config.py file


@app.before_request
def maintenance_mode():
    if app.config['MAINTENANCE_MODE']:  # If the app is in maintenance mode
        if request.endpoint in ['landing_page',
                                'register']:  # If the user is trying to access the landing page or register page
            return redirect(url_for('maintenance'))  # Redirect them to the maintenance page


@app.route('/maintenance')
def maintenance():
    if not app.config['MAINTENANCE_MODE']:  # If the app is not in maintenance mode
        return redirect(url_for('landing_page'))  # Redirect them to the landing page
    return render_template('maintenance.html')  # Render the maintenance page template


@app.route('/')
def landing_page():
    return render_template('landing_page.html')


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']  # Get the name from the form
    phone = request.form['phone']  # Get the phone number from the form

    # Create a DataFrame with the new data
    data = {'Name': [name], 'Phone': [phone], 'Date': [pd.Timestamp.now()]}  # Create a dictionary with the data
    df = pd.DataFrame(data)  # Create a DataFrame from the dictionary

    if os.path.isfile('Students.xlsx'):  # Check if the Excel file already exists

        # If it exists, load the existing data into a DataFrame
        existing_df = pd.read_excel('Students.xlsx')

        # Append the new data to the existing DataFrame
        df = pd.concat([existing_df, df])

    # Save the updated DataFrame to the Excel file
    df.to_excel('Students.xlsx', index=False)

    flash('Thank you for registering!') # Display a flash message
    return redirect(url_for('landing_page'))


if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode (for development)
