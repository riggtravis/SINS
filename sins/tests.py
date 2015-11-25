import unittest
import transaction

from pyramid import testing

from .models import DBSession

""" Tests
Classes:

* SinsFunctionalTests
** Used to test the entire application.

"""

# Apparently every test class for unit testing should only test one class that
# needs to have unit tests performed on it. This is going to a semi major
# rearrangment of code. In fact it would be fair to say that the only portion of
# this file that can stay is headings for the packages and the functional
# testing class frame that is already here.


  #####                     #     #                   #######                            
 #     # # #    #  ####     #     # #    # # #####       #    ######  ####  #####  ####  
 #       # ##   # #         #     # ##   # #   #         #    #      #        #   #      
  #####  # # #  #  ####     #     # # #  # #   #         #    #####   ####    #    ####  
       # # #  # #      #    #     # #  # # #   #         #    #           #   #        # 
 #     # # #   ## #    #    #     # #   ## #   #         #    #      #    #   #   #    # 
  #####  # #    #  ####      #####  #    # #   #         #    ######  ####    #    ####  

 #######                         #     #                   #######                            
 #        ####  #####  #    #    #     # #    # # #####       #    ######  ####  #####  ####  
 #       #    # #    # ##  ##    #     # ##   # #   #         #    #      #        #   #      
 #####   #    # #    # # ## #    #     # # #  # #   #         #    #####   ####    #    ####  
 #       #    # #####  #    #    #     # #  # # #   #         #    #           #   #        # 
 #       #    # #   #  #    #    #     # #   ## #   #         #    #      #    #   #   #    # 
 #        ####  #    # #    #     #####  #    # #   #         #    ######  ####    #    ####  
class FormsTests(unittest.TestCase):
	# Normally I wouldn't write the same function over and over again for
	# different classes. Instead I would usually have subclasses. However,
	# because I want my unit tests to be fully self contained, I want to make
	# sure that none of it interferes. So each class will have their own setUp()
	# and tearDown() functions.
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class BanCreateTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class BanUpdateTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class ForumCreateTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class ForumUpdateTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class GroupCreateTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class GroupUpdateTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class MembershipCreateTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class PermissionCreateTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class PostCreateTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class PostUpdateTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class TopicCreateTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class TopicUpdateTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class UserCreateTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class UserUpdateTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

 #     #                                #     #                   #######                            
 ##   ##  ####  #####  ###### #         #     # #    # # #####       #    ######  ####  #####  ####  
 # # # # #    # #    # #      #         #     # ##   # #   #         #    #      #        #   #      
 #  #  # #    # #    # #####  #         #     # # #  # #   #         #    #####   ####    #    ####  
 #     # #    # #    # #      #         #     # #  # # #   #         #    #           #   #        # 
 #     # #    # #    # #      #         #     # #   ## #   #         #    #      #    #   #   #    # 
 #     #  ####  #####  ###### ######     #####  #    # #   #         #    ######  ####    #    ####  

class BanModelTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class ForumModelTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class GroupModelTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class MembershipModelTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class MetaTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class PermissionModelTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class PostModelTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class PowerModelTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class TopicModelTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class UserModelTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

  #####                                                 #     #                   #######                            
 #     # ###### #####  #    # #  ####  ######  ####     #     # #    # # #####       #    ######  ####  #####  ####  
 #       #      #    # #    # # #    # #      #         #     # ##   # #   #         #    #      #        #   #      
  #####  #####  #    # #    # # #      #####   ####     #     # # #  # #   #         #    #####   ####    #    ####  
       # #      #####  #    # # #      #           #    #     # #  # # #   #         #    #           #   #        # 
 #     # #      #   #   #  #  # #    # #      #    #    #     # #   ## #   #         #    #      #    #   #   #    # 
  #####  ###### #    #   ##   #  ####  ######  ####      #####  #    # #   #         #    ######  ####    #    ####  
class BanServiceTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class ForumServiceTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class GroupServiceTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class MembershipServiceTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class PermissionServiceTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class PostServiceTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class PowerServiceTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class TopicServiceTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class UserServiceTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

  #####                                         #     #                   #######                            
 #     #  ####  #####  # #####  #####  ####     #     # #    # # #####       #    ######  ####  #####  ####  
 #       #    # #    # # #    #   #   #         #     # ##   # #   #         #    #      #        #   #      
  #####  #      #    # # #    #   #    ####     #     # # #  # #   #         #    #####   ####    #    ####  
       # #      #####  # #####    #        #    #     # #  # # #   #         #    #           #   #        # 
 #     # #    # #   #  # #        #   #    #    #     # #   ## #   #         #    #      #    #   #   #    # 
  #####   ####  #    # # #        #    ####      #####  #    # #   #         #    ######  ####    #    ####  
class InitializedbTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()


 #     #                           #     #                   #######                            
 #     # # ###### #    #  ####     #     # #    # # #####       #    ######  ####  #####  ####  
 #     # # #      #    # #         #     # ##   # #   #         #    #      #        #   #      
 #     # # #####  #    #  ####     #     # # #  # #   #         #    #####   ####    #    ####  
  #   #  # #      # ## #      #    #     # #  # # #   #         #    #           #   #        # 
   # #   # #      ##  ## #    #    #     # #   ## #   #         #    #      #    #   #   #    # 
    #    # ###### #    #  ####      #####  #    # #   #         #    ######  ####    #    ####  
class CategoryViewsTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class CategoryEditActions(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class DiscussionViewsTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class TopicEditActionsTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class PostEditActionsTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class ManagementViewsTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class ManagementEditActionsTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class PermissionEditActionsTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class ParticipantViewsTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class UserEditActionsTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class BanEditActionsTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class ViewBaseTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

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

# This if conditional allows the tests to be run from the command line.
if __name__ = "__main__":
	unittest.main()