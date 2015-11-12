# Before I start work on the next portion of learning, I should probably make
# sure I have a basic frame for what the discussion class(es) look like.
from pyramid.view import view_config
from pyramid.view import view_defaults

class DiscussionViews:
	def __init__(self, request):
		self.request = request
	
	# Show the conversation
	@view_config(route_name='topic', renderer='sins:templates/thread.mako')
	def view_discussion(self):
		# Get the information from the URI about which topic we are looking for.
		return{}