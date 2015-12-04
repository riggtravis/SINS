import unittest
import transaction
import datetime

from pyramid import testing

""" Tests
Classes:

* SinsFunctionalTests
** Used to test the entire application.

"""


  #####                                         #####                                                        
 #     # #       ####  #####    ##   #         #     #  ####  #    #  ####  #####   ##   #    # #####  ####  
 #       #      #    # #    #  #  #  #         #       #    # ##   # #        #    #  #  ##   #   #   #      
 #  #### #      #    # #####  #    # #         #       #    # # #  #  ####    #   #    # # #  #   #    ####  
 #     # #      #    # #    # ###### #         #       #    # #  # #      #   #   ###### #  # #   #        # 
 #     # #      #    # #    # #    # #         #     # #    # #   ## #    #   #   #    # #   ##   #   #    # 
  #####  ######  ####  #####  #    # ######     #####   ####  #    #  ####    #   #    # #    #   #    ####  

# Because the tests could be started near midnight December 31st, we should get
# the date and time of when the tests were started.
INIT_DATE = datetime.utcnow()

# Because we do database testing, lets have a function that prepares our
# database for testing.
def _initTestingDB():
	from sqlalchemy import create_engine
	import .models
	
	# We will also need to query the database from time to time.
	from .models import services
	
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
		dbuser = models.user.User()
		dbuser.username = "TestUser"
		email = "test@test.tst"
		join_date = INIT_DATE
		DBSession.add(dbuser)
		
		# Before the test suite will be ready, the user will need a password.
		# The reason for this is that the password attribute is non-nullable. In
		# order to do this I will have to brush up on authentification.
		
		# Now add a ban.
		dbban = models.ban.Ban()
		
		# I don't know for sure that dbuser will have a primary key until it is
		# committed to the database. To be sure, retreive the dbuser entry from
		# the database and then get its primary key.
		dbuser = services.user.UserRecordService.by_username(dbuser.username)
		
		dbban.user_id		= dbuser.user_id
		dbban.start_date	= INIT_DATE
		dbban.end_date		= dbban.start_date
		dbban.end_date.year	= dbban.end_date.year + 1
		dbban.reason		= "Test reason"
		DBSession.add(dbban)
		
		# In order to properly test forums we need to have a parent forum.
		parent_forum		= models.forum.Forum()
		parent_forum.title	= "Parent Forum"
		DBSession.add(parent_forum)
		
		# The forum service tests unsurprisingly need a forum in the database.
		dbforum			= models.forum()
		dbforum.title	= "Test Forum"
		
		# Retrieve the parent forum from the database so that it will have a
		# forum id
		parent_forum = services.forum.ForumRecordService.by_title(
			"Parent Forum"
		)
		
		dbforum.parent_id = parent_forum.forum_id
		DBSession.add(dbforum)
		
		# The CategoryEditActions tests need there to be a child forum with a
		# grandparent. So this forum will be a child of the main test forum.
		child_forum			= models.forum.Forum()
		child_forum.title	= "Child Forum"
		
		# Retrieve the test forum from the database so that it will have a
		# forum_id primary key.
		dbforum = services.forum.ForumRecordService.by_title("Test Forum")
		
		child_forum.parent_id = dbforum.forum_id
		DBSession.add(child_forum)
		
		# The group record service tests will need a group to be in the database
		dbgroup			= models.group.Group()
		dbgroup.title	= "Test Group"
		DBSession.add(dbgroup)
		
		# For the post to be added to the database, it will need a topic.
		
		# Retrieve the test forum from the database so that it will have a forum
		# id primary key.
		# This has already been done now.
		
		dbtopic					= models.topic.Topic()
		dbtopic.forum_id		= dbforum.forum_id
		dbtopic.subject			= "Test Topic"
		dbtopic.sticky_status	= False
		
		# The post record service tests need a test post.
		
		# Retrieve the topic from the database so that it will have a post_id.
		dbtopic = services.topic.TopicRecordService.by_id(1)
		
		dbpost				= models.post.Post()
		dbpost.topic_id		= dbtopic.topic_id
		dbpost.user_id		= dbuser.user_id
		dbpost.posted_date	= INIT_DATE
		dbpost.message		= "Test Post"
		
		# We will have to have the actual powers in the test database eventually
		# so for right now just leave them be so that we can don't have to undo
		# a whole bunch of work.
	return DBSession

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
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	
	def test_all(self):
		from .models.services.ban import BanRecordService
		
		bans = BanRecordService.all()
		
		# We're getting a list. Use list operations.
		self.assertEqual(len(bans), 1)
	
	def test_by_id(self):
		from .models.services.ban import BanRecordService
		
		# I'm not sure if ban_id starts at 0 or 1.
		# According to the SQLite documentation it starts with 1.
		ban = UserRecordService.by_id(1)
		
		# The return value is the ban we created earlier. Check against all of
		# the values that should be in the record.
		self.assertEqual(ban.start_date, INIT_DATE)
		self.assertEqual(ban.user.user_id, 1)
	
	def test_get_paginator(self):
		from .models.services.ban import BanRecordService
		
		# I'm not sure how to test url_maker or even if I can.
		
		# I'm not sure what to expect from the get paginator. I'm pretty sure it
		# returns a list.
	

