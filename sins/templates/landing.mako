<%inherit file="base.mako"/>

<%block name="title">
  Discussion Categories
</%block>

<!-- From here is the body of the forum landing page. It will need to list all
			of the forums with the same parent forum, or otherwise all forums without
			any parent. Whether or not the forums being displayed have parents should
			be handled by the view logic.
-->

<!-- I will have to figure out how best to display forums. For right now dump
			them as raw data.
-->

% for forum in forums
		## Forum titles should be links to the forums they are titles of.
		## I need to remind myself of how to do links within a Pyramid app.
		<a>${forum.title}</a>
% endfor

<!-- We should also be ready to list all of the topics that might be in a forum
			since we are also handling the landing page of forums with parents, which
			may have topics attached.
-->

<!-- The for loop shouldn't execute at all if there are no topics -->
% for topic in topics
		## Link to the topic referenced. Also think about how to display the user
		## that posted the topic.
		## Also needs to be edited once I remember how to link to something within
		## a pyramid app.
		<a>${topic.title}</a>
% endfor