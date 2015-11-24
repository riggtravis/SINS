import unittest
import transaction

from pyramid import testing

from .models import DBSession

# I'm not clear on how this testing suite works. I'll have to either learn it or
# convert this whole thing to nose tests

# I think this class is no longer needed.


 #     #                                                     
 #     # # ###### #    #    ##### ######  ####  #####  ####  
 #     # # #      #    #      #   #      #        #   #      
 #     # # #####  #    #      #   #####   ####    #    ####  
  #   #  # #      # ## #      #   #           #   #        # 
   # #   # #      ##  ##      #   #      #    #   #   #    # 
    #    # ###### #    #      #   ######  ####    #    ####  
class SinsViewTests(unittest.TestCase):
	""" These tests are used to test the functions contained in views. """
	def setUp(self):
		""" This function gets the test suite ready. """
		self.config = testing.setUp()
		
	def tearDown(self):
		""" This cleans all of the things that were done for testing. """
		testing.tearDown()
		
	# Here is the list of view files:
	
	# category
	#	CategoryViews
	#		home
	#		view_category
	#	CategoryEditActions
	#		create_forum
	#		edit_forum
	
	# discussion
	#	DiscussionViews
	#		view_discussion
	#	TopicEditActions
	#		create_topic
	#		edit_topic
	#	PostActions
	#		create_post
	#		edit_post
	
	# management
	#	ManagementViews
	#		view_management
	#	ManagementActions
	#		create_group
	#		edit_group
	#	PermissionActions
	#		create_permission
	
	# participant
	#	ParticipantViews
	#		profile
	#		sign_in_out
	#		promote
	#	BanActions
	#		ban
	#		edit_ban
	#	UserEditActions
	#		create_user
	#		edit_user
	
	# view_base
	#	ViewBase
	#		__init__


  #####                                  #######                            
 #     #  ####  #####  # #####  #####       #    ######  ####  #####  ####  
 #       #    # #    # # #    #   #         #    #      #        #   #      
  #####  #      #    # # #    #   #         #    #####   ####    #    ####  
       # #      #####  # #####    #         #    #           #   #        # 
 #     # #    # #   #  # #        #         #    #      #    #   #   #    # 
  #####   ####  #    # # #        #         #    ######  ####    #    ####  
class SinsScriptTests(unittest.TestCase):
	""" This class tests the scripts that help prepare SINS. """
	
	def setUp(self):
		""" This function prepares the class to perform tests. """
		self.config = testing.setUp()
	
	def tearDown(self):
		""" This function cleans up anything that can interfere with tests. """
		testing.tearDown()
	
	# There are two scripts that need to be tested in initializedb:
	#	usage
	#	main


 #     #                                #######                            
 ##   ##  ####  #####  ###### #            #    ######  ####  #####  ####  
 # # # # #    # #    # #      #            #    #      #        #   #      
 #  #  # #    # #    # #####  #            #    #####   ####    #    ####  
 #     # #    # #    # #      #            #    #           #   #        # 
 #     # #    # #    # #      #            #    #      #    #   #   #    # 
 #     #  ####  #####  ###### ######       #    ######  ####    #    ####  
class SinsModelTests(unittest.TestCase):
	""" This class tests the models SINS depends on. """
	
	def setUp(self):
		""" This function prepares the class for testing. """
		self.config = testing.setUp()
	
	def tearDown(self):
		""" This function cleans up anything that can interfere with tests. """
		testing.tearDown()
	
	# There are several models but not all of them have functions. This may
	# change so it is worth listing all of the models.
	
	#	ban
	#		start_in_words
	#		end_in_words
	
	#	forum
	#		slug
	
	#	group
	#		slug
	
	#	membership
	
	#	permission
	
	#	post
	#		posted_in_words
	
	#	power
	#		slug
	
	#	topic
	#		start_in_words
	#		slug
	
	#	user
	#		joined_in_words
	#		slug


  #####                                          #######                            
 #     # ###### #####  #    # #  ####  ######       #    ######  ####  #####  ####  
 #       #      #    # #    # # #    # #            #    #      #        #   #      
  #####  #####  #    # #    # # #      #####        #    #####   ####    #    ####  
       # #      #####  #    # # #      #            #    #           #   #        # 
 #     # #      #   #   #  #  # #    # #            #    #      #    #   #   #    # 
  #####  ###### #    #   ##   #  ####  ######       #    ######  ####    #    ####  

# We have service classes with functions that need to be tested. There is one
# service class for every model. Not all of these service classes are fully
# fleched out yet, but they should still be listed for when they grow.
class SinsServiceTests(unittest.TestCase):
	""" This class tests our model services. """
	
	def setUp(self):
		""" This function prepares the class for testing. """
		self.config = testing.setUp()
	
	def tearDown(self):
		""" This test cleans up for future testing. """
		testing.tearDown()
	
	# ban
	#	all
	#	by_id
	#	get_paginator
	#		get_paginator has a sub-function. I'm not sure this can be tested.
	
	# forum
	#	all
	#	by_id
	#	by_parent
	
	# group
	#	all
	#	by_id
	
	# membership
	
	# permission
	
	# post
	#	all
	#	by_id
	#	get_paginator
	
	# power
	#	all
	#	by_id
	
	# topic
	#	all
	#	by_id
	#	get_paginator
	
	# user
	#	by_id

 #######                                                             #######                            
 #       #    # #    #  ####  ##### #  ####  #    #   ##   #            #    ######  ####  #####  ####  
 #       #    # ##   # #    #   #   # #    # ##   #  #  #  #            #    #      #        #   #      
 #####   #    # # #  # #        #   # #    # # #  # #    # #            #    #####   ####    #    ####  
 #       #    # #  # # #        #   # #    # #  # # ###### #            #    #           #   #        # 
 #       #    # #   ## #    #   #   # #    # #   ## #    # #            #    #      #    #   #   #    # 
 #        ####  #    #  ####    #   #  ####  #    # #    # ######       #    ######  ####    #    ####  

# All of this will need to be reviewed.
# I think it is safe to say that testing by route would be a safe way to go.
# It might be worth it just to clear all of this out and start over.
class SinsFunctionalTests(unittest.TestCase):
	""" This class creates a test app and then performs tests on it. """
	
	# home
	
	# user_action
	#	create_user
	#	edit_user
	#		valid user
	#		invalid user
	
	# user
	#	valid user
	#	invalid user
	
	# auth
	#	in
	#	out
	
	# ban_action
	#	create ban
	#		valid user
	#		invalid user
	#	edit_ban
	#		valid user
	#		invalid user
	
	# ban
	#	valid ban
	#	invalid ban
	
	# forum_action
	#	create forum
	#	edit forum
	#		valid forum
	#		invalid forum
	
	# forum
	#	valid forum
	#	invalid forum
	
	# group_action
	#	create group
	#	edit group
	#		valid group
	#		invalid group
	
	# membership_action
	#	create
	# membership
	#	valid user/group combo
	#	invalid user/group combo
	
	# For the test list I am assuming that I am not creating power actions
	# within the app.
	
	# power
	#	valid power
	#	invalid power
	
	# permission action
	#	create
	# permission
	#	valid user/group combo
	#	invalid user/group combo
	
	# post action
	#	create
	#		valid topic
	#		invalid topic
	#	edit
	#		valid post
	#		invalid post
	
	# topic action
	#	create
	#		valid forum
	#		invalid forum
	#	edit
	#		valid topic
	#		invalid topic

# This if conditional allows the tests to be ran from the command line.
if __name__ = "__main__":
	unittest.main()