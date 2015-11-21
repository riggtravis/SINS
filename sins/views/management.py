# This file is representitive of groups in the forums.
from pyramid.view import view_config
from pyramid.view import view_defaults
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..models.meta import DBSession
from ..models.group import Group
from ..models.services.group import GroupRecordService

@view_defaults(renderer='sins:templates/group.mako', route_name='group')
class ManagementViews:
	def __init__(self, request):
		self.request = request
	
	def view_management(self):
		group_id = int(self.request.matchdict.get('forum_id', -1))
		group = GroupRecordService.by_id(group_id)
		
		if group:
			return {'group': group}

@view_defaults(route_name='group_action')
class ManagementActions:
	def __init__(self, request):
		self.request = request
	
	# Create
	@view_config(
		match_param='action=create',
		renderer='sins:templates/edit_group.mako'
	)
	def create_group(self):
		entry = Group()
		form = GroupCreateForm()
		
		if self.request.method = 'POST' and form.validate:
			form_populate.populate_obj(entry)
			DBSession.add(entry)
			return HTTPFound(location=self.request.route_url('home'))
		else:
			return {'form': form: 'action': request.matchdict.get('action')}
	
	# Update.
	@view_config(
		match_param='action=create',
		renderer='sins:templates/edit_group.mako'
	)
	def edit_group(self):
		group_id = int(request.params.get('forum_id', -1))
		entry = GroupRecordService.by_id(group_id)
		if entry:
			group = GroupUpdateForm(request.POST, entry)
		else:
			return HTTPNotFound()
		return {'form': form, 'action': self.request.matchdict('action')}
	
	# Delete

# Add the permission view to this to this file. I have chosen to include the
# permission view with this class because it is something that is given to
# groups. To me this made sense for the seperation of concerns.
@view_defaults(route_name="permission_action")
class PermissionActions:
	def __init__(self, request):
		self.request = request
	
	# Create
	
	# Create for permissions is context dependent upon the group that the view
	# was reached from. This means that we need to get it from the URL
	@view_config(
		match_param='action=create'
		renderer='sins:templates/permission_slip.mako'
	)
	def create_permission(self):
		entry = Permission()
		form = PermissionCreateForm()
		group_id = self.request.matchdict.get('group')
		
		if group_id:
			if self.request.method = 'POST' and form.validate:
				form_populate.populate_obj(entry)
				
				# From the form url, set the group_id of the new entry
				entry.group_id = group_id

				DBSession.add(entry)
				return HTTPFound(location=self.request.route_url(
						'group',
						user_id=user_id
					)
				)
			else:
				return {'form': form, 'action': self.request.matchdict('action')}
		else:
			return HTTPNotFound()