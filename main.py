from flask import Flask, request, redirect, render_template
import os
import cgi
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/') #path to form - signup.html
def index():
    return render_template('signup.html')

#EMAIL - string.count(substring) - functions
def alphagreater(email):
    if email.count('.') > 1:
        return True
    else:
        return False
def alphaless(email):
    if email.count('.') < 1:
        return True
    else:
        return False

def alpha_greater(mail):
    if mail.count('@') > 1:
        return True
    else:
        return False
def alpha_less(mail):
    if mail.count('@') < 1:
        return True
    else:
        return False

def empty_field(use_pass):
    if use_pass:
        return True
    else: 
        return False

@app.route('/', methods=['POST'])
def validate_signup():    
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
       

    #username validation#
    if not empty_field(username):  #username == '':
        username_error = 'Username required.'
        username = ''
        password_error = 'Please re-enter password'
        #verify_error = 'Enter password again'
        
    elif len(username) < 3 or len(username) > 20:
        username_error = 'Password should be 3 - 20 characters long.'
        username = ''
        password_error = 'Please re-enter password'
        verify_error = 'Enter password again'
    elif ' ' in username:
        username_error = 'No spaces allowed in username'
        username = ''
        password_error = 'Please re-enter password'
        verify_error = 'Enter password again'

        
    #password validation#
    if not empty_field(password): #not password
        password_error = 'Password required.'
        password = ''
    elif len(password) < 3 or len(password) > 20:
        password_error = 'Not in valid range'
        password = ''
    elif ' ' in password:
        password_error = 'No spaces allowed in password.'
        password = ''

    #do passwords match
    if verify != password:
        verify_error = 'Passwords entered do not match. Please re-enter.'
        verify = ''


    #need to count strong (alphabet)#
    #also need to check if anything is in email field - if there is process#
    if empty_field(email):
        pass
        if ' ' in email: #check for spaces
            email_error = 'No spaces allowed in email address.'
            email = ''
        elif alphagreater(email): #('.') > 1 or string.count('.') < 1:
            email_error = 'Only one period allowed in email address.'
            email = ''
        elif alphaless(email):
            email_error = 'One period required in email address.'
            email = ''
        elif alpha_greater(email):
            email_error = 'Only one ampersand allowed in email address.'
            email = ''
        else:
            if alpha_less(email): 
                email_error = 'One ampersand required in email address.'
                email = ''

    #if no error then all is well to render template (welcome message) otherwise 
    #from render template lesson i think
    if not username_error and not password_error and not verify_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html', username_error=username_error, username=username, password_error=password_error, password=password, verify_error=verify_error, verify=verify, email_error=email_error, email=email)

    
        
@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()