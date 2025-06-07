#!/usr/bin/env python
import numpy as np
from panda3d.core import LPoint3
from direct.task import Task
from space import space
from panda3d.core import DirectionalLight, AmbientLight, Vec4

class FlyingShip(space):
	def __init__(self):
		super().__init__()

		# Load the airplane model
		self.plane = self.load_mesh('airplane.glb')
		self.plane.setScale(2)
		self.plane.setPos(0, 5, 0)

		# Define flight path
		self.start_pos = np.array([0, 5, 0], dtype=float)
		self.end_pos = np.array([1, -6, 5], dtype=float)
		self.duration = 4.0  # seconds
		self.elapsed = 0.0
		self.flying = False

		# Accept spacebar to trigger flight
		self.accept("space", self.fly)

	def fly(self):
		if not self.flying:
			self.elapsed = 0.0
			self.flying = True
			taskMgr.add(self.update_flight, "update_flight")

	def update_flight(self, task):
		dt = globalClock.getDt()
		self.elapsed += dt

		t = min(self.elapsed / self.duration, 1.0)  # clamp to [0,1]
		pos = (1 - t) * self.start_pos + t * self.end_pos
		self.plane.setPos(*pos)

		if t >= 1.0:
			self.flying = False
			return Task.done
		else:
			return Task.cont

app = FlyingShip()
app.run()

