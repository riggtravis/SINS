import unittest
import transaction
import datetime

from pyramid import testing

""" Tests
Classes:

* SinsFunctionalTests
** Used to test the entire application.

"""

# Because we do database testing, lets have a function that prepares our
# database for testing.
def _initTestingDB():
	from sqlalchemy import create_engine
	from .models import (
		ban,
		forum,
		group,
		membership,
		meta,
		permission,
		post,
		power,
		topic,
		user
	)
	
	# We will also need to query the database from time to time.
	from .models.services import (
		ban,
		forum,
		group,
		membership,
		permission,
		post,
		power,
		topic,
		user
	)
	
	engine = create_engine('sqlite://')
	meta.Base.metadata.create_all(engine)
	meta.DBSession.configure(bind=engine)
	
	# I don't know what with does. I should find out.
	# So with makes sure that nothing ends up being out of scope in a harmful
	# way. The only changes that should remain after a with block has run are
	# the changes we actually wanted.
	with transaction.manager:
		# Add a chunk of dummy data for every situation we will need. Which will
		# be many. Instead of trying to add every single piece of data possible,
		# instead just create the things we need until our test database has
		# everything it needs.
		
		# Ban service tests need a ban.
		# In order to have a ban we first need a user.
		# The user model class doesn't have a constructor. So instead of doing
		# it under the assumption that using the class as a function will work I
		# will instead set each attribute one at a time.
		dbuser = user.User()
		dbuser.username = "TestUser"
		email = "test@test.tst"
		join_date = datetime.utcnow()
		DBSession.add(dbuser)
		
		# Now add a ban.
		dbban = ban.Ban()
		
		# I don't know for sure that dbuser will have a primary key until it is
		# committed to the database. To be sure, retreive the dbuser entry from
		# the database and then get its primary key.
		dbuser = UserRecordService.by_username(dbuser.username)
		
		dbban.user_id		= dbuser.user_id
		dbban.start_date	= datetime.utcnow()
		dbban.end_date		= dbban.start_date
		dbban.end_date.year	= dbban.end_date.year + 1
		dbban.reason		= "Test reason"
		DBSession.add(dbban)
	

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

# It might be necessary to set up a unit test for the main function of the
# sins package. However, I don't think this will be necessary, as this is
# covered by the functional tests.

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
	
	def test_strip_filter_with_whitespace_string(self):
		from .forms import strip_filter
		
		self.assertEqual(strip_filter(" whitespace "), "whitespace")
	
	def test_strip_filter_with_no_whitespace_string(self):
		from .forms import strip_filter
		
		self.assertEqual(strip_filter(string), "no whitespace")
	
	def test_strip_filter_with_nothing(self):
		from .forms import strip_filter
		
		self.assertEqual(strip_filter(None), None)
		self.assertEqual(strip_filter(""), None)
		self.assertEqual(strip_filter(False), None)
		self.assertEqual(strip_filter(0), None)
		self.assertEqual(strip_filter([]), None)
		self.assertEqual(strip_filter({}), None)
	

class BanCreateTests(unittest.TestCase):
	# I don't know a ton about WTForms' types. This test class will need to be
	# expanded later. It should be fine though because there is no function
	# associated with this class. I will come back to this after looking over
	# how the BanCreateForm is used in real life.
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	

class BanUpdateTests(unittest.TestCase):
	# See BanCreateTests
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	

class ForumCreateTests(unittest.TestCase):
	# See BanCreateTests
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	

class ForumUpdateTests(unittest.TestCase):
	# See BanCreateTests
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	

class GroupCreateTests(unittest.TestCase):
	# See BanCreateTests
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	

class GroupUpdateTests(unittest.TestCase):
	# See BanCreateTests
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	

class MembershipCreateTests(unittest.TestCase):
	# See BanCreateTests
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class PermissionCreateTests(unittest.TestCase):
	# See BanCreateTests
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	

class PostCreateTests(unittest.TestCase):
	# See BanCreateTests
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	

class PostUpdateTests(unittest.TestCase):
	# See BanCreateTests
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	

class TopicCreateTests(unittest.TestCase):
	# See BanCreateTests
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	

class TopicUpdateTests(unittest.TestCase):
	# See BanCreateTests
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class UserCreateTests(unittest.TestCase):
	# See BanCreateTests
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	

class UserUpdateTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	
	def test_validate_image(self):
		# I am not sure what the .data attribute of the field parameter
		# represents. re.sub() appears to do something with regular expressions.
	

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
	
	def test_start_in_words(self):
		from .models.ban import Ban
		
		test_ban = Ban()
		
		# We need to set the start_date attribute.
		test_ban.start_date = datetime.utcnow()
		
		# I'm working too hard. Just check to see if it works by year.
		test_ban.start_date.year = test_ban.start_date.year - 1
		self.assertEqual(test_ban.start_in_words, "about 1 year")
	
	def test_end_in_words(self):
		from .models.ban import Ban
		
		test_ban = Ban()
		test_ban.end_date = datetime.utcnow()
		test_ban.end_date.year = test_ban.end_date.year + 1
		self.assertEqual(test_ban.end_in_words, "about 1 year")
	

class ForumModelTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	
	def test_slug(self):
		from .models.forum import Forum
		
		test_forum = Forum()
		test_forum.title = "Test Title"
		self.assertEqual(test_forum.slug, "Test Title")
	

class GroupModelTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	
	def test_slug(self):
		from .models.group import Group
		
		test_group = Group()
		test_group.title = "Test Title"
		self.assertEqual(test_group.slug, "Test Title")
	

class MembershipModelTests(unittest.TestCase):
	# This class will test to see if certain attributes are behaving as
	# anticipated. For right now I'm not sure of how to do this, so it will be
	# left for later.
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	

class MetaTests(unittest.TestCase):
	# There are two objects that need to be tested. The DBSession and the Base.
	# I'm not sure how to test this though. I'm not even sure if it's necessary
	# because other peopel will have already tested anything we would need to
	# test with these objects and types.
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	

class PermissionModelTests(unittest.TestCase):
	# See MembershipModelTests
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	

class PostModelTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	
	def test_posted_in_words(self):
		from .models.post import Post
		
		test_post = Post()
		test_post.posted_date = datetime.utcnow()
		test_post.posted_date.year = test_post.posted_date.year + 1
		self.assertEqual(test_post.posted_in_words, "about 1 year")
	

class PowerModelTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	
	def test_slug(self):
		from .models.power import Power
		
		test_power = Power()
		test_power.title = "Test Title"
		self.assertEqual(test_power.slug, "Test Title")
	

class TopicModelTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	
	def test_slug(self):
		from .models.topic import Topic
		
		test_topic = Topic()
		test_topic.subject = "Test Subject"
		self.assertEqual(test_topic.slug, "Test Subject")	
	

class UserModelTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	
	def test_joined_in_words(self):
		from .models.user import User
		
		test_user = User()
		test_user.join_date = datetime.utcnow()
		test_user.join_date.year = test_user.join_date.year - 1
		self.assertEqual(test_user.joined_in_words, "about 1 year")
	
	def test_slug(self):
		from .models.user import User
		
		test_user = User()
		test_user.username = "TestUser"
		self.assertEqual(test_user.slug, "TestUser")
	

  #####                                                 #     #                   #######                            
 #     # ###### #####  #    # #  ####  ######  ####     #     # #    # # #####       #    ######  ####  #####  ####  
 #       #      #    # #    # # #    # #      #         #     # ##   # #   #         #    #      #        #   #      
  #####  #####  #    # #    # # #      #####   ####     #     # # #  # #   #         #    #####   ####    #    ####  
       # #      #####  #    # # #      #           #    #     # #  # # #   #         #    #           #   #        # 
 #     # #      #   #   #  #  # #    # #      #    #    #     # #   ## #   #         #    #      #    #   #   #    # 
  #####  ###### #    #   ##   #  ####  ######  ####      #####  #    # #   #         #    ######  ####    #    ####  
class BanServiceTests(unittest.TestCase):
	# In order to test all services I need to have access to the database. I'm
	# not sure for certain how to do this, but I do know that it is covered in
	# at least one of the tutorials that I'm following. For right now I'm Just
	# going to set up a few tests that I will flesh out later.
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	
	def test_all(self):
		from .models.services.ban import BanRecordService
		
		bans = BanRecordService.all()
		
		# We're getting a list. Use list operations.
		
	
	def test_by_id(self):
		from .models.services.ban import BanRecordService
	
	def test_get_paginator(self):
		from .models.services.ban import BanRecordService
		
		# I'm not sure how to test url_maker or even if I can.
	

class ForumServiceTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	
	def test_all(self):
		from .models.services.forum import ForumRecordService
	
	def test_by_id(self):
		from .models.services.forum import ForumRecordService
	
	def test_by_parent(self):
		from .models.services.forum import ForumRecordService
		
	

class GroupServiceTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	
	def test_all(self):
		from .models.services.group import GroupRecordService
	
	def test_by_id(self):
		from .models.services.group import GroupRecordService
	

class MembershipServiceTests(unittest.TestCase):
	# Currently the membership service is empty. This is because all membership
	# access is done through other models.
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	

class PermissionServiceTests(unittest.TestCase):
	# See MembershipServiceTests
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	

class PostServiceTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	
	def test_all(self):
		from .models.services.post import PostRecordService
	
	def test_by_id(self):
		from .models.services.post import PostRecordService
	
	def test_get_paginator(self):
		from .models.services.post import PostRecordService
		
		# I'm not sure how to test url_maker or even if I can.
	

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
	
	def test_all(self):
		from .models.services.topic import TopicRecordService
	
	def test_by_id(self):
		from .models.services.topic import TopicRecordService
	

class UserServiceTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()
	
	def test_all(self):
		from .models.services.user import UserRecordService
	
	def test_by_id(self):
		from .models.services.user import UserRecordService
	

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
	
	# I'm not sure how to test the two functions of this module.
	def test_usage(self):
		from .scripts.initializedb import usage
	
	def test_main(self):
		from .scripts.initializedb import main
	

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
	
	def test_home(self):
		from .views.category import CategoryViews
		
		request		= testing.DummyRequest()
		inst		= CategoryViews(request)
		response	= inst.home()
		self.assertEqual('Welcome!', response['title_message'])
	
	def test_view_category(self):
		# The view category has two different branches. In one branch there is
		# not a valid forum_id so the software returns an HTTPNotFound call. In
		# the other the landing page for a valid forum is returned. Because I
		# need to access the database in order to do this, I don't know
		# *exactly* how to do this.
		
		# So for the branching calls there should definitely be more than one
		# test function. Each one should test a specific branch. As for the
		# database work, I still have to find a solution to that.
	
	def test_category_not_found(self):
		# This is also dependant upon querying the database.
	

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