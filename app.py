from flask import Flask, render_template, url_for, redirect, request
import subprocess

app = Flask(__name__)

# Mapping of script names to their file paths
scripts = {
    'CompanyUserLogin': 'CompanyUserLogin.py',
    'BrandSettings': 'BrandSettings.py',
    'SystemSettings': 'SystemSettings.py',
    'CompanySettings': 'CompanySettings.py',
    'BankInvoice': 'BankandInvoice.py',  # Renamed to match request
    'Language': 'LanguageCheck.py'
}

# Home route to display buttons
@app.route('/')
def index():
    return render_template('index.html')

# Route to run each script and display results
@app.route('/run_script/<script_name>')
def run_script(script_name):
    # Check if script_name exists in the dictionary
    if script_name in scripts:
        script_path = scripts[script_name]

        try:
            # Run the Python script using subprocess and capture output
            result = subprocess.run(['python', script_path], capture_output=True, text=True)
            output = result.stdout + result.stderr  # Combine stdout and stderr

            return render_template('result.html', script_name=script_name, output=output)
        
        except Exception as e:
            return f"An error occurred while running {script_name}: {str(e)}"
    
    else:
        return f"Script {script_name} not found."

# Error handler for any 404 (page not found) error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
