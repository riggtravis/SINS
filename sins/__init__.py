from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models.meta import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_mako')
	
	# Routes
	
	# Basic utilitarian Routs
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
	
	# Routes specific to SINS
	
	# It looks like basic CRUD actions can be devided at the view level and just
	# be routed as a single route instead of creating a route for each CRUD
	# action. This will probably create a cleaner, easier to use application.
	
	# CRUD actions for users.
	config.add_route('user_action', 'user/{action}')
	config.add_route('user', 'user/{user_id:\d+}/{slug}')
	config.add_route('auth', 'sign/{action}')
	
	# CRUD actions for bans
	config.add_route('ban_action', 'ban/{action}')
	config.add_route('ban', 'ban/{ban_id:\d+}')
	
	# CRUD actions for forums
	config.add_route('forum_action', 'forum/{action}')
	config.add_route('forum', 'forum/{forum_id:\d+}/{slug}')
	
	# CRUD actions for groups
	config.add_route('group_action', 'forum/{action}')
	config.add_route('group', 'group/{group_id:\d+}/{slug}')
	
	# CRUD actions for memberships
	config.add_route('membership_action', 'membership/{action}')
	config.add_route('membership', 'membership/{user_id:\d+}/{group_id:\d+}')
	
	# CRUD actions for powers
	config.add_route('power_action', 'permission/{action}')
	config.add_route('power', 'power/{power_id:\d+}/{slug}')
	
	# CRUD actions for permissions
	config.add_route('permission_action', 'permission/{action}')
	config.add_route('permission', 'permission/{power_id:\d+}/{group_id:\d+}')
	
	# CRUD actions for posts
	config.add_route('post_action', 'post/{action}')
	config.add_route('post', 'post/{post_id:\d+}')
	
	# CRUD actions for topics
	config.add_route('topic_action', 'topic/{action}')
	config.add_route('topic', 'topic/{topic_id:\d+}/{slug}')
	
    config.scan()
    return config.make_wsgi_app()