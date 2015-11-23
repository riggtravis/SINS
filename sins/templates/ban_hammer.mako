<!-- Step one. Import the base template. -->
<%inherit file="base.mako"/>

<!-- Step two. Set the title. -->
<%block name="title">
  Ban ${user.username}
</%block>

<!-- Step three. Present the user with an obvious header for their action. -->
<h1>Ban ${user.username}</h1>
<p>
	You are about to use the great and mighty ban hammer, mjolnir, to ban
	${user.username}. Remember the inscription on the ban hammer:
	
	<blockquote>
		Whosoever holds this hammer, if he be worthy, shall possess the power of ...
		a moderator!
	</blockquote>
</p>

<form 
	action="${request.route_url('ban_action', action=action, user_id=user.user_id)}" 
	method="post" 
	class="form"
>
	% for error in form.end_date.errors:
			<div class="error">
				${error}
			</div>
	% endfor
	
	<div class="form-group">
		<label for="end_date">${form.end_date.label}</label>
		${form.end_date(class_='form-control')}
	</div>
	
	<div class="form-group">
		<label>submit</label>
		<button type="submit" class="btn btn-default">submit</button>
	</div>
</form>