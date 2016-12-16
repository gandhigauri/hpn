from Fluents import Fluents
from Actions import Actions
import random 

class Operators(object):
	"""docstring for Operators"""
	def __init__(self, grid, state, goal):
		self.state_now = state
		self.grid_env = grid
		self.fluents = Fluents(self.state_now)
		self.goals = goal
		self.actions = Actions(self.state_now)


		self.effect = {}
		self.pre = {}
		self.cost = None
		self.isPrim = False
		self.prim = None
		self.choose = None
		self.maxAlpha = 0

	def operator_instances(alpha):
		aux_list = []
		aux_list.append(self.pre['fluents'][0:alpha])
		if len(aux_list) == len(self.pre['fluents']):
			if self.prim:
				self.isPrim = True

    	if alpha is 0:
    		return [(None, self.effect, self.cost)]
    	elif alpha < self.maxAlpha:
    		abstracted_pre = self.bind(self.pre, alpha)
    		tup = []
    		for pre in abstracted_pre:
    			tup.append((pre, self.effect, self.cost))
			return tup
    	else:
    		self.isPrim = True

    def bind(pre_conds, alpha):
    	return None

