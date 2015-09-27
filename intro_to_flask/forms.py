from wtforms import Form, TextField, TextAreaField, SubmitField, HiddenField, validators, ValidationError, PasswordField
 
class ContactForm(Form):
	hidden_tag = HiddenField("hidden field")
	name = TextField("Name", [validators.DataRequired("Please enter your name.")])
	email = TextField("Email", [validators.DataRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
	subject = TextField("Subject", [validators.DataRequired()])
	message = TextAreaField("Message", [validators.DataRequired()])
	submit = SubmitField("Send")

class SignupForm(Form):
	firstname = TextField("First name",  [validators.Required("Please enter your first name.")])
	lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
	email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
	password = PasswordField('Password', [validators.Required("Please enter a password.")])
	submit = SubmitField("Create account")

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

	def validate(self):
		if not Form.validate(self):
			return False
	 
		user = User.query.filter_by(email = self.email.data.lower()).first()
		if user:
			self.email.errors.append("That email is already taken")
			return False
		else:
			return True