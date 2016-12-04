from Fluents import Fluents
from States import States

class Goals(object):
	"""docstring for Goals"""
	def __init__(self):
		self.fluents = Fluents()
		self.start_goal = {'fluent':[self.fluents.Cooked], 'args':[{'obj':['C1'], 'reg':None, 'loc':None}]}
		self.goal_list = []
		self.goal_list.append(start_goal)
		