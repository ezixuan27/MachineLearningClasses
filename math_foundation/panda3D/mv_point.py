#!/usr/bin/env python
from space import *
import numpy as np

class point_interpolation(space):
	def __init__(self):
		space.__init__(self)
		self.total_time_elapsed = 0

		self.p = point([1,1,1])
		self.start = self.p.pos()
		self.end = np.array([[-2],[0],[1]])
		self.direction = self.end - self.p.pos()
		self.accept("m", self.initialize_move)

	def initialize_move(self):
		self.taskMgr.add(self.move_point, "move_task")

	def move_point(self, task):
		t = globalClock.getDt()  # Time elapsed since last frame
		self.total_time_elapsed = self.total_time_elapsed + t
		
		#	we want to take exactly 4 seconds to move
		#	so we divide time by 4 to get percentage
		pcnt = self.total_time_elapsed/4
		if pcnt > 1: return Task.done

		new_loc = self.start + self.direction*pcnt
		self.p.redraw(new_loc)
		return Task.cont		

app = point_interpolation()
app.run()


