# The basic view that a user will be greated with when first landing on a SINS
# based forum will be a list of all the different discussion categories that are
# available. Therefor the root (home) view will be held here in the category
# view controller.

from pyramid.view import view_config
from pyramid.view import view_defaults

# We need our view base
from .view_base import ViewBase

# We're going to want to be able to use our services. Specifically in this view
# file we want to use the forum service.
from ..models.services.forum import ForumRecordService

# We need our forms.
from ..forms import ForumCreateForm, ForumUpdateForm

# We need to be able to throw an HTTPNotFound call.
from pyramid.httpexceptions import HTTPNotFound

""" Category 

Classes:

* CategoryViews
** This class provides a way to list categories

* CategoryEditActions
** This class provides methods for creating and editing forums.

"""https://www.python.org/dev/peps/pep-0333/#environ-variables

# Views should be contained in classes instead of being handled by lose
# functions. Such is the hobo way. I mean the Pyramid way. More than likely that
# stems from it being the Python way.

# Another thing to consider is that I don't want to write boiler plate HTML for
# every single template. There should be ways to combine templates together to
# create what the user sees.

########

 #                                               #     #                        
 #         ##   #    # #####  # #    #  ####     #     # # ###### #    #  ####  
 #        #  #  ##   # #    # # ##   # #    #    #     # # #      #    # #      
 #       #    # # #  # #    # # # #  # #         #     # # #####  #    #  ####  
 #       ###### #  # # #    # # #  # # #  ###     #   #  # #      # ## #      # 
 #       #    # #   ## #    # # #   ## #    #      # #   # #      ##  ## #    # 
 ####### #    # #    # #####  # #    #  ####        #    # ###### #    #  ####  

#########
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
class CategoryViews(ViewBase):
	""" This class provides landing pages for forums and SINS. """
	
	# We know that the home route will be directed to a top level landing page
	# that will have a listing of all root forums.
	@view_config(route_name='home')
	def home(self):
		""" This view is in essence the home page. """
		# Get all of the forums from the database that do not have a parent id.
		forums = ForumRecordService.by_parent(None)
		
		# return the landing page populated with those forums.
		return {'forums': forums, 'title_message': 'Welcome!', 'topics': None}
	
	# I need a function for viewing a forum instead of the forum index.
	@view_config(route_name='forum')
	def view_category(self):
		""" This function provides a landing for a specifc forum. """
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

#########

 #######                    #####                                                 
 #       #####  # #####    #     #   ##   ##### ######  ####   ####  #####  #   # 
 #       #    # #   #      #        #  #    #   #      #    # #    # #    #  # #  
 #####   #    # #   #      #       #    #   #   #####  #      #    # #    #   #   
 #       #    # #   #      #       ######   #   #      #  ### #    # #####    #   
 #       #    # #   #      #     # #    #   #   #      #    # #    # #   #    #   
 ####### #####  #   #       #####  #    #   #   ######  ####   ####  #    #   #   

#########
# I have decided to put the actions in a seperate class so I don't have to
# repeat myself several times.

# Time to start doing the CRUD actions. The reason I am using the term CRUD
# instead of BREAD is because I really only see how to use four RESTful API
# methods, and not five. There should be a one to one correspondence I feel
# between those things for the sake of clarity.

