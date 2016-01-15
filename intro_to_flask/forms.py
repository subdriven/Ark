from wtforms import Form, StringField, TextAreaField, SubmitField, validators, ValidationError, PasswordField
 
class AnimalEntry(Form):
  name = StringField("Name", [validators.DataRequired("Please enter animal's name."), validators.Length(min=2, max=100), validators.InputRequired()])
  regName = StringField("Registered Name", [validators.Length(max=100)])
  breed = StringField("Breed")
  sex = TextAreaField("Sex")
  height = StringField("Height")
  color = StringField("Color", [validators.Length(max=50)])
  submit = SubmitField("Send")

class SignupForm(Form):
  firstname = StringField("First name",  [validators.DataRequired("Please enter your first name.")])
  lastname = StringField("Last name",  [validators.DataRequired("Please enter your last name.")])
  email = StringField("Email",  [validators.DataRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('Password', [validators.DataRequired("Please enter a password.")])
  submit = SubmitField("Create account")

class SearchForm(Form):
  name = StringField("Animal name")
  

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
