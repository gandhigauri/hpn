class Actions(object):
	"""docstring for Actions"""
	def __init__(self, state):
		self.state_now = state
		
	def Wash(self, args):
		self.state_now.obj_clean_state[args['obj']] = True
		print args['obj'] + " washed"

	def Cook(self, args):
		self.state_now.obj_cook_state[args['obj']] = True
		print args['obj'] + " cooked"

	def PickPlace(self, args):
		self.state_now.obj_locs[args['obj']] = args['loc']
		print args['obj'] + " placed at " + str(args['loc'])

