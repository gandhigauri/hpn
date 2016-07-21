class States(object):
	"""docstring for States"""
	def __init__(self):
		self.obj_locs = {'C1': 2, 'C2': 1, 'C3': 4}
		self.obj_clean_state = {'C1': False, 'C2': False, 'C3': False}
		self.obj_cook_state = {'C1': True, 'C2': False, 'C3': False}