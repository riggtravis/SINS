from wtforms import Form
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import validators
from wtforms import HiddenField

# I think there is a more readable way to write this than as a lambda. This is
# an extremely javascript way of doing things. Not that doing things in The
# JavaScript Way is a bad thing, it's just that most Python programmers are
# going to be doing things in a different way, and we should try to accomodate
# that style of thinking.

# strip_filter = lambda x: x.strip() if x else None
def strip_filter(x):
	# This can be written without an else block as
	#
	#	if x:
	#		return x.strip()
	#	return None
	#
	# But that's not as clear for people who are unfamiliar with some of the
	# strange things that programmers do.
	if x:
		return x.strip()
	else:
		return None

class TopicCreateForm(Form):
	# The forum_id should be implicit based on where the user entered the create
	# topic command. This might mean that I will need to pass the forum_id in
	# the URI in order for this to work. It's just something I'm going to have
	# to look into.
	
	subject = StringField(
		'Subject',
		[validators.Length(min=1, max=140)],
		filters=[strip_filter]
	)
	
	# If the user has the power to make posts stick, the option should be given
	# to them.
	
	# Find a way to include the post form when the topic form is presented. This
	# is probably going to be done in a view controller.