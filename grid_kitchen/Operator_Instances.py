from Fluents import Fluents
from Actions import Actions
import random 

class Operator_Instances(object):
	"""docstring for Operator_Instances"""
	def __init__(self, grid, state, goal):
		self.state_now = state
		self.grid_env = grid
		self.fluents = Fluents(self.state_now)
		self.goals = goal
		self.actions = Actions(self.state_now)

		self.effect = {}
		self.pre = {}
		self.cost = None
		self.prim = None
		self.choose = None

		self.OperatorDescriptions = []

		"""defining operator instances"""

		
        self.Wash = {'effect':{'fluents':[self.fluents.Clean], 'args':[{'obj':None, 'reg':None, 'loc':None}]}, \
        			'pre':{'fluents':[self.fluents.In], 'args': [{'obj':None, 'reg':self.grid_env.sink_locs, 'loc':None}]}, \
        			'cost':1 \
        			'prim':self.actions.Wash \
        			'choose':None}

	    self.Cook = {'effect':{'fluents':[self.fluents.Cooked], 'args':[{'obj':None, 'reg':None, 'loc':None}]}, \
        			'pre':{'fluents':[self.fluents.In, self.fluents.Clean], 'args': [{'obj':None, 'reg':self.grid_env.stove_locs, 'loc':None}, {'obj':None, 'reg':None, 'loc':None}]}, \
        			'cost':1 \
        			'prim':self.actions.Cook \
        			'choose':None}

        self.PickPlace = {'effect':{'fluents':[self.fluents.ObjLoc], 'args':[{'obj':None, 'reg':None, 'loc':None}]}, \
        			'pre':{'fluents':[self.fluents.ObjLoc, self.fluents.ClearX], 'args': [{'obj':None, 'reg':None, 'loc':None}, {'obj':None, 'reg':None, 'loc':None}]}, \
        			'cost':1 \
        			'prim':self.actions.Wash}

        self.In = {'effect':{'fluents':[self.fluents.Clean], 'args':[{'obj':None, 'reg':None, 'loc':None}]}, \
        			'pre':{'fluents':[self.fluents.In], 'args': [{'obj':None, 'reg':self.grid_env.sink_locs, 'loc':None}]}, \
        			'cost':1 \
        			'prim':self.actions.Wash}
        self.Clear = {'effect':{'fluents':[self.fluents.Clean], 'args':[{'obj':None, 'reg':None, 'loc':None}]}, \
        			'pre':{'fluents':[self.fluents.In], 'args': [{'obj':None, 'reg':self.grid_env.sink_locs, 'loc':None}]}, \
        			'cost':1 \
        			'prim':self.actions.Wash}
	    self.OperatorDescriptions = [self.Wash]
	
	def Cook(self, args):
		#self.effect = [self.fluents.Cooked(args['obj'])]
		#self.pre = [self.fluents.In(args['obj'],self.grid_env.stove_locs), self.fluents.Clean(args['obj'])]
		self.effect = [self.fluents.Cooked]
		self.pre = [self.fluents.In, self.fluents.Clean]
		self.prim = [self.actions.Cook]

	def PickPlace(self, args):
		#self.effect = [self.fluents.ObjLoc(args['obj'], args['loc'])]
		#TODO start loc should be generated from generate locs in regions
		#start_locs = self.state_now.obj_locs[args['obj']]
		#self.choose = {'start_loc':random.choice(start_locs)}
		#self.pre = [self.fluents.ObjLoc(args['obj'], self.choose['start_loc']), self.fluents.ClearX(self.sweptVol(args['obj'],self.choose['start_loc'],args['loc']),[args['obj']])]
		self.effect = [self.fluents.ObjLoc]
		#TODO start loc should be generated from generate locs in regions
		start_locs = self.state_now.obj_locs[args['obj']]
		self.choose = {'start_loc':random.choice(start_locs)}
		self.pre = [self.fluents.ObjLoc, self.fluents.ClearX]
		self.prim = [self.actions.PickPlace]

	def In(self, args):
		#self.effect = [self.fluents.In(args['obj'], args['reg'])]
		#locs = self.GenerateLocsInRegion(args)
		#self.choose = {'loc':random.choice(locs)}
		#self.pre = [self.fluents.ObjLoc(args['obj'], self.choose['loc'])]
		self.effect = [self.fluents.In]
		locs = self.GenerateLocsInRegion(args)
		self.choose = {'loc':random.choice(locs)}
		self.pre = [self.fluents.ObjLoc]

	def Clear(self, args):
		#self.effect = [self.fluents.ClearX(args['reg'], args['exceptions'])]
		#for obj in (self.state_now.obj_locs.keys()):
			#if obj not in (args['exceptions']):
				#self.pre = [self.fluents.In(obj, list(set(range(0,self.grid_env.grid_length))-set(args['reg'])))]
		self.effect = [self.fluents.ClearX]
		for obj in (self.state_now.obj_locs.keys()):
			if obj not in (args['exceptions']):
				self.pre = [self.fluents.In]

	def sweptVol(self, obj, start_loc, target_loc):
	 	sweep = range(min(start_loc,target_loc), max(start_loc,target_loc)+1)
	 	#print "sweptVol is " + str(sweep)
	 	return sweep

	def GenerateLocsInRegion(self, args):
		#defining set C for present goal
		C = []
		x = []
		for ex in (self.state_now.obj_locs.keys()):
			if ex not in ([args['obj']):
				x.append(ex)
		for r in range(0,self.grid_env.grid_length):
			if (self.fluents.ClearX([r],x) and (self.goals.goal_list[-1]):
				C.append(r)
		#print "Set C is " + str(C)
		# TODO
		#defing set O for the other objects to be placed in the present goal
		O = []
		for l in range(0,self.grid_env.grid_length):
			if (self.fluents.ObjLoc([l],x) and (self.goals.goal_list[-1]):
				O.append(r)
,
		#defing set R
		R = list(set(args['reg'])-(set(C).union(O)))
		print R
		return R

	def Execute(self, oper, args):
		self.oper(args)
		self.prim[0](args)



		
