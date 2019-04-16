#!/usr/bin/python3
import mortoray_path_finding as mpf
	
class MyFinder(mpf.draw.Finder):
	"""Integrate into the simple UI	"""
	def __init__(self):
		self.reset()
	
	def step(self, frames):
		self.max_distance = max( 0, self.max_distance + frames )
		for i in [1,20]:
			self.result = mpf.tutorial_1.fill_shortest_path(self.game.board, self.game.start, self.game.end, max_distance = self.max_distance)
			self.set_board(self.result)
			self.set_path(mpf.tutorial_1.backtrack_to_start(self.result, self.game.end))
			
	
	
	def reset(self):
		self.game = mpf.maze.create_wall_maze(20,10)
		self.max_distance = 18
		self.step(0)
	

finder = MyFinder()
finder.run()
