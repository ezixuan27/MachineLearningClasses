#!/usr/bin/env python
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3, LineSegs, NodePath, TextNode
from panda3d.core import LVector3, LPoint3
from direct.task import Task
from panda3d.core import GeomVertexReader
import math
import numpy as np


def tuple_vector_to_numpy(tup): 
	return np.array(tup).reshape(-1, 1)

def ensure_tuple(obj):
	"""Check if the input is a tuple. If it's a NumPy array, convert it to a tuple."""
	if isinstance(obj, tuple):
		return obj  # Already a tuple, return as is
	elif isinstance(obj, np.ndarray):
		return tuple(obj.flatten())  # Convert NumPy array to a tuple
	else:
		raise TypeError("Input must be a tuple or a NumPy array.")

class vector():
	def __init__(self, render, pos, start=(0,0,0), color=(0.7, 0.7, 0, 1)):
		pos = ensure_tuple(pos)
		self.render = render
		self.draw_line(pos, start, color)

	def draw_line(self, pos, start=(0,0,0), color=(0.7, 0.7, 0, 1)):
		self.lines = LineSegs()
		self.lines.setColor(*color)  # Set the line color
		self.lines.setThickness(4)  # Set line thickness
		self.lines.moveTo(*start)  # Start point
		self.lines.drawTo(*pos)  # End point

		self.line_node = NodePath(self.lines.create())
		self.line_node.reparentTo(render)

		self.start = tuple_vector_to_numpy(start)
		self.pos = tuple_vector_to_numpy(pos)

	def pos(self):
		return self.pos

	def delete(self):
		self.line_node.removeNode()

	def redraw(self, pos, start=(0,0,0), color=(0.7, 0.7, 0, 1)):
		pos = ensure_tuple(pos)
		self.delete()
		self.draw_line(pos)



	def __rmatmul__(self, other):
		"""Implements other @ self"""
		if isinstance(other, np.ndarray):
			return other @ self.pos  # Right multiplication
		else:
			raise TypeError(f"Unsupported type {type(other)} for matrix multiplication")

	def __matmul__(self, other):
		"""Implements self @ other"""
		print(other)
		print(self.pos)
		print('\n\n\n')

		if isinstance(other, np.ndarray):
			return self.pos.T @ other  # Matrix multiplication
		elif isinstance(other, np.ndarray):
			return self.pos.T @ self.pos  # MyMatrix @ MyMatrix
		else:
			raise TypeError(f"Unsupported type {type(other)} for matrix multiplication")


class space(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)

		# Disable default camera controls
		self.disableMouse()

		# Create axes
		self.create_axes()

		# Create grid floor
		self.create_grid()

		# Update camera task
		self.taskMgr.add(self.update_camera, "UpdateCameraTask")


		# Set initial camera position in spherical coordinates
		self.cam_radius = 20
		self.cam_theta = math.pi / 4
		self.cam_phi = math.pi / 4
	

		# Mouse movement tracking
		self.accept("mouse1", self.start_mouse_tracking)
		self.accept("mouse1-up", self.stop_mouse_tracking)
		self.taskMgr.add(self.track_mouse, "TrackMouseTask")
		self.mouse_tracking = False
		self.last_mouse_pos = (0, 0)

		# Mouse scroll for zooming
		self.accept("wheel_up", self.zoom_in)
		self.accept("wheel_down", self.zoom_out)

	def create_vector(self, pos, start=(0,0,0), color=(0.7, 0.7, 0, 1)):
		return vector(self.render, pos, start=(0,0,0), color=(0.7, 0.7, 0, 1))


	def create_grid(self, size=10, spacing=1):
		grid = LineSegs()
		grid.setColor(0.5, 0.5, 0.5, 1)
		
		for i in range(-size, size + 1):
			grid.moveTo(i * spacing, -size * spacing, 0)
			grid.drawTo(i * spacing, size * spacing, 0)
			grid.moveTo(-size * spacing, i * spacing, 0)
			grid.drawTo(size * spacing, i * spacing, 0)
		
		grid_node = grid.create()
		self.render.attachNewNode(grid_node)



	def create_axes(self, length=5):
		axes = LineSegs()
		axes.setThickness(4.0)  # Make axes thicker
		
		# X Axis (Red)
		axes.setColor(0, 0, 0, 1)
		axes.moveTo(0, 0, 0)
		axes.drawTo(length, 0, 0)
		
		# Y Axis (Green)
		axes.setColor(0, 0, 0, 1)
		axes.moveTo(0, 0, 0)
		axes.drawTo(0, length, 0)
		
		# Z Axis (Blue)
		axes.setColor(0, 0, 0, 1)
		axes.moveTo(0, 0, 0)
		axes.drawTo(0, 0, length)
		
		axes_node = axes.create()
		axes_np = self.render.attachNewNode(axes_node)

		# Add labels
		self.create_axis_label("X", length + 0.3, 0, 0, (0, 0, 0, 1))
		self.create_axis_label("Y", 0, length + 0.3, 0, (0, 0, 0, 1))
		self.create_axis_label("Z", 0, 0, length + 0.3, (0, 0, 0, 1))
	




	def create_axis_label(self, text, x, y, z, color):
		label = TextNode(text)
		label.setText(text)
		label.setTextColor(*color)
		label.setAlign(TextNode.ACenter)
		label_node = self.render.attachNewNode(label)
		label_node.setScale(0.5)
		label_node.setPos(x, y, z)
		label_node.setBillboardPointEye()  # Ensures visibility from both sides

	def update_camera(self, task):
		x = self.cam_radius * math.sin(self.cam_phi) * math.cos(self.cam_theta)
		y = self.cam_radius * math.sin(self.cam_phi) * math.sin(self.cam_theta)
		z = self.cam_radius * math.cos(self.cam_phi)
		self.camera.setPos(x, y, z)
		self.camera.lookAt(0, 0, 0)
		return Task.cont

	def start_mouse_tracking(self):
		self.mouse_tracking = True
		if self.mouseWatcherNode.hasMouse():
			self.last_mouse_pos = (self.mouseWatcherNode.getMouseX(), self.mouseWatcherNode.getMouseY())

	def stop_mouse_tracking(self):
		self.mouse_tracking = False

	def track_mouse(self, task):
		if self.mouse_tracking and self.mouseWatcherNode.hasMouse():
			new_x, new_y = self.mouseWatcherNode.getMouseX(), self.mouseWatcherNode.getMouseY()
			dx = new_x - self.last_mouse_pos[0]
			dy = new_y - self.last_mouse_pos[1]
			
			self.cam_theta -= dx * 2
			self.cam_phi = max(0.1, min(math.pi - 0.1, self.cam_phi + dy * 2))  # Corrected inversion
			
			self.last_mouse_pos = (new_x, new_y)
		return Task.cont

	def zoom_in(self):
		self.cam_radius = max(2, self.cam_radius - 1)

	def zoom_out(self):
		self.cam_radius += 1


