<!-- Step one. Fetch the boilerplate html -->
<%inherit file="base.mako"/>

<!-- Step two. Set the title -->
<%block name="title">
  ${group.title}
</%block>

<!-- Step three. Create a nice header that displays the name of the group for
			easy viewing.
-->
<h1>${group.title}</h1>
<!-- I might want to consider including a description of the group -->

<!-- Step four. List all of the users in the group. -->
<!-- This seems like a good place for a media list. -->
<ul class="media-list">
	% for membership in group.memberships:
			<li class="media">
				<div class="media-left">
					<a = href=
						"${request.route_url('user', id=membership.user.user_id, slug=membership.user.user_id)}"
					>
						<img
							src="${request.static_url('sins:static/avatars/%(name)s.png' % topic.user.avatar)}"
							alt="${post.user.username}"
						/>
					</a>
				</div>
				
				<div class="media-body">
					## The user's username should link to their profile as well.
					<a = href=
						"${request.route_url('user', id=membership.user.user_id, slug=membership.user.user_id)}"
					>
						<h4 class="media-heading">${membership.user.username}</h4>
					</a>
					<p>
						${membership.user.bio}
					</p>
				</div>
			</li>
	% endfor
</ul>

<!-- Step five. List all of the powers this group has been granted. -->
<!-- This seems like a good place for a list group. -->
<ul class="list-group">
	% for permission in group.permissions:
			<li class="list-group-item">
				${permission.power.title}
			</li>
	% endfor
</ul>