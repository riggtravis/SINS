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
<!-- Let's do a media list -->
<ul class="media-list">
	% for post in topic.posts:
			<li class="media">
				<div class="media-left">
					<a href="user/${post.user.user_id}">
						<img 
							src="${request.static_url('sins:static/avatars/%(name)s' % topic.user.avatar)}"
							alt=${post.user.username}
						/>
					</a>
				</div>
				<div class="media-body">
					<h4 class="media-heading">${post.user.username}</h4>
					<h5 class="media-heading">${post.posted_date}</h5>
					<p>
						${post.message}
					</p>
				</div>
			</li>
	% endfor
</ul>