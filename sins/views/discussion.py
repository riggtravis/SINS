# Before I start work on the next portion of learning, I should probably make
# sure I have a basic frame for what the discussion class(es) look like.
from pyramid.view import view_config
from pyramid.view import view_defaults
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from .view_base import ViewBase
from ..models.meta import DBSession
from ..models.topic import Topic
from ..models.services.topic import TopicRecordService

########
 ######                                                          #     #                        
 #     # #  ####   ####  #    #  ####   ####  #  ####  #    #    #     # # ###### #    #  ####  
 #     # # #      #    # #    # #      #      # #    # ##   #    #     # # #      #    # #      
 #     # #  ####  #      #    #  ####   ####  # #    # # #  #    #     # # #####  #    #  ####  
 #     # #      # #      #    #      #      # # #    # #  # #     #   #  # #      # ## #      # 
 #     # # #    # #    # #    # #    # #    # # #    # #   ##      # #   # #      ##  ## #    # 
 ######  #  ####   ####   ####   ####   ####  #  ####  #    #       #    # ###### #    #  ####  
########

# Because many classes have this code:
#
#	def __init__(self, request):
#		self.request = request
#
# there's probably an object oriented method of maintaining a don't repeat
# yourself mentality.
@view_defaults(route_name='topic', renderer='sins:templates/thread.mako')
class DiscussionViews(ViewBase):
	"""docstring"""
	
	# Show the conversation
	def view_discussion(self):
		"""docstring"""
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

#########
 #######                           #######                      #                                        
    #     ####  #####  #  ####     #       #####  # #####      # #    ####  ##### #  ####  #    #  ####  
    #    #    # #    # # #    #    #       #    # #   #       #   #  #    #   #   # #    # ##   # #      
    #    #    # #    # # #         #####   #    # #   #      #     # #        #   # #    # # #  #  ####  
    #    #    # #####  # #         #       #    # #   #      ####### #        #   # #    # #  # #      # 
    #    #    # #      # #    #    #       #    # #   #      #     # #    #   #   # #    # #   ## #    # 
    #     ####  #      #  ####     ####### #####  #   #      #     #  ####    #   #  ####  #    #  ####   
#########
@view_defaults(route_name='topic_action', renderer='sins:templates/edit_topic')
class TopicEditActions(ViewBase):
	"""docstring"""
	@view_config(match_param='action=create')
	def create_topic(self):
		"""docstring"""
		entry = Topic()
		form = TopicCreateForm(request.POST)
		
		# Get the forum where the topic was to be created.
		forum_id = request.matchdict.get('forum_id')
		
		# If there is a forum_id we can continue
		if forum_id:
			if self.request.method = 'POST' and form.validate:
				form_populate.populate_obj(entry)
				DBSession.add(entry)
				return HTTPFound(location=self.request.route_url(
						'forum',
						forum_id=forum_id
					)
				)
			else:
				# Get the forum itself from the database.
				forum = ForumRecordService.by_id(forum_id)
				
				return {
					'form': form,
					'action': request.matchdict.get('action'),
					'forum': forum
				}
		else:
			return HTTPNotFound()
	
	@view_config(match_param='action=edit')
	def edit_topic(self):
		"""docstring"""
		topic_id = int(request.params.get('forum_id', -1))
		entry = TopicRecordService.by_id(forum_id)
		if entry:
			form = ForumUpdateForm(request.POST, entry)
			if self.request.method == 'POST' and form.validate:
				form.populate_obj(entry)
				return HTTPFound(location=self.request.route_url(
					'topic',
					topic_id=entry.topic_id,
					slug=entry.slug()
				))
			else:
				# Users who are members of groups with the power to do so should be
				# able to move topics to a better forum.
				
				# For right now just let anyone with the ability to edit the topic
				# move the topic.
				
				# I hate doing this, but I think every forum in the community should
				# be a choice.
				forums = ForumRecordService.all()
				choices = list()
				for forum in forums:
					choice = (forum.forum_id, forum.title)
					choices.append(choice)
				
				forum.forum_id.choices = choices
				
				return {
					'form': form,
					'action': self.request.matchdict('action'),
					'forum': entry.forum
				}
		
		else:
			return HTTPNotFound()
########
 ######                            #                                        
 #     #  ####   ####  #####      # #    ####  ##### #  ####  #    #  ####  
 #     # #    # #        #       #   #  #    #   #   # #    # ##   # #      
 ######  #    #  ####    #      #     # #        #   # #    # # #  #  ####  
 #       #    #      #   #      ####### #        #   # #    # #  # #      # 
 #       #    # #    #   #      #     # #    #   #   # #    # #   ## #    # 
 #        ####   ####    #      #     #  ####    #   #  ####  #    #  ####  
########
# Because posts will mostly be seen in the discussion view, I think it makes
# sense to have their actions included here with the other discussion views.
@view_defaults(
	route_name='post_action',
	renderer='sins:templates/edit_post.mako'
)
class PostActions(ViewBase):
	"""docstring"""
	# Create.
	@view_config(
		match_param='action=create'
	)
	def create_post(self):
		"""docstring"""
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
	
	@view_config(
		match_param='action=edit'
	)
	def edit_post(self):
		"""docstring"""
		post_id = int(request.params.get('forum_id', -1))
		entry = PostRecordService.by_id(post_id)
		if entry:
			# I am using entry.topic multiple times.
			topic = entry.topic
			
			form = ForumUpdateForm(self.request.POST, entry)
			if self.request.method == 'POST' and form.validate():
				form.populate_obj(entry)
				return HTTPFound(location=self.request.route_url(
						'topic',
						topic_id=topic.topic_id,
						slug=topic.slug()
					)
				)
			else:
				return {
					'form': form,
					'action': self.request.matchdict('action'), 
					'topic': topic
				}
		else:
			return HTTPNotFound()