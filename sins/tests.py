import unittest
import transaction

from pyramid import testing

from .models import DBSession

# I'm not clear on how this testing suite works. I'll have to either learn it or
# convert this whole thing to nose tests

class TestMyViewSuccessCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from .models import (
            Base,
            MyModel,
            )
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            model = MyModel(name='one', value=55)
            DBSession.add(model)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_passing_view(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['one'].name, 'one')
        self.assertEqual(info['project'], 'sins')


class TestMyViewFailureCondition(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from .models import (
            Base,
            MyModel,
            )
        DBSession.configure(bind=engine)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_failing_view(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info.status_int, 500)

class SinsViewTests(unittest.TestCase):
	def setUp(self):
		self.config = testing.setUp()
		
	def tearDown(self):
		testing.tearDown()
		
	# I need to create views in order to make some tests to test views.
	# The problem that I am having right now is that I am not sure how I need to
	# make my views in order to maintain a seperation of concerns. It seems to
	# me like every model should have a corresponding view file that contains
	# all of the view logic associated with that model. However, the examples I
	# have been looking at mostly treat views as overall functionality, which I
	# can understand. So I guess what I should do for right now is be flexible
	# and define the set of views for either scenario.
	
	# Model seperation scenario:
	#	ban
	#	forum
	#	group
	#	membership
	#	permission
	#	post
	#	power
	#	topic
	#	user
	
	# Functionality seperation scenario
	#	forum
	#	topic
	#	user
	
	# I have chosen to use the functionality based seperation scenario. I have
	# used these view controllers:
	#	category
	#	discussion
	#	participant
	
class SinsFunctionalTests(unittest.TestCase):
	def setUp(self):
		from sins import main
		from webtest import TestApp
		
		app = main({})
		self.testapp = TestApp(app)
	
	# Just like the unit tests, functional tests will need to test different
	# functionalities. These functionalities include:
	#	category
	#	discussion
	#	participant
	def test_home(self):
		page = self.testapp.get('/', status=200)
		self.assertIn(b'<title>Welcome!', page.head)