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
	
	# management
	
	# participant
	
	# view_base
	

# We have service classes with functions that need to be tested.
# There is one service class for every model. All service models have the
# the following two methods:
#	all
#	by_id

class SinsFunctionalTests(unittest.TestCase):
	"""docstring"""
	def setUp(self):
		"""docstring"""
		from sins import main
		from webtest import TestApp
		
		app = main({})
		self.testapp = TestApp(app)
	
	# Just like the unit tests, functional tests will need to test different
	# functionalities. These functionalities include:
	#	category
	def test_home(self):
		"""docstring"""
		page = self.testapp.get('/', status=200)
		self.assertIn(b'<title>Welcome!', page.head)

	# Test all of the forum actions.
	def test_create(self):
		"""docstring"""
		
	
	def test_edit(self):
		"""docstring"""
		
	
	#	discussion
	#	participant
	# Test to see if the authentification messages are being displayed correctly
	def test_login(self):
		"""docstring"""
		page = self.testapp.get('/sign/in', status=200)
		self.assertIn(b'<title>Sign In', page.head)
	
	def test_logout(self):
		"""docstring"""
		page = self.testapp.get('/sighn/out', status=200)
		self.assertIn(b'Successfully logged out', page.body)