class ForumServiceTests(unittest.TestCase):
	def setUp(self):
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	
	def test_all(self):
		from .models.services.forum import ForumRecordService
		
		forums = ForumRecordService.all()
		self.assertEqual(len(forums), 2)
	
	def test_by_id(self):
		from .models.services.forum import ForumRecordService
		
		# For this test get the second forum in the database since it has more
		# interesting attributes.
		forum = ForumRecordService.by_id(2)
		
		self.assertEqual(forum.title, "Test Forum")
		self.assertEqual(forum.parent_id, 1)
	
	def test_by_parent(self):
		from .models.services.forum import ForumRecordService
		
		forums = ForumRecordService.by_parent(1)
		self.assertEqual(len(forums), 1)
	
	def test_by_title(self):
		from .models.services.forum import ForumRecordService
		
		forum = ForumRecordService.by_title("Test Forum")
		self.assertEqual(forum.forum_id, 2)
		self.assertEqual(forum.parent_id, 1)
	

class GroupServiceTests(unittest.TestCase):
	def setUp(self):
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	
	def test_all(self):
		from .models.services.group import GroupRecordService
		
		groups = GroupRecordService.all()
		self.assertEqual(len(groups), 1)
	
	def test_by_id(self):
		from .models.services.group import GroupRecordService
		
		group = GroupRecordService.by_id(1)
		self.assertEqual(group.title, "Test Group")
	
	def test_by_title(self):
		from .models.services.group import GroupRecordService
		
		group = GroupRecordService.by_title("Test Group")
		self.assertEqual(group.group_id, 1)
	

class MembershipServiceTests(unittest.TestCase):
	# Currently the membership service is empty. This is because all membership
	# access is done through other models.
	def setUp(self):
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	

class PermissionServiceTests(unittest.TestCase):
	# See MembershipServiceTests
	def setUp(self):
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	

class PostServiceTests(unittest.TestCase):
	def setUp(self):
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	
	def test_all(self):
		from .models.services.post import PostRecordService
		
		posts = PostRecordService.all()
		self.assertEqual(len(posts), 1)
	
	def test_by_id(self):
		from .models.services.post import PostRecordService
		
		post = PostRecordService.by_id(1)
		self.assertEqual(post.topic_id, 1)
		self.assertEqual(post.user_id, 1)
		self.assertEqual(post.posted_date, INIT_DATE)
		self.assertEqual(post.message, "Test Post")
	
	def test_get_paginator(self):
		from .models.services.post import PostRecordService
		
		# I'm not sure how to test url_maker or even if I can.
		
		# I'm not really sure what the paginator functions will return. I'm
		# pretty sure it will be a list.
	

class PowerServiceTests(unittest.TestCase):
	def setUp(self):
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	

class TopicServiceTests(unittest.TestCase):
	def setUp(self):
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	
	def test_all(self):
		from .models.services.topic import TopicRecordService
		
		topics = TopicRecordService.all()
		self.assertEqual(len(topics), 1)
	
	def test_by_id(self):
		from .models.services.topic import TopicRecordService
		
		topic = TopicRecordService.by_id(1)
		self.assertEqual(topic.forum_id, 2)
		self.assertEqual(topic.subject, "Test Topic")
		self.assertEqual(topic.sticky_status, False)
		self.assertEqual(topic.forum_id, 2)
	
	# TopicRecordService has a myriad of paginator functions that I am not sure
	# exactly how to test. I'm pretty sure they return lists. But since I am not
	# confident of how to do this for the time being I will leave it for later.
	

