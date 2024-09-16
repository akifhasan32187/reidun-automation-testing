from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

# Function to execute Python scripts
def run_script(script_name):
    try:
        result = subprocess.run(['python', script_name], capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run/<script_name>')
def run(script_name):
    script_mapping = {
        'login': 'CompanyUserLogin.py',
        'brand': 'BrandSettings.py',
        'system': 'SystemSettings.py',
        'company': 'CompanySettings.py',
        'bank': 'BankandInvoice.py'
    }
    script_to_run = script_mapping.get(script_name)
    if script_to_run:
        output = run_script(script_to_run)
        return render_template('result.html', output=output)
    else:
        return "Invalid Script", 404

if __name__ == '__main__':
    app.run(debug=True)
