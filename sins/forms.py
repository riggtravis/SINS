from wtforms import Form

from wtforms import StringField
from wtforms import TextAreaField
from wtforms import DateTimeField
from wtforms import SelectField
from wtforms import PasswordField
from wtforms import FileField

from wtforms import validators

from wtforms import HiddenField

""" Forms 

Classes:
********

* BanCreateForm
** Used to ban a user.

* BanUpdateForm
** Used to edit a ban.

* ForumCreateForm
** Used to create a discussion category.

* ForumUpdateForm
** Used to edit a discussion category.

* GroupCreateForm
** Used to create a group of users for power deligation.

* GroupUpdateForm
** Used to edit a group of users.

* MembershipCreateForm
** Used to add a user to a group.

* PermissionCreateForm
** Used to assign a power to a group.

* PostCreateForm
** Used to post a message to a discussion.

* PostUpdateForm
** Used to edit a posted message.

* TopicCreateForm
** Used to create a new topic of discussion.

* TopicUpdateForm
** Used to edit a discussion topic.

* UserCreateForm
** Used to allow a person to register for the community.

* UserUpdateForm
** Allows a user to update their profile.

Functions:
**********

* strip_filter
** strips white space of an entry field.

"""

# I think there is a more readable way to write this than as a lambda. This is
# an extremely javascript way of doing things. Not that doing things in The
# JavaScript Way is a bad thing, it's just that most Python programmers are
# going to be doing things in a different way, and we should try to accomodate
# that style of thinking.

# strip_filter = lambda x: x.strip() if x else None
def strip_filter(x):
	""" This function is used to strip whitespace from forms.
	
	Arguments:
	x -- A string that will be stripped
	
	Returns:
	If x is a string, x without trailing or leading whitespace
	Otherwise it returns the None value.
	
	"""
	
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
 ######                   #######                             
 #     #   ##   #    #    #        ####  #####  #    #  ####  
 #     #  #  #  ##   #    #       #    # #    # ##  ## #      
 ######  #    # # #  #    #####   #    # #    # # ## #  ####  
 #     # ###### #  # #    #       #    # #####  #    #      # 
 #     # #    # #   ##    #       #    # #   #  #    # #    # 
 ######  #    # #    #    #        ####  #    # #    #  ####  
##################

# Bans should be initiated by administators or moderators from a user's profile
# page. The only thing that administators can edit is when the end date of the
# ban is.
class BanCreateForm(Form):
	""" This form is used when a user gets banned. """
	
	end_date = DateTimeField(
		'End Date',
		# We need to validate that the end date is some time after now.
		
		filters=[strip_filter]
	)

class BanUpdateForm(BanCreateForm):
	""" This form is used if a user's ban contains a mistake. """
	
	ban_id = HiddenField()

##################
 #######                                #######                             
 #        ####  #####  #    # #    #    #        ####  #####  #    #  ####  
 #       #    # #    # #    # ##  ##    #       #    # #    # ##  ## #      
 #####   #    # #    # #    # # ## #    #####   #    # #    # # ## #  ####  
 #       #    # #####  #    # #    #    #       #    # #####  #    #      # 
 #       #    # #   #  #    # #    #    #       #    # #   #  #    # #    # 
 #        ####  #    #  ####  #    #    #        ####  #    # #    #  ####  
##################

# Creation of a forum is a big deal. This is something that should only be done
# by administators. It will need to be described by a power.
class ForumCreateForm(Form):
	""" This form is used when a new discussion category is started. """
	
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
	""" This form is used when a discussion category is changed. """
	
	forum_id = HiddenField()

##################
  #####                                 #######                             
 #     # #####   ####  #    # #####     #        ####  #####  #    #  ####  
 #       #    # #    # #    # #    #    #       #    # #    # ##  ## #      
 #  #### #    # #    # #    # #    #    #####   #    # #    # # ## #  ####  
 #     # #####  #    # #    # #####     #       #    # #####  #    #      # 
 #     # #   #  #    # #    # #         #       #    # #   #  #    # #    # 
  #####  #    #  ####   ####  #         #        ####  #    # #    #  ####  
##################

class GroupCreateForm(Form):
	""" This form is used when a new group is created. """
	
	title = StringField(
		'Group Name',
		[validators.Length(min=1, max=30), validators.required()],
		filters=[strip_filter]
	)

class GroupUpdateForm(GroupCreateForm):
	""" This form is used when a group changes. """
	
	group_id = HiddenField()

##################
 #     #                                                              #######                             
 ##   ## ###### #    # #####  ###### #####   ####  #    # # #####     #        ####  #####  #    #  ####  
 # # # # #      ##  ## #    # #      #    # #      #    # # #    #    #       #    # #    # ##  ## #      
 #  #  # #####  # ## # #####  #####  #    #  ####  ###### # #    #    #####   #    # #    # # ## #  ####  
 #     # #      #    # #    # #      #####       # #    # # #####     #       #    # #####  #    #      # 
 #     # #      #    # #    # #      #   #  #    # #    # # #         #       #    # #   #  #    # #    # 
 #     # ###### #    # #####  ###### #    #  ####  #    # # #         #        ####  #    # #    #  ####  
##################

# This is another dynamically scoped form. This form should be accessed from a
# user's profile. So the assigner of the membership doesn't specify what user
# they are adding to a group. Instead they specify what group they are adding a
# user to.

class MembershipCreateForm(form):
	""" This form is used when someone is added to a group. """
	
	# Rember that the SelectField must be populated dynamically later.
	group_id = SelectField(
		'Group',
		[validators.required()],
		filters=[strip_filter]
	)

