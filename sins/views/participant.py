from pyramid.view import view_config
from pyramid.view import view_defaults
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..models.meta import DBSession
from ..models.user import User
from ..models.services.user import UserRecordService
from ..models.services.post import PostRecordService

""" Participant 

Classes:
* ParticipantViews
** This class provides various views related to users.

* UserEditActions
** This class allows users to register and edit their profiles

* BanEditActions
** This class lets management with the power to do so ban users and edit bans.

"""

##############################
 #     #                                                                                                                                                                         
 ##   ## #  ####   ####  ###### #        ##   #    # #  ####  #    #  ####     #####    ##   #####  ##### #  ####  # #####    ##   #    # #####    #    # # ###### #    #  ####  
 # # # # # #      #    # #      #       #  #  ##   # # #    # #    # #         #    #  #  #  #    #   #   # #    # # #    #  #  #  ##   #   #      #    # # #      #    # #      
 #  #  # #  ####  #      #####  #      #    # # #  # # #    # #    #  ####     #    # #    # #    #   #   # #      # #    # #    # # #  #   #      #    # # #####  #    #  ####  
 #     # #      # #      #      #      ###### #  # # # #    # #    #      #    #####  ###### #####    #   # #      # #####  ###### #  # #   #      #    # # #      # ## #      # 
 #     # # #    # #    # #      #      #    # #   ## # #    # #    # #    #    #      #    # #   #    #   # #    # # #      #    # #   ##   #       #  #  # #      ##  ## #    # 
 #     # #  ####   ####  ###### ###### #    # #    # #  ####   ####   ####     #      #    # #    #   #   #  ####  # #      #    # #    #   #        ##   # ###### #    #  ####  
##############################

# I have chosen to include authentification/authorization views in the
# participant file. The reason I have chosen to do this is that it relates
# directly to users.
class ParticipantViews(ViewBase):
	""" This view class provides various user related views. """
	
	# Show the participant's profile
	@view_config(route_name='user', renderer='sins:templates/profile.mako')
	def profile(self):
		""" This view function allows us to see user profiles. """
		# Search the database for a user whose id matches the user_id passed
		# through the URI.
		user_id = int(sef.request.matchdict.get('user_id', -1))
		user = UserRecordService.by_id(user_id) # Get the id from the URI.
		
		if user:
			# Don't forget that in order for pagination to work we need to
			# specify what page we want.
			paginated_posts = # Get paginated posts that were made by this user.
			return {'user': user, 'posts': paginated_posts}
		else:
			return HTTPNotFound()
	
	# Let the participant log in and out.
	@view_config(
		route_name='auth',
		match_param='action=in',
		renderer='sins:templates/log.mako',
		request_method='POST'
	)
	@view_config(
		route_name='auth',
		match_param='action=out',
		renderer='sins:templates/log.mako'
	)
	def sign_in_out(self):
		""" This function is used for the user to sign in and out. """
		# Make sure to pass a sign out message if the user is logging out.
		# The other thing to do is to pass what whether the user is logging in
		# or out so that there can be a sensible title like "success" or
		# "log in"
		return {}
	
	# This view is for when a user becomes a member of a group.
	@view_config(
		route_name='membership_action',
		match_param='action=create',
		renderer='sins:templates/promotion.mako'
	)
	def promote(self):
		""" This function is used to add the user to a group. """
		entry = Membership()
		form = MembershipCreateForm()
		user_id = self.request.matchdict.get('parent_id')
		
		if user_id:
			if self.request.method = 'POST' and form.validate:
				form_populate.populate_obj(entry)
				
				# From the form url, set the user_id of the new entry.
				entry.user_id = user_id

				# The user_id is a required field.
				# The database should only be updated if there was a user_id
				DBSession.add(entry)
				return HTTPFound(loaction=self.request.route_url(
						'user',
						user_id=user_id
					)
				)
			else:
				# Populate the choices for the group field.
				# Step 1: Get all of the groups.
				groups = GroupRecordService.all()
				
				# Step 2: Create a properly scoped list.
				choices = list()
				
				# Step 3: Populate the choices list.
				for group in groups:
					choice = (group.group_id, group.title)
					choices.append(choice)
				
				# Step 4: Set the choices list as the choices for the group id
				# in the form.
				form.group_id.choices = choices
				
				return {'form': form, 'action': self.request.matchdict('action')}
		else:
			return HTTPNotFound()

