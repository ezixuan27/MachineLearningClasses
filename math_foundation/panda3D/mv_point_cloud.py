#!/usr/bin/env python
from space import *
import numpy as np
from numpy import cos, sin
from numpy import pi as π


#!/usr/bin/env python
import numpy as np
from direct.task import Task
from space import space

class FlyingShip(space):
	def __init__(self):
		super().__init__()

		self.plane = self.load_mesh("airplane.glb")
		self.plane.setScale(2)
		self.plane.setPos(0,5,0)
		self.plane.set_p(90) #plane pointing at sky as of start

		self.accept("space", self.fly)
		self.start = np.array([0.0,5.0,0.0])
		self.end = np.array([1.0,-6.0,5.0])

		self.duration = 4.0 
		self.flying = False
		self.elapsed = 0
		self.velocity = None

	def fly(self):
		if not self.flying:
			self.flying = True
			self.elapsed = 0.0
			self.plane.setPos(*self.start)
			self.velocity = (self.end - self.start) / self.duration
			taskMgr.add(self.update_flight, "update_flight")
		
	def update_flight(self,task):
		dt = globalClock.getDt()
		self.elapsed += dt

		move = self.velocity * dt
		x, y, z = self.plane.getPos()
		new_pos = np.array([x, y, z]) + move
		self.plane.setPos(*new_pos)

		if self.elapsed >= self.duration:
			self.plane.setPos(*self.end)
			self.flying = False
			return Task.done
		return Task.cont
				
app = FlyingShip()
app.run()
















# class A3(space):
#     def __init__(self):
#         super().__init__() 

#         self.P = np.array([
#             [3, 1, 2],
#             [5, 1, 2],
#             [5, 4, 2],
#             [3, 4, 2],
#             [3, 1, 5],
#             [5, 1, 5],
#             [5, 4, 5],
#             [3, 4, 5]
#         ])

#         self.center = self.P.mean(axis=0)
#         self.pc = point_cloud(self.P)

#         self.accept("x", self.rotate_x)
#         self.accept("y", self.rotate_y)
#         self.accept("z", self.rotate_z)
#         self.accept("s", self.smaller)
#         self.accept("b", self.larger)

#     def center_transform(self, matrix):
#         X = (self.pc.pos() - self.center) @ matrix.T + self.center
#         self.pc.redraw(X)

#     def rotate_x(self):
#         θ = np.radians(10)
#         Rx = np.array([[1, 0, 0],
#             [0, np.cos(θ), -np.sin(θ)],
#             [0, np.sin(θ), np.cos(θ)] ])
#         self.center_transform(Rx)

#     def rotate_y(self):
#         θ = np.radians(10)
#         Ry = np.array([[np.cos(θ), 0, np.sin(θ)],
#             [0, 1, 0],
#             [-np.sin(θ), 0, np.cos(θ)]])
#         self.center_transform(Ry)

#     def rotate_z(self):
#         θ = np.radians(10)
#         Rz = np.array([[np.cos(θ), -np.sin(θ), 0],
#             [np.sin(θ), np.cos(θ), 0],
#             [0, 0, 1]])
#         self.center_transform(Rz)

#     def larger(self):
#         S = np.eye(3) * 2
#         self.center_transform(S)

#     def smaller(self):
#         S = np.eye(3) * 0.5
#         self.center_transform(S)

# app = A3()
# app.run()

'''
Centering is necessary before rotation and scaling because we want the object to 
rotate around its center/axis instead of around (0,0,0). Without centering the object, 
when I try to rotate the shape, it will rotate around (0,0,0); and if we try to scale 
the object, it will instead scale the distance between the object and the origin.
'''















# class cloud_of_points(space):
# 	def __init__(self):
# 		space.__init__(self)
# 		X = np.array([[2,3,0],[4,5,0],[6,7,0],[8,9,0]])
# 		self.cloud = point_cloud(X=X)  
# 		self.accept("m", self.move_cloud)


# 	def move_cloud(self):
# 		H = np.eye(4) - (0.25 * np.ones((4,4)))
# 		pts = self.cloud.pos()          
# 		new_loc = H @ pts
# 		self.cloud.redraw(new_loc)     

# app = cloud_of_points()
# app.run()




# class cloud_of_points(space):
#     def __init__(self):
#         space.__init__(self)
#         X = np.array([[1,0,0],[0,1,0],[0,0,1],[-1,0,0]])
#         self.cloud = point_cloud(X=X)  
#         self.accept("m", self.move_cloud)

#     def move_cloud(self):
#         θ = π/90
#         R = np.array([[cos(θ), -sin(θ), 0],
#                       [sin(θ),  cos(θ), 0],
#                       [0, 0, 1]])
#         pts = self.cloud.pos()          
#         new_loc = 2 * (R @ pts.T).T
#         self.cloud.redraw(new_loc)     

# app = cloud_of_points()
# app.run()
