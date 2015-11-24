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

# We have service classes with functions that need to be tested.
# There is one service class for every model. All service models have the
# the following two methods:
#	all
#	by_id

# All of this will need to be reviewed.
# I think it is safe to say that testing by route would be a safe way to go.
# It might be worth it just to clear all of this out and start over.
class SinsFunctionalTests(unittest.TestCase):
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