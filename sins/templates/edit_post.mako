<!-- Step one. Fetch the base template -->
<%inherit file="base.mako"/>

<!-- Step two. Set the title. -->
<%block name="title">
  ${action} post in ${topic.subject}
</%block>

<!-- Step three. Present the user with an obvious header for their action. -->
<h1>${action} post in ${topic.subject}</h1>

<!-- Think about a way to remind the user of the context they are posting into.
			This could expresss itself in a few different ways. The first is to
			display all of the posts in a topic (which would be the easiest). The
			second would be to display the last post (which would be the second
			easiest). The third is to display a post that the user wants to reply to
			or the most recent post. This is the one that I am the least interested in
			doing. It would be the hardest and would break the paradigm that I am
			trying to get where people have a long discussion instead of a fractal
			mess with users only talking about a specific subdiscussion semi-related
			to the original topic.
-->

<form 
	action="${request.route_url('post_action', action=action, topic_id=topic.topic_id)}" 
	method="post" 
	class="form"
>
	% if action == 'edit'
			## I'm not clear on why this is being treated as a funcion.
			${form.post_id()}
	% endif
	
	% for error in form.message.errors:
			<div class="error">
				${error}
			</div>
	% endfor
	
	<div class="form-group">
		<label for="message">${form.message.label}</label>
		${form.message(class_='form-control')}
	</div>
	
	<div class="form-group">
		<label>submit</label>
		<button type="submit" class="btn btn-default">submit</button>
	</div>
</form>