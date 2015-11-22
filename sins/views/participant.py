from pyramid.view import view_config
from pyramid.view import view_defaults
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..models.meta import DBSession
from ..models.user import User
from ..models.services.user import UserRecordService
from ..models.services.post import PostRecordService

# I have chosen to include authentification/authorization views in the
# participant file. The reason I have chosen to do this is that it relates
# directly to users.
class ParticipantViews:
	def __init__(self, request):
		self.request = request
	
	# Show the participant's profile
	@view_config(route_name='user', renderer='sins:templates/profile.mako')
	def profile(self):
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
		# Make sure to pass a sign out message if the user is logging out.
		# The other thing to do is to pass what whether the user is logging in
		# or out so that there can be a sensible title like "success" or
		# "log in"
		return {}
	
	# I am including the ban view in the participant class because it relates to
	# participants. A ban is not something that affects forums or posts.
	@view_config(
		route_name='ban_action',
		match_param='action=create',
		renderer='sins:templates/ban_hammer.mako'
	)
	def ban(self):
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
				)
			)
		else:
			return {'form': form, 'action': request.matchdict,get('action')}
	
	# This view is for when a user becomes a member of a group.
	@view_config(
		route_name='membership_action',
		match_param='action=create',
		renderer='sins:templates/promotion.mako'
	)
	def promote(self):
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