<!-- Step one. Import the base template -->
<%inherit file="base.mako"/>

<!-- Step two. Set the title. -->
<%block name="title">
  ${action} group
</%block>

<!-- Step three. Present the user with an obvious header for their action -->
<h1>${action} group</h1>

<!-- Step four. Present the user with a form to edit the group. -->
<form 
	action="${request.route_url('group_action', action=action)}" 
	method="post" 
	class="form"
>
	% if action == 'edit'
			${form.forum_id()}
	% endif
	
	% for error in form.title.errors
			<div class="error">
				${error}
			</div>
	% endfor
	
	<div class="form-group">
		<label for="title">${form.title.label}</label>
		${form.title(class_='form-control')}
	</div>
	
	<div class="form-group">
		<label>submit</label>
		<button type="submit" class="btn btn-default">submit</button>
	</div>
</form>