class UserServiceTests(unittest.TestCase):
	def setUp(self):
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	
	def test_all(self):
		from .models.services.user import UserRecordService
		
		users = UserRecordService.all()
		self.assertEqual(len(users), 1)
	
	def test_by_id(self):
		from .models.services.user import UserRecordService
		
		user = UserRecordService.by_id(1)
		self.assertEqual(user.username, "TestUser")
		self.assertEqual(user.email_address, "test@test.tst")
		
		# We will want to test the password at some point.
		
		self.assertEqual(user.join_date, INIT_DATE)
	

  #####                                         #     #                   #######                            
 #     #  ####  #####  # #####  #####  ####     #     # #    # # #####       #    ######  ####  #####  ####  
 #       #    # #    # # #    #   #   #         #     # ##   # #   #         #    #      #        #   #      
  #####  #      #    # # #    #   #    ####     #     # # #  # #   #         #    #####   ####    #    ####  
       # #      #####  # #####    #        #    #     # #  # # #   #         #    #           #   #        # 
 #     # #    # #   #  # #        #   #    #    #     # #   ## #   #         #    #      #    #   #   #    # 
  #####   ####  #    # # #        #    ####      #####  #    # #   #         #    ######  ####    #    ####  
class InitializedbTests(unittest.TestCase):
	# I'm not sure how to do any of this testing.
	
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
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	
	def test_home(self):
		from .views.category import CategoryViews
		
		request		= testing.DummyRequest()
		inst		= CategoryViews(request)
		response	= inst.home()
		self.assertEqual('Welcome!', response['title_message'])
	
	def test_view_category(self):
		from .views.category import CategoryViews
		
		# The view category has two different branches. In one branch there is
		# not a valid forum_id so the software returns an HTTPNotFound call. In
		# the other the landing page for a valid forum is returned. Because I
		# need to access the database in order to do this, I don't know
		# *exactly* how to do this.
		
		# So for the branching calls there should definitely be more than one
		# test function. Each one should test a specific branch. As for the
		# database work, I still have to find a solution to that.
		
		# We need to create a good request. To do this a route has to be matched
		# while the request is being made.
		request		= testing.DummyRequest(params={'forum_id': 2})
		inst		= CategoryViews(request)
		response	= inst.view_category()
		
		# We know that a good request will have a dictionary response.
		self.assertEqual(response, {'title_message': "Test Forum"})
	
	def test_category_not_found(self):
		from .views.category import CategoryViews
		from pyramid.httpexceptions import HTTPNotFound
		
		# This is also dependant upon querying the database. We will need to
		# create a request that has a URL that will cause view_category to throw
		# and HTTPNotFound
		request		= testing.DummyRequest(params={'forum_id': 4})
		inst		= CategoryViews(request)
		response	= inst.view_category()
		
		# We know that a bad request will have an HTTPNotFound response.
		self.assertEqual(response, HTTPNotFound())
	

