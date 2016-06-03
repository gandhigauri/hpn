#from GridEnv import GridEnv

class Fluents(object):
	"""docstring for fluents"""
	def __init__(self, env):
		#self.grid_env = GridEnv([15], 3, {'C1': 2, 'C2': 1, 'C3': 4}, {'C1': False, 'C2': False, 'C3': False}, {'C1': False, 'C2': False, 'C3': False}, [5,2], [8,2], [11,4])
		self.grid_env = env

	def ObjLoc(self, obj, pos):
		"""whether object at given position"""
		if self.grid_env.item_locs[obj] is pos:
			print obj + " at position " + str(pos)
			return True
		else:
			print obj + " not at position " + str(pos)
			return False

	def In(self, obj, reg):
		"""whether object entirely contained in given region"""
		#if (min(reg) <= self.grid_env.item_locs[obj]) and (max(reg) >= self.grid_env.item_locs[obj]):
		if self.grid_env.item_locs[obj] in (reg):
			print obj + " entirely in " + str(reg)
			return True
		else:
			print obj + " not entirely in " + str(reg)
			return False

	def ClearX(self, reg, exceptions):
		"""whether region is clear of objects"""
		non_obj_locs = []
		for obj in (self.grid_env.item_locs.keys()):
			if obj not in (exceptions):
				non_obj_locs.append(self.grid_env.item_locs[obj])
		if not (list(set(non_obj_locs).intersection(reg))):
			print "its clear for " + str(exceptions)
			return True
		else:
			print "its not clear for " + str(exceptions)
			return False

	def Clean(self, obj):
		if (self.grid_env.clean_states[obj]) is True:
			print obj + " is clean"
			return True
		else:
			print obj + " is not clean"
			return False

	def Cooked(self, obj):
		if (self.grid_env.cook_states[obj]) is True:
			print obj + " is cooked"
			return True
		else:
			print obj + " is not cooked"
			return False

#if __name__ == '__main__':
#	fluents = Fluents()