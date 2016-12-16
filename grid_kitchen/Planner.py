from GridEnv import GridEnv
from States import States
from Operators import Operators
from Goals import Goals
import copy

class Planner(object):
	"""docstring for Planner"""
	def __init__(self, arg):
		self.state_now = States()
		self.grid_env = GridEnv([15], 3, self.state_now.obj_locs, self.state_now.obj_clean_state, self.state_now.obj_cook_state, [5,2], [8,2], [11,4])
		self.goals = Goals()
		#self.operators = Operators(self.grid_env, self.state_now, self.goals)
		self.OperatorNames = Operators.__subclassess__()
	self.OperatorDescriptions = []
		for n in self.OperatorNames:
			self.OperatorDescriptions.append(n(self.grid_env, self.state_now, self.goals))
		self.HPN(self.goals.goal_list[0], alpha)
		
	def HPN(self, goal, alpha):
		p = self.plan(goal, alpha)
		for [w,g] in p:
			if is_prim(w):
				self.operators.Execute(w, args)
			else:
				self.HPN(g, next_level(alpha,w))

	def plan(self, goal, alpha):
		return self.a_star_search(goal, self.goal_test(), self.applicable_ops(goal, alpha), self.num_fluents_not_satisfied(goal))

	def a_star_search(self, goal, goal_test, ops, h):
		return 0

	def goal_test(self):
		return 0

	def applicable_ops(self, goal, alpha):
		ops = []
		for i, f in enumerate(goal['fluent']):
			for O in self.operators.OperatorDescriptions:
				for j, r in enumerate(O['effect']['fluents']):
					w = apply_bindings(O, unify(f,r, goal['args'][i]), j)
					if w:
						for (pre_conds, effects, cost) in self.operators.Instances(alpha):
							sg = regress(f, pre_conds, effects)
							if sg:
								ops.append()



	def apply_bindings(O, binding, index):
		if binding:
			w = copy.deepcopy(O)
			w['effect']['args'][index] = binding
			return w
		else:
			return None

	def unify(f,r, args):
		if (f==r):
			return args
		else:
			return None


