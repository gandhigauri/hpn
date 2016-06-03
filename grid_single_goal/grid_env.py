class grid_env(object):
	"""docstring for grid_env"""
	def __init__(self, grid_size, num_obj, obj_locs, goal_reg):
		self.grid_length = grid_size[0]
		self.grid_breadth = grid_size[1]
		self.number_items = num_obj
		self.item_locs = obj_locs
		self.goal_locs = goal_reg
		self.create_grid()

	def grid_to_node(self, grid_id):
		row_id = grid_id[0]
		col_id = grid_id[1]
		node_id = row_id * self.grid_breadth + col_id
		return node_id

	def create_grid(self):
		grid = [["  X  " for i in range(self.grid_breadth)] for j in range(self.grid_length)]
		for l in range(self.grid_length):
			for b in range(self.grid_breadth):
				if [l,b] in (self.goal_locs):
					grid[l][b] = "  G  "
				for i in range(self.number_items):
					if [l,b] in ([self.item_locs[i]]):
						grid[l][b] = "  I" + str(i+1) + " "
			print grid[l]				

if __name__ == '__main__':
	"""pass the grid size(list tyoe [l,b]), number of objects, object locations(as list of lists), goal region"""
	set_env = grid_env([5,4], 2, [[1,2],[1,3]], [[4,0],[4,1]])
		 