# Because this entity has a composite primary key, it doesn't make sense to
# update it. Instead, if a user shouldn't be a member of a group anymore, their
# membership attribute should be deleted.

##################
 ######                                                          #######                             
 #     # ###### #####  #    # #  ####   ####  #  ####  #    #    #        ####  #####  #    #  ####  
 #     # #      #    # ##  ## # #      #      # #    # ##   #    #       #    # #    # ##  ## #      
 ######  #####  #    # # ## # #  ####   ####  # #    # # #  #    #####   #    # #    # # ## #  ####  
 #       #      #####  #    # #      #      # # #    # #  # #    #       #    # #####  #    #      # 
 #       #      #   #  #    # # #    # #    # # #    # #   ##    #       #    # #   #  #    # #    # 
 #       ###### #    # #    # #  ####   ####  #  ####  #    #    #        ####  #    # #    #  ####  
##################

# This will work almost identically to the membership form. This time, the form
# should be reached by clicking on a link to add a new power to a group. So
# the only field should be which power is being given to a group.
class PermissionCreateForm(Form):
	""" This form is used when a group gains a power. """
	
	power_id = SelectField(
		'Group',
		[validators.required()],
		filters=[strip_filter]
	)

##################
 ######                         #######                             
 #     #  ####   ####  #####    #        ####  #####  #    #  ####  
 #     # #    # #        #      #       #    # #    # ##  ## #      
 ######  #    #  ####    #      #####   #    # #    # # ## #  ####  
 #       #    #      #   #      #       #    # #####  #    #      # 
 #       #    # #    #   #      #       #    # #   #  #    # #    # 
 #        ####   ####    #      #        ####  #    # #    #  ####  
##################

class PostCreateForm(Form):
	""" This form is used when a post is made. """
	
	message = TextAreaField(
		'Message',
		[validators.Length(min=1), validators.required()],
		filters=[strip_filter]
	)

class PostUpdateForm(PostCreateForm):
	""" This form is used when a post is edited. """
	
	post_id = HiddenField()

##################
 ######                                 #######                             
 #     #  ####  #    # ###### #####     #        ####  #####  #    #  ####  
 #     # #    # #    # #      #    #    #       #    # #    # ##  ## #      
 ######  #    # #    # #####  #    #    #####   #    # #    # # ## #  ####  
 #       #    # # ## # #      #####     #       #    # #####  #    #      # 
 #       #    # ##  ## #      #   #     #       #    # #   #  #    # #    # 
 #        ####  #    # ###### #    #    #        ####  #    # #    #  ####  
##################

# I'm not sure it actually makes sense to have power forms. I think instead this
# will be implemented in the initialize DB scripts.

##################
 #######                           #######                             
    #     ####  #####  #  ####     #        ####  #####  #    #  ####  
    #    #    # #    # # #    #    #       #    # #    # ##  ## #      
    #    #    # #    # # #         #####   #    # #    # # ## #  ####  
    #    #    # #####  # #         #       #    # #####  #    #      # 
    #    #    # #      # #    #    #       #    # #   #  #    # #    # 
    #     ####  #      #  ####     #        ####  #    # #    #  ####  
##################

class TopicCreateForm(Form):
	""" This form is used when a new topic is made. """
	
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
	""" This form is used when a topic is changed. """
	
	# I'm not sure why this line has to be here. I have a guess that if you do
	# not include this line, then the update form will give the user access to
	# change the primary key. Which is bad.
	topic_id = HiddenField()
	
	forum_id = SelectField(
		'Forum',
		[validators.optional()],
		filters=[strip_filter]
	)

##################
 #     #                         #######                             
 #     #  ####  ###### #####     #        ####  #####  #    #  ####  
 #     # #      #      #    #    #       #    # #    # ##  ## #      
 #     #  ####  #####  #    #    #####   #    # #    # # ## #  ####  
 #     #      # #      #####     #       #    # #####  #    #      # 
 #     # #    # #      #   #     #       #    # #   #  #    # #    # 
  #####   ####  ###### #    #    #        ####  #    # #    #  ####  
##################

# Think of this as registration.
class UserCreateForm(Form):
	""" This form is used when a user registers. """
	
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
	
	# Confirming the password is important. Typos are annoying.
	
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

# This of updates as customizing a user's profile.
class UserUpdateForm(UserCreateForm):
	""" This for is used when a user updates their profile. """
	
	# I need to validate that the username doesn't contain any whitespace at all
	
	user_id		= HiddenField()
	username	= HiddenField()
	
	# Instead of a text form for the avatar, I need a way to upload a file.
	avatar = FileField('Avatar', [validators.regexp('^[^/\\]\.png$')])
	
	# I'm not sure what this function does. I believe it ensures that the file
	# uploaded by the user is actually an image file and not a text file that is
	# wearing a disquise.
	def validate_image(form, field):
		""" This function ensures that images are okay. """
		# I need to document this function better, but the clarity of what it
		# does is not at a level where I can comfortably do so.
		
		if field.data:
			field.data = re.sub('[^a-z0-9_.-]', '_', field.data)

##################
 #                                 #######                             
 #        ####   ####  # #    #    #        ####  #####  #    #  ####  
 #       #    # #    # # ##   #    #       #    # #    # ##  ## #      
 #       #    # #      # # #  #    #####   #    # #    # # ## #  ####  
 #       #    # #  ### # #  # #    #       #    # #####  #    #      # 
 #       #    # #    # # #   ##    #       #    # #   #  #    # #    # 
 #######  ####   ####  # #    #    #        ####  #    # #    #  ####  
##################

# I will work on learning how to do this later. For right now I need to work on
# uploading files.