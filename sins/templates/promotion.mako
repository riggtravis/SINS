<!-- Step one. Import the base template -->
<%inherit file="base.mako"/>

<!-- Step two. Set the title. -->
<%block name="title">
  Grant ${user.username} power
</%block>

<!-- Step three. Present the user with an obvious header for their action -->
<h1>Grant ${user.username} power</h1>

<p>
	With the mighty power that I weild, I hereby grant ${user.username} with all
	of the powers that are given to...
</p>

<form 
	action="${request.route_url('membership_action', action=action)}"
	method="post"
	class="form"
>
	% for error in form.group_id.errors:
			<div class="error">
				${error}
			</div>
	% endfor
	
	<!-- Use a dropdown to determine which group the user is being added to. -->
	<div class="form-group">
		<label for="group_id">${form.group_id.label}</label>
		${form.group_id(class_='form-control')}
	</div>
	
	<div class="form-group">
		<label>submit</label>
		<button type="submit" class="btn btn-default">amen</button>
	</div>
</form>