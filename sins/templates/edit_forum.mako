<!-- Step one. Fetch the bolerplate html -->
<%inherit file="base.mako"/>

<!-- Step two. Set the title. -->
<%block name="title">
  ${action} forum
</%block>

<!-- Step three. Present the user with an obvious header for their action. -->
<h1>${action} forum</h1>

<form 
	action="${request.route_url('forum_action', action=action)}" 
	method="post" 
	class="form"
>
	% if action == 'edit'
			${form.id()}
	% endif
	
	% for error in form.title.errors
			<div class="error">
				${error}
			</div>
	% endfor
	
	<!-- Because there is only one field, let's use a button addon -->
	<!-- I couldn't figure out how to use a button addon. -->
	<div class="form-group">
		<label for="title">${form.title.label}</label>
		${form.title(class_='form-control')}
	</div>
	
	<div class="form-group">
		<label>submit</label>
		<button type="submit" class="btn btn-default">submit</button>
	</div>
</form>