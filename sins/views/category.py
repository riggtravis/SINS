# The basic view that a user will be greated with when first landing on a SINS
# based forum will be a list of all the different discussion categories that are
# available. Therefor the root (home) view will be held here in the category
# view controller.

from pyramid.view import view_config
from pyramid.view import view_defaults

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
		
		# It will be easier to perform testing if instead of trying to do
		# everything at once if there is a get forums function. That way we can
		# test that that function is retrieving records properly as well as test
		# the correctness of the home function.
		
		# return the landing page populated with those forums.
	
	def retrieve_records():