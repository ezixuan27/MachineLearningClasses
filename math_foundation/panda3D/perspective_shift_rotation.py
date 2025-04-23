#!/usr/bin/env python
from space import *
from numpy import cos, sin, sqrt, vstack
from numpy import pi as π

class cloud_of_points(space):
	def __init__(self):
		space.__init__(self)
		self.state = 'shrink'
		self.total_time_elapsed = 0 
		self.cloud = point_cloud(mean=[0,0,0], n=4)
		self.V = self.draw_new_basis()

		self.taskMgr.add(self.move_points, "move_task")



	def draw_new_basis(self,
						  length=5.0,
						  colors=((1, 1, 0, 1),   # yellow   for v1
								  (1, 0, 1, 1),   # magenta  for v2
								  (0, 1, 1, 1))): # cyan	 for v3

		# Unit‑length basis (columns) -------------------------------
		v1 = np.array([ 1/sqrt(2),  1/sqrt(2), 0	 ])
		v2 = np.array([-1/sqrt(6),  1/sqrt(6), 2/sqrt(6) ])
		v3 = np.array([ 1/sqrt(3), -1/sqrt(3), 1/sqrt(3) ])
		V = vstack((v1, v2, v3))
		print(V)
		
		# Draw and label --------------------------------------------
		vec1 = self.create_vector(v1, color=colors[0], thickness=5)
		vec2 = self.create_vector(v2, color=colors[1], thickness=5)
		vec3 = self.create_vector(v3, color=colors[2], thickness=5)
	
		# Optional tip labels (uncomment if you want them right away)
		self.create_axis_label("x", * (1.1 * v1), colors[0])
		self.create_axis_label("y", * (1.1 * v2), colors[1])
		self.create_axis_label("z", * (1.1 * v3), colors[2])
	
		return V


	def move_points(self, task):
		V = self.V
		θ = 2*π/256
		R = np.array([	[cos(θ), -sin(θ), 0],
				[sin(θ),  cos(θ), 0],
				[0,	   0,	  1]])

		#R = np.array([	[1, 0, 0],
		#				[0, cos(θ), -sin(θ)],
		#				[0, sin(θ), cos(θ)]])

		#R = np.array([	[cos(θ),  0, sin(θ)],
        #				[0,              1, 0            ],
        #				[-sin(θ), 0, cos(θ)] ])

		#import pdb; pdb.set_trace()
		t = globalClock.getDt()  # Time elapsed since last frame
		self.total_time_elapsed = self.total_time_elapsed + t
		if self.total_time_elapsed > 0.01:
			X = self.cloud.pos()
			X̂ = X @ V.T @ R.T @ V
			self.cloud.redraw(X̂)
			self.total_time_elapsed = 0

		return Task.cont
		

app = cloud_of_points()
app.run()


