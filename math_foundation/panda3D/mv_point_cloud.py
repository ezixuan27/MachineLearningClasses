#!/usr/bin/env python
from space import *
from numpy import cos, sin
from numpy import pi as π
from panda3d.core import LineSegs, NodePath, PointLight, Material, TransparencyAttrib
from direct.gui.OnscreenImage import OnscreenImage
import math

class cloud_of_points(space):
	def __init__(self):
		space.__init__(self)
		
		self.cloud = point_cloud(self, mean=[2,1,1])
		self.accept("m", self.move_cloud)
		print(type(self.cloud))

	def move_cloud(self):
		X = self.cloud.pos()
		X -= np.array([1,0,0.2])
		self.cloud.redraw(X)
		




#		# Set up material with emission (glow-like effect)
#		mat = Material()
#		mat.setEmission((1, 1, 0, 1))  # Yellow glow
#		self.sphere.setMaterial(mat)
#
#		# Add a light to enhance the glow
#		plight = PointLight("plight")
#		plight.setColor((1, 1, 0.2, 1))  # Light color
#		plnp = self.render.attachNewNode(plight)
#		plnp.setPos(1, 1, 1.3)
#		self.render.setLight(plnp)

		#self.sprite = OnscreenImage(image="./imgs/glow.png", pos=(0.1, 0.1, 0.1))
		#self.sprite.setTransparency(TransparencyAttrib.M_alpha)
		#self.sprite.setScale(0.1)


app = cloud_of_points()
app.run()


