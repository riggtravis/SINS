# This file is representitive of groups in the forums.
from pyramid.view import view_config
from pyramid.view import view_defaults
from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from ..models.meta import DBSession
from ..models.group import Group
from ..models.services.group import GroupRecordService

""" Management 

Classes:
* ManagementViews
** This class provides methods for viewing a management group.

* ManagementEditActions
** This class allows the creation and modification of management groups.

* PermissionEditActions
** This class allows powers to be given to to a management group.

"""

# I have not provided for a way to list all groups. Which is probably important.

 #     #                                                                  #     #                        
 ##   ##   ##   #    #   ##    ####  ###### #    # ###### #    # #####    #     # # ###### #    #  ####  
 # # # #  #  #  ##   #  #  #  #    # #      ##  ## #      ##   #   #      #     # # #      #    # #      
 #  #  # #    # # #  # #    # #      #####  # ## # #####  # #  #   #      #     # # #####  #    #  ####  
 #     # ###### #  # # ###### #  ### #      #    # #      #  # #   #       #   #  # #      # ## #      # 
 #     # #    # #   ## #    # #    # #      #    # #      #   ##   #        # #   # #      ##  ## #    # 
 #     # #    # #    # #    #  ####  ###### #    # ###### #    #   #         #    # ###### #    #  ####  
@view_defaults(renderer='sins:templates/group.mako', route_name='group')
class ManagementViews(ViewBase):
	""" This class provides a way to see who manages the community. """

	def view_management(self):
		""" This view function provides a view of a group of users. """
		group_id = int(self.request.matchdict.get('group_id', -1))
		group = GroupRecordService.by_id(group_id)
		
		if group:
			return {'group': group}
		else:
			return HTTPNotFound()
	

 #     #                                                                  #######                      #                                        
 ##   ##   ##   #    #   ##    ####  ###### #    # ###### #    # #####    #       #####  # #####      # #    ####  ##### #  ####  #    #  ####  
 # # # #  #  #  ##   #  #  #  #    # #      ##  ## #      ##   #   #      #       #    # #   #       #   #  #    #   #   # #    # ##   # #      
 #  #  # #    # # #  # #    # #      #####  # ## # #####  # #  #   #      #####   #    # #   #      #     # #        #   # #    # # #  #  ####  
 #     # ###### #  # # ###### #  ### #      #    # #      #  # #   #      #       #    # #   #      ####### #        #   # #    # #  # #      # 
 #     # #    # #   ## #    # #    # #      #    # #      #   ##   #      #       #    # #   #      #     # #    #   #   # #    # #   ## #    # 
 #     # #    # #    # #    #  ####  ###### #    # ###### #    #   #      ####### #####  #   #      #     #  ####    #   #  ####  #    #  ####  

@view_defaults(
	route_name='group_action', 
	renderer='sins:templates/edit_group.mako'
)
class ManagementEditActions(ViewBase):
	""" This class allows groups to be created and edited. """
	
	# Create
	@view_config(
		match_param='action=create',
		renderer='sins:templates/edit_group.mako'
	)
	def create_group(self):
		""" This view provides a way to create a new group. """
		entry = Group()
		form = GroupCreateForm()
		
		if self.request.method = 'POST' and form.validate:
			form_populate.populate_obj(entry)
			DBSession.add(entry)
			
			# Instead of returning how it should go to the newly created group
			# page using the ManagementViews
			return HTTPFound(location=self.request.route_url(
					'group',
					group_id=entry.group_id,
					slug=entry.slug
				)
			)
		else:
			return {'form': form: 'action': request.matchdict.get('action')}
	
	# Update.
	@view_config(
		match_param='action=edit',
		renderer='sins:templates/edit_group.mako'
	)
	def edit_group(self):
		""" This view function allows us to change existing groups. """
		group_id = int(request.params.get('group_id', -1))
		entry = GroupRecordService.by_id(group_id)
		if entry:
			form = GroupUpdateForm(request.POST, entry)
			
			# I need to do that thing where I validate the form.
			if request.method == 'POST' and form.validate():
				form.populate_obj(entry)
				return HTTPFound(location=request.route_url(
						'group',
						group_id=entry.group_id,
						slug=entry.slug()
					)
				)
			
			# The return only runs if the form doesn't validate.
			else:
				return {'form': form, 'action': self.request.matchdict('action')}
		else:
			return HTTPNotFound()
	


 ######                                                          #######                      #                                        
 #     # ###### #####  #    # #  ####   ####  #  ####  #    #    #       #####  # #####      # #    ####  ##### #  ####  #    #  ####  
 #     # #      #    # ##  ## # #      #      # #    # ##   #    #       #    # #   #       #   #  #    #   #   # #    # ##   # #      
 ######  #####  #    # # ## # #  ####   ####  # #    # # #  #    #####   #    # #   #      #     # #        #   # #    # # #  #  ####  
 #       #      #####  #    # #      #      # # #    # #  # #    #       #    # #   #      ####### #        #   # #    # #  # #      # 
 #       #      #   #  #    # # #    # #    # # #    # #   ##    #       #    # #   #      #     # #    #   #   # #    # #   ## #    # 
 #       ###### #    # #    # #  ####   ####  #  ####  #    #    ####### #####  #   #      #     #  ####    #   #  ####  #    #  ####  

# Add the permission view to this to this file. I have chosen to include the
# permission view with this class because it is something that is given to
# groups. To me this made sense for the seperation of concerns.
@view_defaults(
	route_name="permission_action", 
	match_param='action=create',
	renderer='sins:templates/permission_slip.mako'
)
class PermissionEditActions(ViewBase):
	""" This class allows us to give groups powers. """
	
	# Create
	
	# Create for permissions is context dependent upon the group that the view
	# was reached from. This means that we need to get it from the URL
	@view_config(
		
	)
	def create_permission(self):
		""" This view gives us the ability to give a power to a group. """
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
						group_id=group_id
					)
				)
			else:
				# We need a dynamic list of choices for the form.
				# Step 1: get all of the permissions
				powers = PowerRecordService.all()
				
				# Step 2: create a list in the correct scope.
				choices = list()
				
				# Step 3: populate the choices list.
				for power in powers:
					choice = (power.power_id, power.title)
					choices.append(choice)
				
				# Step 4: set the form power_id choices.
				form.power_id.choices = choices
				
				# Get the group from the group id.
				group = GroupRecordService.by_id(group_id)
				
				return {
					'form': form, 
					'action': self.request.matchdict('action'),
					'group': group
				}
		else:
			return HTTPNotFound()