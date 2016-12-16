#from GridEnv import GridEnv

class Fluents(object):
	"""docstring for fluents"""
	def __init__(self, state):
		#self.grid_env = GridEnv([15], 3, {'C1': 2, 'C2': 1, 'C3': 4}, {'C1': False, 'C2': False, 'C3': False}, {'C1': False, 'C2': False, 'C3': False}, [5,2], [8,2], [11,4])
		#self.grid_env = env
		self.state_now = state

	def ObjLoc(self, args):
		"""whether object at given position"""
		if self.state_now.obj_locs[args['obj'][0]] is args['loc']:
			print args['obj'][0] + " at position " + str(args['loc'])
			return True
		else:
			print args['obj'][0] + " not at position " + str(args['loc'])
			return False

	def In(self, args):
		"""whether object entirely contained in given region"""
		#if (min(reg) <= self.grid_env.item_locs[obj]) and (max(reg) >= self.grid_env.item_locs[obj]):
		if self.state_now.obj_locs[args['obj'][0]] in (args['reg']):
			print args['obj'][0] + " entirely in " + str(args['reg'])
			return True
		else:
			print args['obj'][0] + " not entirely in " + str(args['reg'])
			return False

	def ClearX(self, args):
		"""whether region is clear of objects"""
		non_obj_locs = []
		for obj in (self.state_now.obj_locs.keys()):
			if obj not in (args['obj']):
				non_obj_locs.append(self.state_now.obj_locs[obj])
		if not (list(set(non_obj_locs).intersection(args['reg']))):
			print "its clear for " + str(args['obj'])
			return True
		else:
			print "its not clear for " + str(args['obj'])
			return False

	def Clean(self, args):
		"""whether object is clean"""
		if (self.state_now.obj_clean_state[args['obj'][0]]) is True:
			print args['obj'][0] + " is clean"
			return True
		else:
			print args['obj'][0] + " is not clean"
			return False

	def Cooked(self, args):
		"""whether object is cooked"""
		if (self.state_now.obj_cook_state[args['obj'][0]]) is True:
			print args['obj'][0] + " is cooked"
			return True
		else:
			print args['obj'][0] + " is not cooked"
			return False

#if __name__ == '__main__':
#	fluents = Fluents()