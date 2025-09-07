#!/usr/bin/env python
import numpy as np
from panda3d.core import LPoint3, GeomVertexReader, GeomNode
from panda3d.core import RenderModeAttrib, NodePath, Mat3, Quat
from direct.task import Task
from space import space
from numpy import cos, sin, pi as π

class FlyingShip(space):
	def __init__(self):
		super().__init__()

		# Load the airplane model
		self.plane = self.load_mesh('airplane.glb')
		self.plane.setScale(2)
		self.plane.setPos(0, 5, 0)

		# Apply wireframe mode
		wireframe_mode = RenderModeAttrib.make(RenderModeAttrib.M_wireframe, 2.0)
		self.plane.setAttrib(wireframe_mode)
		self.plane.clearShader()
		self.plane.setTwoSided(True)
		self.plane.setColor(1, 1, 1, 1)
		self.plane.setLightOff()

		# Define flight path
		self.start_pos = np.array([0, 5, 5], dtype=float)
		self.end_pos = np.array([1, -6, 5], dtype=float)
		self.duration = 4.0
		self.elapsed = 0.0
		self.flying = False

		# Extract original vertex positions
		self.original_vertices = self.extract_vertices(self.plane)

		self.accept("space", self.fly)

	def fly(self):
		if not self.flying:
			self.elapsed = 0.0
			self.flying = True
			taskMgr.add(self.update_flight, "update_flight")

	def extract_vertices(self, nodepath):
		verts = []
		geom_nodes = nodepath.findAllMatches('**/+GeomNode')
		for node in geom_nodes:
			geom_node = node.node()
			for i in range(geom_node.getNumGeoms()):
				geom = geom_node.getGeom(i)
				vdata = geom.getVertexData()
				reader = GeomVertexReader(vdata, 'vertex')
				while not reader.isAtEnd():
					v = reader.getData3f()
					verts.append(np.array([v.x, v.y, v.z]))
		return np.array(verts)

	def update_flight(self, task):
		dt = globalClock.getDt()
		self.elapsed += dt
		t = min(self.elapsed / self.duration, 1.0)
		pos = (1 - t) * self.start_pos + t * self.end_pos
		self.plane.setPos(*pos)

		# Rotation around the local y-axis
		θ = 2 * π / 256
		Ry = np.array([
			[cos(θ), 0, sin(θ)],
			[0, 1, 0],
			[-sin(θ), 0, cos(θ)]
		])

		# Apply rotation to all original vertices
		rotated = (self.original_vertices @ Ry.T)
		center = rotated.mean(axis=0)
		translated = rotated - center

		# Optional debug: log a few points
		#print("Vertex[0] rotated:", translated[0])

		# Set new orientation
		mat = Mat3(*Ry.flatten())
		q = Quat()
		q.setFromMatrix(mat)
		self.plane.setQuat(q)

		if t >= 1.0:
			self.flying = False
			return Task.done
		else:
			return Task.cont

app = FlyingShip()
app.run()


##!/usr/bin/env python
#import numpy as np
#from panda3d.core import LPoint3
#from direct.task import Task
#from space import space
#from numpy import cos, sin, sqrt, vstack
#from numpy import pi as π
#from panda3d.core import RenderModeAttrib
#
#class FlyingShip(space):
#	def __init__(self):
#		super().__init__()
#
#		# Load the airplane model
#		self.plane = self.load_mesh('airplane.glb')
#		self.plane.setScale(2)
#		self.plane.setPos(0, 5, 0)
#
#		wireframe_mode = RenderModeAttrib.make(RenderModeAttrib.M_wireframe, 1.0)
#		self.plane.setAttrib(wireframe_mode)
#
#
#		# Define flight path
#		self.start_pos = np.array([0, 5, 5], dtype=float)
#		self.end_pos = np.array([1, -6, 5], dtype=float)
#		self.duration = 4.0  # seconds
#		self.elapsed = 0.0
#		self.flying = False
#
#		# Accept spacebar to trigger flight
#		self.accept("space", self.fly)
#
#	def fly(self):
#		if not self.flying:
#			self.elapsed = 0.0
#			self.flying = True
#			taskMgr.add(self.update_flight, "update_flight")
#
#	def update_flight(self, task):
#		dt = globalClock.getDt()
#		self.elapsed += dt
#		θ = 2*π/256
#		R = np.array([	[cos(θ), -sin(θ), 0],
#				[sin(θ),  cos(θ), 0],
#				[0,	   0,	  1]])
#
#		t = min(self.elapsed / self.duration, 1.0)  # clamp to [0,1]
#		pos = (1 - t) * self.start_pos + t * self.end_pos
#		H = np.eye(4) - (1/4)*np.ones((4,4))
#
#		#import pdb; pdb.set_trace()
#		self.plane.setPos(*pos)
#
#		if t >= 1.0:
#			self.flying = False
#			return Task.done
#		else:
#			return Task.cont
#
#app = FlyingShip()
#app.run()
#
