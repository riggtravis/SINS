""" view_base 

Classes:
* ViewBase
** This class provides common functionality to all view classes.
 
"""

class ViewBase:
	""" We need a view base for other view classes to inherit. """
	
	def __init__(self, request):
		""" We need the request made to be available to be manipulated. """
		self.request = request