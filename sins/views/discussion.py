# Before I start work on the next portion of learning, I should probably make
# sure I have a basic frame for what the discussion class(es) look like.
from pyramid.view import view_config
from pyramid.view import view_defaults
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from ..models.meta import DBSession
from ..models.topic import Topic
from ..models.services.topic import TopicRecordService

@view_defaults(route_name='topic')
class DiscussionViews:
	def __init__(self, request):
		self.request = request
	
	# Show the conversation
	@view_config(renderer='sins:templates/thread.mako')
	def view_discussion(self):
		# Get the information from the URI about which topic we are looking for.
		# I am not clear on what the -1 in this function does.
		topic_id = int(self.request.matchdict.get('topic_id', -1))
		topic = TopicRecordService.by_id(topic_id)
		
		# I know that this is not the optimal way to do the following operation
		# in terms of speed or interpretation. But this is the most readable way
		# I could think of to write this code.
		if topic:
			return {'topic': topic}
		else:
			return HTTPNotFound()

# Because posts will mostly be seen in the discussion view, I think it makes
# sense to have their actions included here with the other discussion views.
@view_defaults(route_name='post_action')
class PostActions:
	def __init__(self, request):
		self.request = request
	
	# Create.
	@view_config(
		match_param='action=create',
		renderer='sins:templates/edit_post.mako'
	)
	def create_post(self):
		entry = Post()
		form = PostCreateForm(request.POST)
		
		# Get the discussion where the action was initiated
		topic_id = request.matchdict.get('topic_id')
		
		if topic_id:
			if self.request.method = 'POST' and form.validate:
				form_populate.populate_obj(entry)
				DBSession.add(entry)
				
				# Return to the discussion for the post.
				return HTTPFound(location=self.request.route_url(
						'topic',
						topic_id=topic_id
					)
				)
			else:
				# I want to pass the context of the post to make the form better
				topic = TopicRecordService.by_id(topic_id)
				return {
					'form': form, 
					'action': request.matchdict.get('action'),
					'topic': topic
				}
		else:
			return HTTPNotFound()