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
	