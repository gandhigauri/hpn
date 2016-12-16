from Operators import Operators 

class Wash(Operators):
	"""docstring for Wash"""
	def __init__(self, grid, state, goal):
		Operators.__init__(self, grid, state, goal)
		self.effect = {'fluents':[self.fluents.Clean], 'args':[{'obj':None, 'reg':None, 'loc':None}]}
      	self.pre = {'fluents':[self.fluents.In], 'args': [{'obj':None, 'reg':None, 'loc':None}]}
       	self.cost = 1
       	self.isPrim = False
        self.prim = self.actions.Wash
        self.choose = False
        self.maxAlpha = len(self.pre['fluents']) + 1

    def bind(pre_conds, alpha):
    	bound_pre = []
    	if (alpha-1) is 0:
    		pre_conds['args'][alpha - 1]['obj'] = self.effect['args'][0]['obj']
    		pre_conds['args'][alpha - 1]['reg'] = self.grid_env.sink_locs
    		bound_pre.append({'fluents':[pre_conds['fluents'][alpha-1]], 'args':[pre_conds['args'][alpha - 1]]})
    		return bound_pre

class Cook(Operators):
	"""docstring for Cook"""
	def __init__(self, grid, state, goal):
		Operators.__init__(self, grid, state, goal)
		self.effect = {'fluents':[self.fluents.Cooked], 'args':[{'obj':None, 'reg':None, 'loc':None}]}
      	self.pre = {'fluents':[self.fluents.In, self.fluents.Clean], 'args': [{'obj':None, 'reg':None, 'loc':None}, {'obj':None, 'reg':None, 'loc':None}]}
       	self.cost = 1
       	self.isPrim = False
        self.prim = self.actions.Cook
        self.choose = False
        self.maxAlpha = len(self.pre['fluents'])

  def bind(pre_conds, alpha):
  	bound_pre = []
  	if (alpha-1) is 0:
  		pre_conds['args'][alpha - 1]['obj'] = self.effect['args'][0]['obj']
  		pre_conds['args'][alpha - 1]['reg'] = self.grid_env.stove_locs
  		bound_pre.append({'fluents':[pre_conds['fluents'][alpha-1]], 'args':[pre_conds['args'][alpha - 1]]})
  		return bound_pre
  	elif (alpha-1) is 1:
  		pre_conds['args'][alpha - 1]['obj'] = self.effect['args'][0]['obj']
  		bound_pre.append({'fluents':[pre_conds['fluents'][alpha-1]], 'args':[pre_conds['args'][alpha - 1]]})
  		return bound_pre

class PickPlace(Operators):
	"""docstring for PickPlace"""
	def __init__(self, grid, state, goal):
		Operators.__init__(self, grid, state, goal)
		self.effect = {'fluents':[self.fluents.ObjLoc], 'args':[{'obj':None, 'reg':None, 'loc':None}]}
      	self.pre = {'fluents':[self.fluents.ObjLoc, self.fluents.ClearX], 'args': [{'obj':None, 'reg':None, 'loc':None}, {'obj':None, 'reg':None, 'loc':None}]}
       	self.cost = 1
       	self.isPrim = False
        self.prim = self.actions.PickPlace
        self.choose = True
        self.maxAlpha = len(self.pre['fluents'])

  def bind(pre_conds, alpha):
  	bound_pre = []
  	o = self.effect['args'][0]['obj']
  	l_start = list(set([self.state_now.obj_locs[o[0]]]).union(self.generate_locs(o[0], [self.grid_env.home_locs, self.grid_env.stove_locs, self.grid_env.sink_locs])))
  	if (alpha-1) is 0:
  		pre_conds['args'][alpha - 1]['obj'] = o
  		for ls in l_start:
  			pre_conds['args'][alpha - 1]['loc'] = ls
  			bound_pre.append({'fluents':[pre_conds['fluents'][alpha-1]], 'args':[pre_conds['args'][alpha - 1]]})
  		return bound_pre
  	elif (alpha-1) is 1:
  		pre_conds['args'][alpha - 1]['obj'] = o
  		for 
  		pre_conds['args'][alpha-1]['reg'] = swept_vol(o[0], )
  		bound_pre.append({'fluents':[pre_conds['fluents'][alpha-1]], 'args':[pre_conds['args'][alpha - 1]]})
  		return bound_pre

class In(Operators):
	"""docstring for In"""
	def __init__(self, grid, state, goal):
		Operators.__init__(self, grid, state, goal)
		self.effect = {'fluents':[self.fluents.In], 'args':[{'obj':None, 'reg':None, 'loc':None}]}
      	self.pre = {'fluents':[self.fluents.ObjLoc], 'args': [{'obj':None, 'reg':None, 'loc':None}]}
       	self.cost = 1
       	self.isPrim = False
        self.prim = None
        self.choose = False
        self.maxAlpha = len(self.pre['fluents'])

class In(Operators):
	"""docstring for In"""
	def __init__(self, grid, state, goal):
		Operators.__init__(self, grid, state, goal)
		self.effect = {'fluents':[self.fluents.ClearX], 'args':[{'obj':None, 'reg':None, 'loc':None}]}
      	self.pre = {'fluents':[self.fluents.In], 'args': [{'obj':None, 'reg':None, 'loc':None}]}
       	self.cost = 1
       	self.isPrim = False
        self.prim = None
        self.choose = False
        self.maxAlpha = len(self.pre['fluents'])
	
		