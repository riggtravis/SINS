<!-- Step one. Fetch the base template. -->
<%inherit file="base.mako"/>

<!-- Step two. Set the title. -->
<%block name="title">
  ${action} topic in ${forum.title}
</%block>

<!-- Step three. Create a human readable heading -->
<h1>${action} topic</h1>

<!-- Step four. Create the form. -->
<form 
	action="${request.route_url('topic_action')}, action=action, forum_id=forum.forum_id" 
	method="post" 
	class="form"
>
	% if action == 'edit'
			${form.topic_id()}
	% endif
	
	% for error in form.subject.errors:
			<div class="error">
				${error}
			</div>
	% endfor
	
	<div class="form-group">
		<label for="subject">${form.subject.label}</label>
		${form.subject(class_='form-control')}
	</div>
	
	<div class="form-group">
		<label>submit</label>
		<button type="submit" class="btn btn-default">submit</button>
	</div>
</form>