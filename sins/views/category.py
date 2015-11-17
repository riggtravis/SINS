# The basic view that a user will be greated with when first landing on a SINS
# based forum will be a list of all the different discussion categories that are
# available. Therefor the root (home) view will be held here in the category
# view controller.

from pyramid.view import view_config
from pyramid.view import view_defaults

# We're going to want to be able to use our services. Specifically in this view
# file we want to use the forum service.
from ..models.services.forum import ForumRecordService

# Views should be contained in classes instead of being handled by lose
# functions. Such is the hobo way. I mean the Pyramid way. More than likely that
# stems from it being the Python way.

# Another thing to consider is that I don't want to write boiler plate HTML for
# every single template. There should be ways to combine templates together to
# create what the user sees.

# Let's start by thinking about what to call the landing page that users will
# see when they look at a list of forums.

# There will need to be a specific home view that gathers together all of the
# forums that do not have parents. These are the root forums and are the top
# level of all forums. This would be a good display to show for someone who is
# just coming onto the website.

# Since this is the category class, we know that all of the possible uses of
# this class are going to involve using the landing template. Since the landing
# template already includes the base template, we don't have to worry about it.
@view_defaults(renderer='sins:templates/landing.mako')
class CategoryViews:
	def __init__(self, request):
		self.request = request
	
	# We know that the home route will be directed to a top level landing page
	# that will have a listing of all root forums.
	@view_config(route_name='home')
	def home(self):
		# Get all of the forums from the database that do not have a parent id.
		forums = ForumRecordService.by_parent(None)
		
		# return the landing page populated with those forums.
		return {'forums': forums, 'title_message': "Welcome!", 'topics': None}
	
	# I am removing the retrieve forums method from this class. Now that there
	# are service classes the view classes should call upon those classes
	# instead of querying the database themselves.

# I have decided to put the actions in a seperate class so I don't have to
# repeat myself several times.

# Time to start doing the CRUD actions. The reason I am using the term CRUD
# instead of BREAD is because I really only see how to use four RESTful API
# methods, and not five. There should be a one to one correspondence I feel
# between those things for the sake of clarity.

# I will need to determine if the old renderer should be overwritten or
# rather reworked so that an option can be used to view an edit forum on the
# render page
@view_config(route_name='forum_action')
class CategoryActions:
	def __init__(self, request):
		self.request = request
	
	# Create.
	# This is where WTForms start coming into play.
	@view_config(match_param='action=create',
		renderer='sins:templates/edit_forum.mako')
	def create_forum(self):
		# Make sure to populate the choices field of the parent_id SelectField.
		
		return {}
	
	# Read.
	
	# Update.
	@view_config(match_param='action=edit',
		renderer='sins:templates/edit_forum.mako')
	def edit_forum(self):
		return {}
	
	# Delete.