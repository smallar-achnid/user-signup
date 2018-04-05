from flask import Flask, request, redirect, render_template
import cgi
app = Flask(__name__)
app.config['DEBUG'] = True

def email_verification(email):
	at_counter = 0
	dot_counter = 0
	if email == "":
		return True
	else:
		for char in email:
			if char == "@":
				at_counter += 1
			elif char == ".":
				dot_counter += 1
	if at_counter == 1 and dot_counter == 1:
		return True
	else:
		return False
def username_password_verification(text):
	if len(text) < 3 or len(text) > 20 or ' ' in text:
		return False
	else:
		return True


@app.route("/welcome", methods=['POST'])
def welcome():
	content = "<p>Welcome {0}<p>".format('username')
	return content


@app.route('/signup', methods=['POST'])
def verification():
	username = request.form['username']
	password = str(request.form['password'])
	verify_password = str(request.form['verify-password'])
	email = request.form['email']
	#initializing variables:
	username_error = ''
	password_error = ''
	verify_password_error = ''
	email_error = ''
	
	error = 0
	if username_password_verification(username) == False:
		error += 1
		username_error = "Username is invalid. Please try again."
	if username_password_verification(password) == False:
		error += 1
		password_error = "Password is invalid. Please try again." 
	if password != verify_password:
		error += 1
		verify_password_error = "Passwords do not match. Please try again."  
		print(verify_password_error)
	if email_verification(email) == False:
		error += 1
		email_error = "Invalid email. Please try again." 

	
	print (error)

	if error > 0:
		#total_error = username_error + "&" + password_error + "&" + verify_password_error + "&" + email_error
		return render_template('edit.html', username=username, email=email, uerror=username_error, perror=password_error, verror=verify_password_error, eerror=email_error)
	else:    # if we didn't redirect by now, then all is well
		print ("Success!")
		return render_template('welcome.html', username=username)

@app.route("/")
def index():
	return render_template('edit.html')
app.run()