#!/usr/bin/env python
from space import *
from numpy import cos, sin
from numpy import pi as π

class cloud_of_points(space):
	def __init__(self):
		space.__init__(self)
		self.state = 'shrink'
		self.total_time_elapsed = 0 
		self.cloud = point_cloud(mean=[4,1,1], n=30)
		self.taskMgr.add(self.move_points, "move_task")

	def move_points(self, task):
		T = 4.83
		θ = 2*π/256
		R = np.array([	[cos(θ), -sin(θ), 0],
				[sin(θ),  cos(θ), 0],
				[0,       0,      1]])

		X = self.cloud.pos()
		n = X.shape[0] # tells u num of points
		C = np.eye(n) - (1/n)*np.ones((n,n))
		X̄ = (1/n)*np.ones((n,n)) @ X

		t = globalClock.getDt()  # Time elapsed since last frame
		self.total_time_elapsed = self.total_time_elapsed + t
		if self.state == 'shrink':
			s = 0.992
			if self.total_time_elapsed%T > 4: 
				self.state = 'expand'
		else:
			s = 1.04
			if self.total_time_elapsed%T < 4: self.state = 'shrink'

		X̂ᵀ = R @ (s*(C @ X).T)
		X̂ = X̂ᵀ.T + X̄
		self.cloud.redraw(X̂)

		return Task.cont
		

app = cloud_of_points()
app.run()