# I will need to determine if the old renderer should be overwritten or
# rather reworked so that an option can be used to view an edit forum on the
# render page
@view_defaults(
	route_name='forum_action',
	renderer='sins:templates/edit_forum.mako'
)
class CategoryEditActions(ViewBase):
	""" This class provides views for creating and editing forums. """
	
	# Create.
	# This is where WTForms start coming into play.
	@view_config(match_param='action=create')
	def create_forum(self):
		""" This view is for creating forums. """
		# This function needs to create a dynamic list of potential parents.
		# I'm not sure that calling this variable entry is the most sensible
		entry = Forum()
		form = ForumCreateForm(self.request.POST)
		
		# Get the context the create action was initiated from.
		current_forum = ForumRecordService.by_id(
			request.matchdict.get('current_forum_id')
		)
		
		# This works by checking what the server received from the client. The
		# form.validate statement works because our form might already be
		# populated by request.POST
		if self.request.method = 'POST' and form.validate:
			form_populate.populate_obj(entry)
			DBSession.add(entry)
			
			# This isn't good. The forum should return somewhere it is visible,
			# and one of the possibilities is that the forum will be a child of
			# the context forum. What should instead happen is that the user
			# should be sent to the parent of the new forum if it exists.
			if entry.parent_id:
				return HTTPFound(location=self.request.route_url(
						'forum', 
						forum_id=entry.parent_id,
						# I think we need a slug attribute. We do.
						slug=entry.slug
					)
				)
			# Otherwise the forum is a jotun and should be returned to the home
			# view page.
			else:
				return HTTPFound(location=self.request.route_url('home'))
		else:
			# Populate the choices list with potential forums.
			
			# If there is a current_forum, it should be a potential choice as
			# well as all of its children.
			
			# No matter what happens in this if then else branching statement we
			# will need a list that has a scope outside the branches.
			choices = list()
			if current_forum:
				choices = append((current_forum.forum_id, current_forum.title))
				
				# Add all of the current forum's children to the choices.
				for child in current_forum.children:
					choice = (child.forum_id, child.title)
					choices.append(choice)
			
			# Otherwise the choices should be the jotnar
			else:
				jotnar = ForumRecordService.by_parent(None)
				for jotun in jotnar:
					choice = (jotun.forum_id, jotun.title)
					choices.append(choice)
			
			# Now that we are out of the branching statement, set the choices
			# list as the choices for the parent id in the form.
			form.parent_id.choices = choices
			
			# In case there is an error and the system has to be started again,
			# make sure to pass the current_forum
			return {
				'form': form, 
				'action': request.matchdict.get('action'), # What does this do?
				'current_forum_id': current_forum.forum_id
			}
	
	# Update.
	@view_config(match_param='action=edit')
	def edit_forum(self):
		""" This function view is for editing existing forums. """
		# I have forgotten to include the HTTPFound() call for this function.
		
		# I need to figure out how in the hell this works.
		forum_id = int(request.params.get('forum_id', -1))
		
		# Make sure the form variable is available outside the if branch scope.
		form = None
		
		entry = ForumRecordService.by_id(forum_id)
		if entry:
			# Wait, why is this taking entry as a parameter?
			form = ForumUpdateForm(self.request.POST, entry)
			
			# First check to see if the form has already been filled out.
			# I need to figure out a way to change this to a put for the sake of
			# standards compliance.
			if request.method == 'POST' and form.validate():
				form.populate_obj(entry)
				return HTTPFound(location=request.route_url(
						'forum',
						forum_id=entry.forum_id,
						slug=entry.slug()
					)
				)
			else:	# Do all the other stuff we were already doing.
				# If I could do all of this using a switch statement somehow,
				# that would be great.
				
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
					choice = (jotun.forum_id, jotun.title)
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
						
						# Reset the choices list so that it isn't populated with
						# the jotun choices.
						choices = list()

						for child in grandparent.children:
							# It will be more readable to have tuples set up 
							# before adding tuples to the list. This way we
							# won't have difficult to parse nested parentheses.
							choice = (child.forum_id, child.title)
							choices.append(choice)
						
				# We have form.parent_id.choices = choices repeated three times
				# here and there has to be a better way to do this.			
				form.parent_id.choices = choices
		else:
			return HTTPNotFound()
		
		# This looks odd, but it's the best way to ensure that what the if
		# statement performed is returned correctly. So this statement will only
		# run if the if statement ran, even though it is outside of the if
		# if statement's codeblock.
		return {'form': form, 'action': self.request.matchdict('action')}