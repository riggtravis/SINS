<!-- Step one. Fetch the boilerplate html -->
<%inherit file="base.mako"/>

<!-- Step two. Set the title. -->
<%block name="title">
  Grant power to ${group.title}
</%block>

<!-- Step three. Present the user with an obvious header for their action -->
<h1>Grant power to ${group.title}</h1>

<!-- Step four. Make the form. -->
<form 
	action="${request.route_url('permission_action', action=action)}" 
	method="post" 
	class="form"
>
	% for error in form.power_id.errors:
			<div class="error">
				${error}
			</div>
	% endfor
	
	<div class="form-group">
		<label for="power_id">${form.power_id.label}</label>
		${form.power_id(class_='form-control')}
	</div>
	
	<div class="form-group">
		<label>submit</label>
		<button type="submit" class="btn btn-default">submit</button>
	</div>
</form>