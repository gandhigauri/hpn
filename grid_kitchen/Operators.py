from Fluents import Fluents
#from GridEnv import GridEnv
#from States import States
#from Goals import Goals

import random

class Operators(object):
	"""docstring for Operators"""
	def __init__(self, grid, state, goal):
		self.state_now = state
		self.grid_env = grid
		self.fluents = Fluents(self.state_now)
		self.goal_now = goal
		#self.is_prim = {'W': True, 'C': True, 'P': True, 'I': False, 'X': False}
		#self.execute = {'W': Wash, 'C': Cook, 'P': PickPlace}
		#self.Wash('C1')
		#self.grid_env.item_locs['C1']=8
		#self.Cook('C1')
		#self.sweptVol('C1',3,11)
		#self.PickPlace('C3',5)
		#self.In('C1',[1,2])
		#self.Clear(range(4,11),['C3'])
		#self.GenerateLocsInRegion('C1',[7,8])

	def Wash(self, obj):
		if (self.fluents.In(obj, self.grid_env.sink_locs)):
			self.state_now.obj_clean_state[obj] = True
			print obj + " washed"
		else:
			print obj + " not washed"

	def Cook(self, obj):
		if (self.fluents.In(obj, self.grid_env.stove_locs)) and (self.fluents.Clean(obj)):
			self.state_now.obj_cook_state[obj] = True
			print obj + " cooked"
		else:
			print obj + " not cooked"

	def PickPlace(self, obj, target_loc):
		#choose start_loc
		obj_loc = [self.state_now.obj_locs[obj]]
		#start_loc = random.choice(list(set(obj_loc).union(self.GenerateLocsInRegion(obj,reg))))
		start_loc = obj_loc[0]
		#preconditions
		if (self.fluents.ObjLoc(obj,start_loc)) and self.fluents.ClearX(self.sweptVol(obj,start_loc,target_loc),[obj]):
			self.state_now.obj_locs[obj] = target_loc
			print obj + " placed at " + str(target_loc)
		else:
			print obj + " not placed at " + str(target_loc)
		self.grid_env.create_grid()

	def sweptVol(self, obj, start_loc, target_loc):
	 	sweep = range(min(start_loc,target_loc), max(start_loc,target_loc)+1)
	 	print "sweptVol is " + str(sweep)
	 	return sweep

	def GenerateLocsInRegion(self, obj, reg):
		#defining set C for present goal
		C = []
		x = []
		for ex in (self.state_now.obj_locs.keys()):
			if ex not in ([obj]):
				x.append(ex)
		for r in range(0,self.grid_env.grid_length):
			if (self.fluents.ClearX([r],x) and (self.goal_now.goal_list[-1]):
				C.append(r)
		print "Set C is " + str(C)
		# TODO
		#defing set O for the other objects to be placed in the present goal
		O = []
		#defing set R
		R = list(set(reg)-(set(C).union(O)))
		print R
		return R

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
		for obj in (self.state_now.obj_locs.keys()):
			if obj not in (exceptions):
				if not (self.fluents.In(obj,list(set(range(0,self.grid_env.grid_length))-set(reg)))):
					check = 0
		if (check):
			print "ClearX fluent is " + str(self.fluents.ClearX(reg,exceptions))
			print "region " + str(reg) + " is clear of all objects except " + str(exceptions)
		else:
			print "ClearX fluent is " + str(self.fluents.ClearX(reg,exceptions))			
			print "region " + str(reg) + " is not clear of all objects except " + str(exceptions)
		
'''
if __name__ == '__main__':
	operators = Operators()
'''
