#!/usr/bin/env python
from space import *
from numpy import cos, sin
from numpy import pi as π
from panda3d.core import LineSegs, NodePath
import math

class rotating_point(space):
	def __init__(self):
		space.__init__(self)
		self.v = self.create_vector(([1,1,1]))
		self.v2 = self.create_vector(([1,2,1]))

		self.taskMgr.add(self.rotate_x, "Rotate")
		self.taskMgr.add(self.rotate_y, "Rotate")


	def rotate_x(self, task):
		v = self.v
		θ = π/60
		# R = np.array([	[1, 0, 0],
		# 		[0, cos(θ), -sin(θ)],
		# 		[0, sin(θ), cos(θ)]])
		# R = np.array([	[cos(θ), 0, sin(θ)],
		# 		[0, 1, 0],
		# 		[-sin(θ), 0, cos(θ)]])
		R = np.array([	[cos(θ), -sin(θ), 0],
				[sin(θ), cos(θ), 0],
				[0,0,1]])
		new_loc = R @ v.pos
		v.redraw(new_loc)

		task.delayTime = 1/30.0
		return Task.again 	# Runs every 1/40 seconds
		#return Task.cont 	# Run every frame

	def rotate_y(self, task):
		v2 = self.v2
		θ = π/60
		R = np.array([	[1, 0, 0],
				[0, cos(θ), -sin(θ)],
				[0, sin(θ), cos(θ)]])
		# R = np.array([	[cos(θ), 0, sin(θ)],
		# 		[0, 1, 0],
		# 		[-sin(θ), 0, cos(θ)]])
		# R = np.array([[cos(θ), -sin(θ), 0],
		# 		[sin(θ), cos(θ), 0],
		# 		[0,0,1]])
		new_loc = R @ v2.pos
		v2.redraw(new_loc)

		task.delayTime = 1/30.0
		return Task.again 	# Runs every 1/40 seconds
		#return Task.cont 	# Run every frame

app = rotating_point()
app.run()

