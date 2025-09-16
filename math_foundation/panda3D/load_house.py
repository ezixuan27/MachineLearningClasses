#!/usr/bin/env python

from space import *
from panda3d.core import loadPrcFileData, AmbientLight, DirectionalLight, PointLight, Spotlight, Vec4, Vec3
loadPrcFileData("", "win-size 800 600") #optional, set window size
loadPrcFileData("", "window-title My Panda3D Scene") #optional, set window title

from direct.showbase.ShowBase import ShowBase


class load_house(space):
	def __init__(self):
		space.__init__(self)
		self.house = self.loader.loadModel("Luffy.glb") # or house_mesh2.glb
		
		self.house.reparentTo(self.render)
		self.house.setPos(0, 0, 1)
		#self.house.setRenderModeWireframe()


		# Add Ambient Light (fills the scene with a general light)
		#ambientLight = AmbientLight("ambientLight")
		#ambientLight.setColor(Vec4(0.2, 0.2, 0.2, 1)) # Dim white light
		#self.render.setLight(self.render.attachNewNode(ambientLight))
		
		# Add Directional Light (simulates sunlight)
		#directionalLight = DirectionalLight("directionalLight")


		#directionalLight.setColor(Vec4(1, 1, 0.8, 1)) # Slightly yellow light
		#directionalLight.setDirection(Vec3(0, 0, -1)) # Corrected: Using Vec3
		#self.render.setLight(self.render.attachNewNode(directionalLight))

app = load_house()
app.run()
