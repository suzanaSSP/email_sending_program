from flask import Flask, request

app = Flask(__name__)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    # Process the data (e.g., store in a database, send emails, etc.)
    return "Form data submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)