class CategoryEditActions(unittest.TestCase):
	# The tearDown in this case will have to remove any changes made to the
	# database. It should probably also have its own entry that it is allowed to
	# edit and then have it be torn down as well.
	def setUp(self):
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	
	def test_create_forum_valid_parent_id(self):
		from .view.category import CategoryEditActions
		from pyramid.httpexceptions import HTTPFound
		
		# I need to make sure that the request method is a post. Then I also
		# need to make sure that form is valid somehow. This looks hard.
		
		# This is not as hard as it looked at first. I just need to figure out
		# how to create POST data in my DummyRequest
		request = testing.DummyRequest(
			params={'current_forum_id': 1, 'action': 'create'}, 
			post={'title': "New Forum", 'parent_id': 1}
		)
		
		inst		= CategoryEditActions(request)
		response	= inst.create_forum()
		
		# response should be an HTTPFound call.
		self.assertEqual(response, HTTPFound(location=request.route_url(
					'forum', 
					forum_id=1,
					slug="New Forum"
				)
			)
		)
	
	def test_create_forum_valid_jotun(self):
		from .view.category import CategoryEditActions
		from pyramid.httpexceptions import HTTPFound
		
		request = testing.DummyRequest(
			params={'current_forum_id': None, 'action': 'create'},
			post={'title': "New Forum", 'parent_id': None}
		)
		
		inst		= CategoryEditActions(request)
		response	= inst.create_forum()
		
		# response should be an HTTPFound call. Which will need to request url.
		self.assertEqual(response, HTTPFound(location=request.route_url(
					'home'
				)
			)
		)
	
	def test_crate_forum_with_parent_id(self):
		from .view.category import CategoryEditActions
		
		request		= testing.DummyRequest(params={
				'current_forum_id': 1, 
				'action': 'create'
			}
		)
		
		inst		= CategoryEditActions(request)
		response	= inst.create_forum()
		
		# Realistically I could probably test all of this with one assert, but
		# this was easier.
		
		# What I really need to test is what the values in the form attribute of
		# the returned dictionary should be.
		self.assertEqual(response['form'].parent_id.choices, [
				(1, "Parent Forum"), 
				(2, "Test Forum")
			]
		)
		
		# The action should be create, otherwise the wrong function call this is
		self.assertEqual(response['action'], 'create')
		
		# The current forum id was set to one, and it should be returned as one.
		self.assertEqual(response['current_forum_id'], 1)
	
	def test_crate_forum_without_parent_id(self):
		from .view.category import CategoryEditActions
		
		request		= testing.DummyRequest(params={
				'current_forum_id': None,
				'action': 'create'
			}
		)
		
		inst		= CategoryEditActions(request)
		response	= inst.create_forum()
		
		self.assertEqual(response['form'].parent_id.choices, [
				(1, "Parent Forum")
			]
		)
		
		self.assertEqual(response['action'], 'create')
		self.assertEqual(response['current_forum_id'], None)
	
	def test_edit_forum_valid_id_valid_form(self):
		from .view.category import CategoryEditActions
		from pyramid.httpexceptions import HTTPFound
		
		request	= testing.DummyRequest(
			params={'forum_id': 1, 'action': 'edit'},
			post={'title': "Edited Forum", 'parent_id': None, 'forum_id': 2}
		)
		
		inst		= CategoryEditActions(request)
		response	= inst.edit_forum()
		
		self.assertEqual(response, HTTPFound(location=request.route_url(
					'forum',
					forum_id=2
					slug="Edited Forum"
				)
			)
		)
	
	def test_edit_forum_with_grandparent(self):
		from .view.category import CategoryEditActions
		
		request = testing.DummyRequest(params={'forum_id': 3, 'action': 'edit'})
		
		inst		= CategoryEditActions(request)
		response	= inst.edit_forum()
		
		# Check the choices for the parent id of the form. These should be the
		# children of the grandparent
		self.assertEqual(response['form'].parent_id.choices, ['Test Forum'])
		
		# Also check the action, which should be edit since this is an edit test
		self.assertEqual(response['action'], 'edit')
	
	def test_edit_forum_no_grandparent(self):
		from .view.category import CategoryEditActions
		
		request = testing.DummyRequest(params={'forum_id': 2, 'action': 'edit'})
		
		inst		= CategoryEditActions(request)
		response	= inst.edit_forum()
		
		# Check the choices of the parent id of the form. These should be the
		# forums without parents.
		self.assertEqual(response['form'].parent_id.choices, ['Parent Forum'])
		
		# Also check the action, which should be edit since this is an edit test
		self.assertEqual(response['action'], 'edit')
	
	def test_edit_invalid_forum(self):
		from .view.category import CategoryEditActions
		from pyramid.httpexceptions import HTTPNotFound
		
		request = testing.DummyRequest(params={'forum_id': 4, 'action': 'edit'})
		
		inst		= CategoryEditActions(request)
		response	= inst.edit_forum()
		
		self.assertEqual(response, HTTPNotFound())
	

