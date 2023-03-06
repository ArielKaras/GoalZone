"""
Use routes to define the URL paths that your application will respond to.
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
import pandas as pd
import os

main_bp = Blueprint('views', __name__, template_folder='templates')


@main_bp.route('/')
def landing_page():
    return render_template('landing_page.html')


@main_bp.route('/register', methods=['POST'])
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

    flash('We will contact with you soon!')  # Display a flash message
    return redirect(url_for('views.landing_page'))  # Redirect to the landing page
