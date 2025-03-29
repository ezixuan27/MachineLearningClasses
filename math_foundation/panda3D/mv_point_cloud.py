#!/usr/bin/env python
from space import *

class cloud_of_points(space):
	def __init__(self):
		space.__init__(self)
		self.cloud = point_cloud(mean=[2,1,1])
		self.accept("m", self.move_cloud)

	def move_cloud(self):
		X = self.cloud.pos()
		X = X - 0.2
		self.cloud.redraw(X)
		

app = cloud_of_points()
app.run()