class DiscussionViewsTests(unittest.TestCase):
	def setUp(self):
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	
	def test_discussion_view_valid_topic(self):
		from .views.discussion import DiscussionViews
		
		request		= testing.DummyRequest(params={'topic_id': 1})
		inst		= DiscussionViews(request)
		response	= inst.view_discussion()
		
		self.assertEqual(response['topic'].subject, "Test Topic")
	
	def test_discussion_view_invalid_topic(self):
		from .views.discussion import DiscussionViews
		from pyramid.httpexceptions import HTTPNotFound
		
		request		= testing.DummyRequest(params={'topic_id': 2})
		inst		= DiscussionViews(request)
		response	= inst.view_discussion()
		
		self.assertEqual(response, HTTPNotFound())
	

class TopicEditActionsTests(unittest.TestCase):
	def setUp(self):
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	
	def test_create_topic_valid_forum_valid_form(self):
		from .views.discussion import TopicEditActions
		from pyramid.httpexceptions import HTTPFound
		
		request = testing.DummyRequest(
			params={'forum_id': 2, 'action': 'create'},
			post={'subject': "New Topic", 'forum_id': 2}
		)
		
		inst		= TopicEditActions(request)
		response	= inst.create_topic()
		
		self.assertEqual(response, HTTPFound(request.route_url(
					request.route_url('post_action', action='create', topic_id=2)
				)
			)
		)
	
	def test_create_topic_valid_forum_invalid_form(self):
		from .views.discussion import TopicEditActions
		
		request = testing.DummyRequest(params={
				'forum_id': 2, 
				'action': 'create'
			}
		)
		
		inst		= TopicEditActions(request)
		response	= inst.create_topic()
		
		# Check to see that the choices of the forum id are correct.
		self.assertEqual(response['form'].forum_id.choices, [(2, "Test Forum")])
		
		# Check that the action is still equal to 'create'
		self.assertEqual(response['action'], 'create')
		
		# Check that the sent forum is correct.
		self.assertEqual(response['forum'].forum_id, 2)
		self.assertEqual(response['forum'].title, "Test Forum")
	
	def test_create_topic_invalid_forum(self):
		from .views.discussion import TopicEditActions
		from pyramid.httpexceptions import HTTPNotFound
		
		request = testing.DummyRequest(params={
				'forum_id': 4,
				'action': 'create'
			}
		)
		
		inst		= TopicEditActions(request)
		response	= inst.create_topic()
		
		self.assertEqual(response, HTTPNotFound)
	
	def test_edit_topic_valid_topic_valid_form(self):
		from .views.discussion import TopicEditActions
		from pyramid.httpexceptions import HTTPFound
		
		request = testing.DummyRequest(
			params={'topic_id': 1, 'action': 'edit'}
			post={'subject': "Edited Topic", 'forum_id': 3, 'topic_id': 1}
		)
		
		inst		= TopicEditActions(request)
		response	= inst.edit_topic()
		
		self.assertEqual(response, HTTPFound(location=request.route_url(
					'topic', 
					topic_id=1, 
					slug="Edited Topic"
				)
			)
		)
	
	def test_edit_topic_valid_topic_invalid_form(self):
		from .views.discussion import TopicEditActions
		from pyramid.httpexceptions import HTTPNotFound
		
		request = testing.DummyRequest(params={
				'topic_id': 1, 
				'action': 'edit'
			}
		)
		
		inst		= TopicEditActions(request)
		response	= inst.edit_topic()
		
		# Check to make sure the form has enough forum choices.
		self.assertEqual(len(response['form'].forum_id.choices), 3)
		
		# Make sure the action is passed along correctly.
		self.assertEqual(response['action'], 'edit')
		
		# Make sure that the forum is the correct forum.
		self.assertEqual(response['forum'].forum_id, 2)
		self.assertEqual(response['forum'].title, "Test Forum")
	
	def test_edit_topic_invaid_topic(self):
		from .views.discussion import TopicEditActions
		
		request = testing.DummyRequest(params={
				'topic_id': 2,
				'action': 'edit'
			}
		)
		
		inst		= TopicEditActions(request)
		response	= inst.edit_topic()
		
		self.assertEqual(response, HTTPNotFound)
	

