class GridEnv(object):
	"""docstring for grid_env"""
	def __init__(self, grid_size, num_obj, obj_locs, obj_clean_state, obj_cook_state, sink_reg, stove_reg, home_reg):
		
		self.grid_length = grid_size[0]
		
		self.number_items = num_obj
		
		self.item_locs = obj_locs

		self.clean_states = obj_clean_state

		self.cook_states = obj_cook_state

		self.sink_locs = [sink_reg[0]]*sink_reg[1]
		for i in range(sink_reg[1]):
			self.sink_locs[i] = self.sink_locs[i] + i
		
		self.stove_locs = [stove_reg[0]]*stove_reg[1]
		for i in range(stove_reg[1]):
			self.stove_locs[i] = self.stove_locs[i] + i
		
		self.home_locs = [home_reg[0]]*home_reg[1]
		for i in range(home_reg[1]):
			self.home_locs[i] = self.home_locs[i] + i
		
		self.create_grid()


	def create_grid(self):

		grid = [" X " for i in range(self.grid_length)]

		for l in range(self.grid_length):

			if l in (self.sink_locs):
				grid[l] = " W "

			if l in (self.stove_locs):
				grid[l] = " C "

			if l in (self.home_locs):
				grid[l] = " H "	

			for i in range(self.number_items):
				if l in ([self.item_locs.values()[i]]):
					grid[l] = " " + self.item_locs.keys()[i]

		print grid				


#if __name__ == '__main__':

	#"""pass the grid size, number of objects, object locations(in dict format), object clean states, object cook states, sink region([start loc, size]), stove region, home region """

	#set_env = GridEnv([15], 3, {'C1': 2, 'C2': 1, 'C3': 4}, {'C1': False, 'C2': False, 'C3': False}, {'C1': False, 'C2': False, 'C3': False}, [5,2], [8,2], [11,4])
		