from wtforms import Form, TextField, TextAreaField, SubmitField, HiddenField, validators, ValidationError
 
class ContactForm(Form):
  hidden_tag = HiddenField("hidden field")
  name = TextField("Name", [validators.DataRequired("Please enter your name.")])
  email = TextField("Email", [validators.DataRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
  subject = TextField("Subject", [validators.DataRequired()])
  message = TextAreaField("Message", [validators.DataRequired()])
  submit = SubmitField("Send")