#!/usr/bin/env python
from space import *
from numpy import cos, sin, sqrt, vstack
from numpy import pi as π

class cloud_of_points(space):
	def __init__(self):
		space.__init__(self)
		self.total_time_elapsed = 0 
		self.cloud = point_cloud(mean=[0,0,0], n=4)
		self.taskMgr.add(self.move_points, "move_task")


		# Unit‑length basis (columns) -------------------------------
		v1 = np.array([ 1/sqrt(2),  1/sqrt(2), 0	 ])
		v2 = np.array([-1/sqrt(6),  1/sqrt(6), 2/sqrt(6) ])
		v3 = np.array([ 1/sqrt(3), -1/sqrt(3), 1/sqrt(3) ])
		self.V = vstack((v1, v2, v3))
		self.draw_new_basis(self.V)

	def move_points(self, task):
		V = self.V
		θ = 2*π/256
		R = np.array([	[cos(θ), -sin(θ), 0],
				[sin(θ),  cos(θ), 0],
				[0,	   0,	  1]])

		t = globalClock.getDt()  # Time elapsed since last frame
		self.total_time_elapsed = self.total_time_elapsed + t
		if self.total_time_elapsed > 0.01:
			X = self.cloud.pos() # each point is a row

			#X̂ =    fill in here
			#		remember the equation you saw was for X̂ᐪ , redraw requires X̂

			self.cloud.redraw(X̂)
			self.total_time_elapsed = 0

		return Task.cont
		

app = cloud_of_points()
app.run()


