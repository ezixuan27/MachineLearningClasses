#!/usr/bin/env python
from space import *
from numpy import cos, sin
from numpy import pi as π


class cloud_of_points(space):
	def __init__(self):
		space.__init__(self)

		X = np.array([[2,3,0], [4,5,0], [6,7,0], [8,9,0]])
		self.cloud = point_cloud(X = X)
		self.accept("m", self.center_points)

	def center_points(self):
		H = np.eye(4) - (1/4)*np.ones((4,4))
		X = self.cloud.pos()
		X̂ = H @ X
		self.cloud.redraw(X̂)

		return Task.cont
		

app = cloud_of_points()
app.run()


