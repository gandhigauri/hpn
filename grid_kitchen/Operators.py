from Fluents import Fluents
from GridEnv import GridEnv
import random

class Operators(object):
	"""docstring for Operators"""
	def __init__(self):
		self.grid_env = GridEnv([15], 3, {'C1': 2, 'C2': 1, 'C3': 4}, {'C1': False, 'C2': False, 'C3': False}, {'C1': False, 'C2': False, 'C3': False}, [5,2], [8,2], [11,4])
		self.fluents = Fluents(self.grid_env)
		#self.Wash('C1')
		#self.grid_env.item_locs['C1']=8
		#self.Cook('C1')
		#self.sweptVol('C1',3,11)
		#self.PickPlace('C1',5)
		#self.In('C1',[1,2])
		#self.Clear(range(4,11),['C3'])

	def Wash(self, obj):
		if (self.fluents.In(obj, self.grid_env.sink_locs)):
			self.grid_env.clean_states[obj] = True
			print obj + " washed"
		else:
			print obj + " not washed"

	def Cook(self, obj):
		if (self.fluents.In(obj, self.grid_env.stove_locs)) and (self.fluents.Clean(obj)):
			self.grid_env.cook_states[obj] = True
			print obj + " cooked"
		else:
			print obj + " not cooked"

	def PickPlace(self, obj, target_loc):
		#choose start_loc
		obj_loc = [self.grid_env.item_locs[obj]]
		#start_loc = random.choice(list(set(obj_loc).union(self.GenerateLocsInRegion(obj,reg))))
		start_loc = obj_loc[0]
		#preconditions
		if (self.fluents.ObjLoc(obj,start_loc)) and self.fluents.ClearX(self.sweptVol(obj,start_loc,target_loc),[obj]):
			self.grid_env.item_locs[obj] = target_loc
			print obj + " placed at " + str(target_loc)
		else:
			print obj + " not placed at " + str(target_loc)

	def sweptVol(self, obj, start_loc, target_loc):
	 	sweep = range(min(start_loc,target_loc), max(start_loc,target_loc)+1)
	 	print "sweptVol is " + str(sweep)
	 	return sweep

	def GenerateLocsInRegion(self, obj, reg):
		pass

	def In(self, obj, reg):
		#choose
		loc = random.choice(self.GenerateLocsInRegion(obj,reg))
		#preconditions
		if (self.fluents.ObjLoc(obj,loc)):
			print "In fluent is " + str(self.fluents.In(obj,reg))
			print obj + " at loc " + str(loc) + " in reg " + str(reg)
		else:
			print "In fluent is " + str(self.fluents.In(obj,reg))
			print obj + " at loc " + str(loc) + " not in reg " + str(reg)	

	def Clear(self, reg, exceptions):
		check = 1
		for obj in (self.grid_env.item_locs.keys()):
			if obj not in (exceptions):
				if not (self.fluents.In(obj,list(set(range(0,self.grid_env.grid_length))-set(reg)))):
					check = 0
		if (check):
			print "ClearX fluent is " + str(self.fluents.ClearX(reg,exceptions))
			print "region " + str(reg) + " is clear of all objects except " + str(exceptions)
		else:
			print "ClearX fluent is " + str(self.fluents.ClearX(reg,exceptions))			
			print "region " + str(reg) + " is not clear of all objects except " + str(exceptions)
		

if __name__ == '__main__':
	operators = Operators()

