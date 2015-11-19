# The basic view that a user will be greated with when first landing on a SINS
# based forum will be a list of all the different discussion categories that are
# available. Therefor the root (home) view will be held here in the category
# view controller.

from pyramid.view import view_config
from pyramid.view import view_defaults

# We're going to want to be able to use our services. Specifically in this view
# file we want to use the forum service.
from ..models.services.forum import ForumRecordService

# We need our forms.
from ..forms import ForumCreateForm, ForumUpdateForm

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
	
	# I need a function for viewing a forum instead of the forum index.
	@view_config(rout_name='forum')
	def view_category(self):
		forum_id = int(self.request.matchdict.get('forum_id', -1))
		forum = ForumRecordService.by_id(forum_id)
		
		if forum:
			return {
				'forums': forum.forums,
				'title_message': forum.title,
				'topics': forum.topics
			}
		else:
			return HTTPNotFound()
	
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
@view_defaults(route_name='forum_action')
class CategoryActions:
	def __init__(self, request):
		self.request = request
	
	# Create.
	# This is where WTForms start coming into play.
	@view_config(
		match_param='action=create',
		renderer='sins:templates/edit_forum.mako'
	)
	def create_forum(self):
		# I'm not sure that calling this variable entry is the most sensible
		entry = Forum()
		form = ForumCreateForm()
		
		# Make sure to populate the choices field of the parent_id SelectField.
		
		# The thing I need to figure out is how to get the context that the
		# request was made from.
		
		if self.request.method = 'POST' and form.validate:
			form_populate.populate_obj(entry)
			
			# From the form url, set the parent_id of the new entry
			entry.parent_id = self.request.matchdict.get('parent_id')
			
			DBSession.add(entry)
			
			# Change this so it returns to its original context.
			if parent_id:
				return HTTPFound(location=self.request.route_url(
						'forum', 
						forum_id=parent_id
					)
				)
			else:
				return HTTPFound(location=self.request.route_url('home'))
		else:
			return {'form': form, 'action': request.matchdict.get('action')}
	
	# Update.
	@view_config(
		match_param='action=edit',
		renderer='sins:templates/edit_forum.mako'
	)
	def edit_forum(self):
		# I need to figure out how in the hell this works.
		forum_id = int(request.params.get('forum_id', -1))
		
		entry = ForumRecordService.by_id(forum_id)
		if entry:
			form = ForumUpdateForm(request.POST, entry)
			
			# If I could do all of this using a switch statement somehow, that
			# would be great.
			
			# Before checking to see if the forum has been set up, populate the
			# parent option. This should be possible by asking for the parent of
			# the forum we're editing's parent. If this does not exist, offer
			# all of the top level categories.
			
			# Because there are multiple situations in which all of the forums
			# without parents will be needed, it will be easier to write the
			# code to do that outside of the branching if then else logic. This
			# will be slower, but I am willing to sacrifice speed for more
			# concise code.
			
			# I picked the name jotnar because that is the norsk word for the
			# ice giants to whome all other norse entities in some way or 
			# another originate from. I picked a norsk word because I have norse
			# horses dammit.
			jotnar = ForumRecordService.by_parent(None)
			
			# We will also need to populate a list here, or else populate it
			# later in the if then else branching pattern.
			choices = list()
			
			# jotun is the singular form of jotnar
			for jotun in jotnar:
				choice = (child.forum_id, child.title)
				choices.append(choice)
			
			if entry.parent_id:
				parent = ForumRecordService.by_id(entry.parent_id)
				if parent.parent_id:
					grandparent = ForumRecordService.by_id(parent.parent_id)
					
					# There has to be a more readable way of doing this.
					# 
					# form.parent_id.choices = [
					# 	(choice.forum_id, choice.title) for choice in grandparent.children
					# ]
					#
					
					# Reset the choices list so that it isn't populated with the
					# jotun choices.
					
					choices = list()
					for child in grandparent.children:
						# It will be more readable to have tuples set up before
						# adding tuples to the list. This way we won't have
						# difficult to parse nested parentheses.
						choice = (child.forum_id, child.title)
						choices.append(choice)
					
					form.parent_id.choices = choices
				else:
					form.parent_id.choices = choices
			else:
				form.parent_id.choices = choices
		else:
			return HTTPNotFound()
		
		# This looks odd, but it's the best way to ensure that what the if
		# statement performed is returned correctly. So this statement will only
		# run if the if statement ran, even though it is outside of the if
		# if statement's codeblock.
		return {'form': form, 'action': self.request.matchdict('action')}
	
	# Delete.