class PostEditActionsTests(unittest.TestCase):
	def setUp(self):
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	
	def test_create_post_valid_topic_valid_form(self):
		from .views.discussion import PostEditActions
		from pyramid.httpexceptions import HTTPFound
		
		request = testing.DummyRequest(
			params={'topic_id': 1},
			post={'message': "This is a new message"}
		)
		
		inst		= PostEditActions(request)
		response	= inst.create_post()
		
		self.assertEqual(response, HTTPFound(location=request.route_url(
					'topic',
					topic_id=1
				)
			)
		)
	
	def test_create_post_valid_topic_invalid_form(self):
		from .views.discussion import PostEditActions
		
		request = testing.DummyRequest(params={
				'topic_id': 1,
				'action': 'create'
			}
		)
		
		inst		= PostEditActions(request)
		response	= inst.create_post()
		
		# I'm not sure how to test that a form is returned, so I will leave that
		# for later testing when I can better understand how to do that.
		self.assertEqual(response['action'], 'action')
		self.assertEqual(response['topic'].subject, "Test Topic")
		self.assertEqual(response['topic'].topic_id, 1)
	
	def test_create_post_invalid_topic(self):
		from .view.discussion import PostEditActions
		from pyramid.httpexceptions import HTTPNotFound
		
		request = testing.DummyRequest(params={
				'topic_id': 2,
				'action': 'create'
			}
		)
		
		inst		= PostEditActions(request)
		response	= inst.create_post()
		
		self.assertEqual(response, HTTPNotFound())
	
	def test_edit_post_valid_post_valid_form(self):
		from .view.discussion import PostEditActions
		from pyramid.httpexceptions import HTTPFound
		
		request = testing.DummyRequest(
			params={'post_id': 1, 'action': 'edit'},
			post={'message': "This post has been edited", 'post_id': 1}
		)
		
		inst		= PostEditActions(request)
		response	= inst.edit_post()
		
		self.assertEqual(response, HTTPFound(location=request.route_url(
				'topic',
				topic_id=1,
				slug="Test Topic"
			)
		)
	
	def test_edit_post_valid_post_invalid_form(self):
		from .view.discussion import PostEditActions
		
		request = testing.DummyRequest(params={
				'post_id': 1,
				'action': 'edit'
			}
		)
		
		inst		= PostEditActions(request)
		response	= inst.edit_post()
		
		# I'm still not sure how to validate that the form that's returned is
		# correct, so instead I will validate that everyhing else is correct.
		self.assertEqual(response['action'], 'edit')
		self.assertEqual(response['topic'].subject, "Test Topic")
		self.assertEqual(response['topic'].topic_id, 1)
	
	def test_edit_post_invalid_post(self):
		from .view.discussion import PostEditActions
		from pyramid.httpexceptions import HTTPNotFound
		
		request = testing.DummyRequest(params={
				'post_id': 2,
				'action': 'edit'
			}
		)
		
		inst		= PostEditActions(request)
		response	= inst.edit_post()
		
		self.assertEqual(response, HTTPNotFound())
	

class ManagementViewsTests(unittest.TestCase):
	def setUp(self):
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	
	def test_view_management_valid_group(self):
		from .views.management import ManagementViews
		
		request		= testing.DummyRequest(params={'group_id': 1})
		inst		= ManagementViews(request)
		response	= inst.view_management()
		
		self.assertEqual(response['group'].group_id, 1)
		self.assertEqual(response['group'].title, "Test Group")
	
	def test_view_management_invalid_group(self):
		from .views.management import ManagementViews
		from pyramid.httpexceptions import HTTPNotFound
		
		request		= testing.DummyRequest(params={'group_id': 2})
		inst		= ManagementViews(request)
		response	= inst.view_management()
		
		self.assertEqual(response, HTTPNotFound())

class ManagementEditActionsTests(unittest.TestCase):
	def setUp(self):
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	
	

class PermissionEditActionsTests(unittest.TestCase):
	def setUp(self):
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	

class ParticipantViewsTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
	
	def tearDown(self):
		testing.tearDown()

class UserEditActionsTests(unittest.TestCase):
	def setUp(self):
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		
		transaction.abort()
		DBSession.remove()
		testing.tearDown()
	

class BanEditActionsTests(unittest.TestCase):
	def setUp(self):
		self.session	= _initTestingDB()
		self.config		= testing.setUp()
	
	def tearDown(self):
		import transaction
		from .models.meta import DBSession
		
		transaction.abort()
		DBSession.remove()
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