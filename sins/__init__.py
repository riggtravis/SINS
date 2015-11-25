from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models.meta import (
    DBSession,
    Base
)

""" SINS package 

Subpackages:
* models
* scripts
* views

Modules:
* forms
* tests

"""
def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
	
	Parameters:
	* global_config	-- Learn more about what global_config does.
	* settings		-- Settings for setting up the application.
	
	Returns:
	A Pyramid WSGI application
	
	"""
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_mako')
	
	##########
	# 
 ######                                    
 #     #  ####  #    # ##### ######  ####  
 #     # #    # #    #   #   #      #      
 ######  #    # #    #   #   #####   ####  
 #   #   #    # #    #   #   #           # 
 #    #  #    # #    #   #   #      #    # 
 #     #  ####   ####    #   ######  ####  
	#
	##########
	
	##########################
 ######                                                                                           ######                                    
 #     #   ##    ####  #  ####     #    # ##### # #      # #####   ##   #####  #   ##   #    #    #     #  ####  #    # ##### ######  ####  
 #     #  #  #  #      # #    #    #    #   #   # #      #   #    #  #  #    # #  #  #  ##   #    #     # #    # #    #   #   #      #      
 ######  #    #  ####  # #         #    #   #   # #      #   #   #    # #    # # #    # # #  #    ######  #    # #    #   #   #####   ####  
 #     # ######      # # #         #    #   #   # #      #   #   ###### #####  # ###### #  # #    #   #   #    # #    #   #   #           # 
 #     # #    # #    # # #    #    #    #   #   # #      #   #   #    # #   #  # #    # #   ##    #    #  #    # #    #   #   #      #    # 
 ######  #    #  ####  #  ####      ####    #   # ###### #   #   #    # #    # # #    # #    #    #     #  ####   ####    #   ######  ####  
	##########################
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
	
	##########################
  #####  ### #     #  #####      #####                                            ######                                    
 #     #  #  ##    # #     #    #     # #####  ######  ####  # ###### #  ####     #     #  ####  #    # ##### ######  ####  
 #        #  # #   # #          #       #    # #      #    # # #      # #    #    #     # #    # #    #   #   #      #      
  #####   #  #  #  #  #####      #####  #    # #####  #      # #####  # #         ######  #    # #    #   #   #####   ####  
       #  #  #   # #       #          # #####  #      #      # #      # #         #   #   #    # #    #   #   #           # 
 #     #  #  #    ## #     #    #     # #      #      #    # # #      # #    #    #    #  #    # #    #   #   #      #    # 
  #####  ### #     #  #####      #####  #      ######  ####  # #      #  ####     #     #  ####   ####    #   ######  ####  
	##########################
	
	# It looks like basic CRUD actions can be devided at the view level and just
	# be routed as a single route instead of creating a route for each CRUD
	# action. This will probably create a cleaner, easier to use application.
	
 #     #                          #####  ######  #     # ######  
 #     #  ####  ###### #####     #     # #     # #     # #     # 
 #     # #      #      #    #    #       #     # #     # #     # 
 #     #  ####  #####  #    #    #       ######  #     # #     # 
 #     #      # #      #####     #       #   #   #     # #     # 
 #     # #    # #      #   #     #     # #    #  #     # #     # 
  #####   ####  ###### #    #     #####  #     #  #####  ######  
	##############################
	config.add_route('user_action', 'user/{action}')
	config.add_route('user', 'user/{user_id:\d+}/{slug}')
	config.add_route('auth', 'sign/{action}')
	
 ######                    #####  ######  #     # ######  
 #     #   ##   #    #    #     # #     # #     # #     # 
 #     #  #  #  ##   #    #       #     # #     # #     # 
 ######  #    # # #  #    #       ######  #     # #     # 
 #     # ###### #  # #    #       #   #   #     # #     # 
 #     # #    # #   ##    #     # #    #  #     # #     # 
 ######  #    # #    #     #####  #     #  #####  ######  
	##############################
	config.add_route('ban_action', 'ban/{action}/{user_id:\d+}')
	config.add_route('ban', 'ban/{ban_id:\d+}')
	
 #######                                 #####  ######  #     # ######  
 #        ####  #####  #    # #    #    #     # #     # #     # #     # 
 #       #    # #    # #    # ##  ##    #       #     # #     # #     # 
 #####   #    # #    # #    # # ## #    #       ######  #     # #     # 
 #       #    # #####  #    # #    #    #       #   #   #     # #     # 
 #       #    # #   #  #    # #    #    #     # #    #  #     # #     # 
 #        ####  #    #  ####  #    #     #####  #     #  #####  ######  
	##############################
	
	# We need to a parameter for the context to use when creating forums.
	config.add_route('forum_action', 'forum/{action}/{forum_id:\d+}')
	config.add_route('forum', 'forum/{forum_id:\d+}/{slug}')
	
  #####                                  #####  ######  #     # ######  
 #     # #####   ####  #    # #####     #     # #     # #     # #     # 
 #       #    # #    # #    # #    #    #       #     # #     # #     # 
 #  #### #    # #    # #    # #    #    #       ######  #     # #     # 
 #     # #####  #    # #    # #####     #       #   #   #     # #     # 
 #     # #   #  #    # #    # #         #     # #    #  #     # #     # 
  #####  #    #  ####   ####  #          #####  #     #  #####  ######  
	##############################
	config.add_route('group_action', 'forum/{action}')
	config.add_route('group', 'group/{group_id:\d+}/{slug}')
	
 #     #                                                               #####  ######  #     # ######  
 ##   ## ###### #    # #####  ###### #####   ####  #    # # #####     #     # #     # #     # #     # 
 # # # # #      ##  ## #    # #      #    # #      #    # # #    #    #       #     # #     # #     # 
 #  #  # #####  # ## # #####  #####  #    #  ####  ###### # #    #    #       ######  #     # #     # 
 #     # #      #    # #    # #      #####       # #    # # #####     #       #   #   #     # #     # 
 #     # #      #    # #    # #      #   #  #    # #    # # #         #     # #    #  #     # #     # 
 #     # ###### #    # #####  ###### #    #  ####  #    # # #          #####  #     #  #####  ######  
	##############################
	config.add_route('membership_action', 'membership/{action}')
	
	# I'm not convinced that the membership route makes sense or that it will be
	# included in the final version of this.
	config.add_route('membership', 'membership/{user_id:\d+}/{group_id:\d+}')
	
 ######                                  #####  ######  #     # ######  
 #     #  ####  #    # ###### #####     #     # #     # #     # #     # 
 #     # #    # #    # #      #    #    #       #     # #     # #     # 
 ######  #    # #    # #####  #    #    #       ######  #     # #     # 
 #       #    # # ## # #      #####     #       #   #   #     # #     # 
 #       #    # ##  ## #      #   #     #     # #    #  #     # #     # 
 #        ####  #    # ###### #    #     #####  #     #  #####  ######  
	##############################
	
	# I don't actually think that I will be using the power_action route because
	# powers are so intertwined with logic. More than likely these will have to
	# be set up in the initialize_sins_db script, and use global constants to
	# determine which power to use. It might even be a good idea to have a
	# powers object that contains as member variables all of the different
	# permission values. This way when a power is used in the code it can be
	# clear which permission it is. It would be a lot easer to have something
	# like BAN_USER instead of just the power number like 8.
	config.add_route('power_action', 'power/{action}')
	config.add_route('power', 'power/{power_id:\d+}/{slug}')
	
 ######                                                           #####  ######  #     # ######  
 #     # ###### #####  #    # #  ####   ####  #  ####  #    #    #     # #     # #     # #     # 
 #     # #      #    # ##  ## # #      #      # #    # ##   #    #       #     # #     # #     # 
 ######  #####  #    # # ## # #  ####   ####  # #    # # #  #    #       ######  #     # #     # 
 #       #      #####  #    # #      #      # # #    # #  # #    #       #   #   #     # #     # 
 #       #      #   #  #    # # #    # #    # # #    # #   ##    #     # #    #  #     # #     # 
 #       ###### #    # #    # #  ####   ####  #  ####  #    #     #####  #     #  #####  ######  
	##############################
	config.add_route('permission_action', 'permission/{action}/')
	config.add_route('permission', 'permission/{power_id:\d+}/{group_id:\d+}')
	
 ######                          #####  ######  #     # ######  
 #     #  ####   ####  #####    #     # #     # #     # #     # 
 #     # #    # #        #      #       #     # #     # #     # 
 ######  #    #  ####    #      #       ######  #     # #     # 
 #       #    #      #   #      #       #   #   #     # #     # 
 #       #    # #    #   #      #     # #    #  #     # #     # 
 #        ####   ####    #       #####  #     #  #####  ######  
	##############################
	
	# Realistically posts shouldn't be linked directly. I need to find a way to
	# safely eliminate this routing method and instead link to the topic where
	# the post was made.
	config.add_route('post_action', 'post/{action}/{topic_id:\d+}')
	config.add_route('post', 'post/{post_id:\d+}/{slug}')
	
 #######                            #####  ######  #     # ######  
    #     ####  #####  #  ####     #     # #     # #     # #     # 
    #    #    # #    # # #    #    #       #     # #     # #     # 
    #    #    # #    # # #         #       ######  #     # #     # 
    #    #    # #####  # #         #       #   #   #     # #     # 
    #    #    # #      # #    #    #     # #    #  #     # #     # 
    #     ####  #      #  ####      #####  #     #  #####  ######  
	##############################
	config.add_route('topic_action', 'topic/{action}/{forum_id:\d+}')
	config.add_route('topic', 'topic/{topic_id:\d+}/{slug}')
	
	###################
	# 
 ######                                                                                        
 #     # #    # #    #    ##### #    # ######     ####  ###### #####  #    # ###### #####      
 #     # #    # ##   #      #   #    # #         #      #      #    # #    # #      #    #     
 ######  #    # # #  #      #   ###### #####      ####  #####  #    # #    # #####  #    #     
 #   #   #    # #  # #      #   #    # #              # #      #####  #    # #      #####
 #    #  #    # #   ##      #   #    # #         #    # #      #   #   #  #  #      #   #
 #     #  ####  #    #      #   #    # ######     ####  ###### #    #   ##   ###### #    #
	#
	###################
	
    config.scan()
    return config.make_wsgi_app()