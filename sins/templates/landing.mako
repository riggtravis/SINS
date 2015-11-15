<%inherit file="base.mako"/>

<%block name="title">
  ${title_message}
</%block>

<!-- From here is the body of the forum landing page. It will need to list all
			of the forums with the same parent forum, or otherwise all forums without
			any parent. Whether or not the forums being displayed have parents should
			be handled by the view logic.
-->

<!-- I will have to figure out how best to display forums. For right now dump
			them as raw data. It is entirely possible that the best way to display 
			this information is as a table.
-->
<div class="list-group">
	% for forum in forums:
			## Forum titles should be links to the forums they are titles of.
			## I need to remind myself of how to do links within a Pyramid app.
			<a href=
				"${request.route_url('forum', forum_id=forum.forum_id, slug=forum.slug)}"
				class="list-group-item"
			>
				${forum.title}
			</a>
	% endfor
</div>


<!-- We should also be ready to list all of the topics that might be in a forum
			since we are also handling the landing page of forums with parents, which
			may have topics attached.
-->

<!-- The for loop shouldn't execute at all if there are no topics -->
<!-- There is probably other information that I will want to display as well,
			including who posted the topic, and possibly their avatar.
-->
<!-- Finding a way to display information about the most recent post would be
			really cool.
-->
<!-- This actually seems like a great place for a media list. -->
<ul class="media-list">
	% for topic in topics:
			## Link to the topic referenced. Also think about how to display the user
			## that posted the topic.
			## Also needs to be edited once I remember how to link to something within
			## a pyramid app.
			## Use the original poster's username as a link to their profile.
			<li class="media">
				<div class="media-left">
					<a href=
						"${request.route_url('user', user_id=topic.user.user_id, slug=topic.slug)}"
					>
						<img 
							src="${request.static_url('sins:static/avatars/%(name)s' % topic.user.avatar)}"
							alt=${topic.user.username}
						/>
					</a>
				</div>
				
				<div class="media-body">
					<h4 class="media-heading">
						<a href=
							"${request.route_url('topic', topic_id=topic.topic_id, slug=topic.slug)}"
						>
							${topic.title}
						</a>
					</h4>
					<a href=
						"${request.request_url('user', user_id=topic.user.user_id, slug=topic.user.slug)}"
					>
						${topic.user.username}
					</a>
				</div>
			</li>
	% endfor
</ul>