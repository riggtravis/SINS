<!-- Step one. Bring in the base view. -->
<%inherit file="base.mako"/>

<!-- Step two. Set the title. -->
<%block name="title">
  ${topic.subject}
</%block>

<!-- Step three. Display the title as a header. -->
<h1>${topic.subject}</h1>

<!-- Step four. Display all the posts. -->
<!-- I will need to decide how I want to lay this out. For right now dump all as
			raw data.
-->
<!-- The other issue to consider is how to gather the user information for each
			post. More than likely this should be easy to do using the backref from
			the user table. But until I am sure of that, this will remain as is.
-->	
<!-- Because of the backref, every post entity should have a user attribute. -->
% for post in topic.posts:
		<h2>${post.user.username}</h2>
		<% image_path = post.user.avatar + ".png" %>
		<img src=${image_path} alt=${post.user.username} />
		<h3>${post.posted_date}</h3>
		<p>
			${post.message}
		</p>
% endfor