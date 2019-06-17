from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
<body>
    <h2>Signup</h2>
    <form action='/valid' method='POST'>
        <label for='user'>Username:
        <input id='user' name='username' type='text' autofocus required></label>
        <label for='passwrd'>Password:
        <input id='passwrd' name='password' type='password' required></label>
        <p class='error'>{password_err}</p>
        <label for='verify'>Verify Password:
        <input id='verify' name='verify_password' type='password' required></label>
        <label for='mail'>Email (Optional):
        <input id='mail' name='email' type='email'></label>
        <input type='submit' value='Submit'>
    </form>
</body>
</html>
"""

@app.route("/valid", methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

app.run()