##############################
 #     #                         #######                   #     #                        
 #     #  ####  ###### #####     #       #####  # #####    #     # # ###### #    #  ####  
 #     # #      #      #    #    #       #    # #   #      #     # # #      #    # #      
 #     #  ####  #####  #    #    #####   #    # #   #      #     # # #####  #    #  ####  
 #     #      # #      #####     #       #    # #   #       #   #  # #      # ## #      # 
 #     # #    # #      #   #     #       #    # #   #        # #   # #      ##  ## #    # 
  #####   ####  ###### #    #    ####### #####  #   #         #    # ###### #    #  ####  
##############################

@view_defaults(route_name='user_action', renderer='edit_user.mako')
class UserEditActions(ViewBase):
	""" This class provides a way to create and edit users. """
	
	@view_config(match_param='action=create')
	def create_user(self):
		""" This view function allows users to register. """
		entry = User()
		form = UserCreateForm(self.request.POST)
		
		if self.request.method = 'POST' and form.validate:
			form_populate.populate_obj(entry)
			DBSession.add(entry)
			
			# Send the user to their new profile.
			return HTTPFound(location=self.request.route_url(
					'user',
					user_id=entry.user_id,
					slug=entry.slug()
				)
			)
		else:
			return {
				'form': form,
				'action': request.matchdict.get('action'),
			}
	
	@view_config(match_param='action=edit')
	def edit_user(self):
		""" This function allows users to update their profiles. """
		user_id = int(request.params.get('forum_id', -1))
		entry = UserRecordService.by_id(user_id)
		if entry:
			form = UserUpdateForm(self.request.POST, entry)
			if request.method == 'POST' and form.validate():
				form.populate_obj(entry)
				return HTTPFound(location=request.route_url(
						'user',
						user_id=entry.user_id,
						slug=entry.slug()
					)
				)
			else:
				return {
					'form': form,
					'action': self.request.matchdict('action')
				}
		else:
			return HTTPNotFound()

##############################
 ######                      #                                        
 #     #   ##   #    #      # #    ####  ##### #  ####  #    #  ####  
 #     #  #  #  ##   #     #   #  #    #   #   # #    # ##   # #      
 ######  #    # # #  #    #     # #        #   # #    # # #  #  ####  
 #     # ###### #  # #    ####### #        #   # #    # #  # #      # 
 #     # #    # #   ##    #     # #    #   #   # #    # #   ## #    # 
 ######  #    # #    #    #     #  ####    #   #  ####  #    #  ####  
##############################

@view_defaults(
	route_name='ban_action',
	renderer='sins:templates/ban_hammer.mako'
)
class BanEditActions(ViewBase):
	""" This class allows us to ban and edit the bans of a user. """
	
	@view_config(
		route_name='ban_action',
		match_param='action=create',
		renderer='sins:templates/ban_hammer.mako'
	)
	def ban(self):
		""" This restricts a user's access to the community. """
		entry = Ban()
		form = BanCreateForm()
		
		if self.request.method = 'POST' and form.validate:
			forum_populate.populate_obj(entry)
			user_id = self.request.matchdict.get('user_id')
			entry.user_id = user_id
			DBSession.add(entry)
			return HTTPFound(location=self.request.route_url(
					'user', 
					user_id=user_id
					slug=entry.user.slug()
				)
			)
		else:
			return {'form': form, 'action': request.matchdict,get('action')}
	
	def edit_ban(self):
		""" If there has been a mistake a ban can be changed. """
		ban_id = int(request.params.get('forum_id', -1))
		entry = BanRecordService.by_id(ban_id)
		if entry:
			form = BanUpdateForm(request.POST, entry)
			if request.method == 'POST' and form.validate():
				form.populate_obj(entry)
				return HTTPFound(location=request.route_url(
						'user',
						user_id=entry.user_id,
						slug=entry.user.slug()
					)
				)

# EOF
