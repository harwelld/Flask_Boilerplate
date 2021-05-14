# -----------------------------------------------------------------------------
# Name:        exampleForm.py
#
# Purpose:     Application models
#
# Author:      Dylan Harwell
# -----------------------------------------------------------------------------

from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField, StringField, SelectField
from wtforms.validators import *


class ExampleForm(FlaskForm):
	pass


###############################################################################
if __name__ == '__main__':
    pass
