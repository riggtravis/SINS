<!-- Step one. Include the base. -->
<%inherit file="base.mako"/>

<!-- Step two. Modify the title so that it's specific to the user. -->
<%block name="title">
	${user.username}
</%block>

<!-- Step three. Make the body. -->
<h1>${user.username}</h1>
<img src="${request.static_url('sins:static/avatars/%(name)s' % topic.user.avatar)}" alt=${user.username} />

<!-- Step four. List any current bans that are applied to the user -->
<!-- I will need to decide how to display this information on the page. Until
			then I will just leave it as raw data. I think more than likely it will
			probably end up being displayed in a table
-->
<!-- I forgot to bootstrap this. I will have to bootstrap this. -->
<!-- Use a list group for this. -->
<div class="list-group">
	% for ban in user.bans:
			<a 
				href="${request.route_url('ban', ban_id=ban.ban_id)}" 
				class="list-group-item"
			>
				<h4 class="list-group-item-heading">
					${ban.start_date}
					% if end_date:
							${ban.end_date}
					% endif
				</h4>
				
				<p class="list-group-item-text">
					${ban.reason}
				</p>
			</a>
	% endfor
</div>

<!-- Step five. List all of the groups that the user is a member of. -->
<!-- This might take some thinking since a membership is a relational entity.
			However, memberships are backref'd to groups, so it's possible that I will
			be able to get that information directly
-->

<!-- Step six. List the most recent posts by the user. -->
<!-- This will take a little more logic than what is here right now.  -->
<!-- This, much like memberships might be a little more complicated than it
			appears. More than likely it will be fine because of the backref. But I'm
			going to put this off for just right now.
-->
<!-- Posts should link to the topic where they were posted. -->
<!-- This looks like a great place for a list group -->
<!-- I would like to change this so that posts aren't linked directly. Instead I
			would like to link to the topics where the posts were made. I think a way
			to do this would be to use the fact that forums and topics should be
			backreffed to eachother.
-->
<div class="list-group">
% for post in posts:
		<a href="${request.rout_url('post', post_id=post.post_id, slug=post.slug)}" class="list-group-item">
			<h4 class="list-group-item-heading">${post.date}</h4>
			<p class="list${post.topic.title}-group-item-text">
				${post.topic.title}
			</p>
		</a>
% endfor
</div>
