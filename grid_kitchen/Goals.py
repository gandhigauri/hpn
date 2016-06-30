from Fluents import Fluents
from States import States

class Goals(object):
	"""docstring for Goals"""
	def __init__(self):
		self.fluents = Fluents()
		self.start_goal = [self.fluents.Cooked('C1')]
		self.goal_list = []
		self.goal_list.append(start_goal)
		