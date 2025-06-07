#!/usr/bin/env python
from panda3d.core import Filename
from space import space  # your custom ShowBase subclass

class load_example(space):
	def __init__(self):
		super().__init__()

		house = self.load_mesh("little_house_mesh.glb")
		house.setScale(2)
		house.setPos(0, 0, 1)

app = load_example()
app.run()

