#!/usr/bin/env python
from panda3d.core import Filename
from space import space  # your custom ShowBase subclass

class GLBViewer(space):
	def __init__(self):
		super().__init__()

		# Use the built-in loader (already in ShowBase/space)
		
		model_path = "airplane.glb"
		#model_path = "little_house_mesh.glb"

		self.mesh = self.loader.load_model(Filename.from_os_specific(model_path))
		if not self.mesh:
			print("Failed to load model:", model_path)
			return

		self.mesh.reparentTo(render)
		self.mesh.setScale(2)
		self.mesh.setPos(0, 0, 1)
		self.mesh.setHpr(0, 0, 0)

		print("GLB model loaded successfully.")

app = GLBViewer()
app.run()

