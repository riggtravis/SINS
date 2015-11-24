# We need a view base for other view classes to inherit.
class ViewBase:
	"""docstring"""
	def __init__(self, request):
		"""docstring"""
		self.request = request