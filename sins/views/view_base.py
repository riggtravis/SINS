# We need a view base for other view classes to inherit.
class ViewBase:
	def __init__(self, request):
		self.request = request