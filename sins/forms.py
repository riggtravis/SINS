from wtforms import Form

from wtforms import StringField
from wtforms import TextAreaField
from wtforms import DateTimeField
from wtforms import SelectField
from wtforms import PasswordField

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

##################
# Ban Forms
##################

# Bans should be initiated by administators or moderators from a user's profile
# page. The only thing that administators can edit is when the end date of the
# ban is.
class BanCreateForm(Form):
	end_date = DateTimeField(
		'End Date',
		# We need to validate that the end date is some time after now.
		
		filters=[strip_filter]
	)

class BanUpdateForm(BanCreateForm):
	ban_id = HiddenField()

##################
# Forum Forms
##################

# Creation of a forum is a big deal. This is something that should only be done
# by administators. It will need to be described by a power.
class ForumCreateForm(Form):
	title = StringField(
		'Title',
		[validators.Length(min=1, max=30), validators.required()],
		filters=[strip_filter]
	)
	
	# What forum this forum belongs to should be handled with a drop down menu.
	# The forum dropdown menu should be populated based on the current scope
	# when the user opened the form. Any forum that was displaying on the page
	# at the time should be availabe, as well as putting the current scoped
	# parent for the parent for the new forum. So if the user is on the index
	# page the user should be able to add a forum with no parent, or add a
	# category to any of the forums with no parents. If the user were looking at
	# a forum called "Off Topic" the user would be able to add a category to
	# "Off Topic" or to any forum that belongs to "Off Topic". The process
	# should work non recursively because it would present the user with too
	# many choices to be useful.
	
	# In order to create the functionality of a scoped drop down list we need to
	# use a SelectField and then not assign choices until we are using the form
	# in our view controller.
	parent_id = SelectField(
		'Parent',
		[validators.optional()],
		filters=[strip_filter]
	)

class ForumUpdateForm(ForumCreateForm):
	forum_id = HiddenField()

##################
# Group Forms
##################

class GroupCreateForm(Form):
	title = StringField(
		'Group Name',
		[validators.Length(min=1, max=30), validators.required()]
		filters=[strip_filter]
	)

class GroupUpdateForm(GroupCreateForm):
	group_id = HiddenField()

##################
# Membership Forms
##################

# This is another dynamically scoped form. This form should be accessed from a
# user's profile. So the assigner of the membership doesn't specify what user
# they are adding to a group. Instead they specify what group they are adding a
# user to.

class MembershipCreateForm(form):
	# Rember that the SelectField must be populated dynamically later.
	group_id = SelectField(
		'Group',
		[validators.required()]
		filters=[strip_filter]
	)

# Because this entity has a composite primary key, it doesn't make sense to
# update it. Instead, if a user shouldn't be a member of a group anymore, their
# membership attribute should be deleted.

##################
# Permission Forms
##################

# This will work almost identically to the membership form. This time, the form
# should be reached by clicking on a link to add a new power to a group. So
# the only field should be which power is being given to a group.

class PermissionCreateForm(Form):
	power_id = SelectField(
		'Group',
		[validators.required()]
		filters=[strip_filter]
	)

##################
# Post Forms
##################

class  PostCreateForm(Form):
	message = TextAreaField(
		'Message',
		[validators.Length(min=1), validators.required()],
		filters=[strip_filter]
	)

class PostUpdateForm(PostCreateForm):
	post_id = HiddenField()

##################
# Power Forms
##################

# I'm not sure it actually makes sense to have power forms. I think instead this
# will be implemented in the initialize DB scripts.

##################
# Topic Forms
##################

class TopicCreateForm(Form):
	# The forum_id should be implicit based on where the user entered the create
	# topic command. This might mean that I will need to pass the forum_id in
	# the URI in order for this to work. It's just something I'm going to have
	# to look into.
	
	subject = StringField(
		'Subject',
		[validators.Length(min=1, max=140), validators.required()],
		filters=[strip_filter]
	)
	
	# If the user has the power to make posts stick, the option should be given
	# to them.
	
	# Find a way to include the post form when the topic form is presented. This
	# is probably going to be done in a view controller.

class TopicUpdateForm(TopicCreateForm):
	# I'm not sure why this line has to be here. I have a guess that if you do
	# not include this line, then the update form will give the user access to
	# change the primary key. Which is bad.
	topic_id = HiddenField()

##################
# User Forms
##################

# Think of this as registration.
class UserCreateForm(Form):
	username = StringField(
		'Username',
		[validators.Length(min=1, max=30), validators.required()],
		filters=[strip_filter]
	)
	
	# I'm not sure how to implement password. There might be a specific field.
	# There sure is.
	password = PasswordField(
		'Password',
		[validators.Length(min=8), validators.required()],
		filters=[strip_filter]
	)
	
	# An email address field makes sense at sign up, even if I don't decide to
	# make it a required value.
	email = StringField(
		'E-Mail Address',
		[validators.email(), validators.required()],
		filters=[strip_filter]
	)
	
	# It doesn't make sense for the user to upload an avatar at registration
	# Similarly it doesn't make sense to let the user create a signature at the
	# time of registration.