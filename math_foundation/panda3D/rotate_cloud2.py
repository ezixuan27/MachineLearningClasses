#!/usr/bin/env python
from space import *
from numpy import cos, sin
from numpy import pi as π


class cloud_of_points(space):
	def __init__(self):
		space.__init__(self)

		X = np.array([[1,0,0], [0,1,0], [0,0,1], [-1,0,0]])
		self.cloud = point_cloud(X = X)
		self.accept("m", self.move_points)

	def move_points(self):
		T = 4.83
		θ = π/2
		R = np.array([	[cos(θ), -sin(θ), 0],
				[sin(θ),  cos(θ), 0],
				[0,	   0,	  1]])

		X = self.cloud.pos()
		X̂ = 2*(R @ X.T).T
		self.cloud.redraw(X̂)

		return Task.cont
		

app = cloud_of_points()
app.run()


