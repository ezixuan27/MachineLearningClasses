#!/usr/bin/env python
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3, LineSegs, NodePath, TextNode
from panda3d.core import LVector3, LPoint3
from direct.task import Task
from panda3d.core import GeomVertexReader
import math

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Disable default camera controls
        self.disableMouse()

        # Set initial camera position in spherical coordinates
        self.cam_radius = 20
        self.cam_theta = math.pi / 4
        self.cam_phi = math.pi / 4

        # Create grid floor
        self.create_grid()

        # Create axes
        self.create_axes()

        # Create rotating sphere
        self.create_rotating_sphere()

        # Update camera task
        self.taskMgr.add(self.update_camera, "UpdateCameraTask")
        self.taskMgr.add(self.update_rotating_sphere, "UpdateRotatingSphereTask")

        # Mouse movement tracking
        self.accept("mouse1", self.start_mouse_tracking)
        self.accept("mouse1-up", self.stop_mouse_tracking)
        self.taskMgr.add(self.track_mouse, "TrackMouseTask")
        self.mouse_tracking = False
        self.last_mouse_pos = (0, 0)

        # Mouse scroll for zooming
        self.accept("wheel_up", self.zoom_in)
        self.accept("wheel_down", self.zoom_out)



#def get_sphere_vertices(self):
#    geom_node = self.sphere_np.find("**/+GeomNode").node()
#    vertex_list = []
#    
#    for i in range(geom_node.getNumGeoms()):
#        geom = geom_node.getGeom(i)
#        vdata = geom.getVertexData()
#        reader = GeomVertexReader(vdata, "vertex")
#
#        while not reader.isAtEnd():
#            vertex = reader.getData3()
#            vertex_list.append([vertex.x, vertex.y, vertex.z])
#    
#    return vertex_list

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
        axes.setThickness(5.0)  # Make axes thicker
        
        # X Axis (Red)
        axes.setColor(1, 0, 0, 1)
        axes.moveTo(0, 0, 0)
        axes.drawTo(length, 0, 0)
        
        # Y Axis (Green)
        axes.setColor(0, 1, 0, 1)
        axes.moveTo(0, 0, 0)
        axes.drawTo(0, length, 0)
        
        # Z Axis (Blue)
        axes.setColor(0, 0, 1, 1)
        axes.moveTo(0, 0, 0)
        axes.drawTo(0, 0, length)
        
        axes_node = axes.create()
        axes_np = self.render.attachNewNode(axes_node)

        # Add labels
        self.create_axis_label("X", length + 0.3, 0, 0, (1, 0, 0, 1))
        self.create_axis_label("Y", 0, length + 0.3, 0, (0, 1, 0, 1))
        self.create_axis_label("Z", 0, 0, length + 0.3, (0, 0, 1, 1))
    
    def create_axis_label(self, text, x, y, z, color):
        label = TextNode(text)
        label.setText(text)
        label.setTextColor(*color)
        label.setAlign(TextNode.ACenter)
        label_node = self.render.attachNewNode(label)
        label_node.setScale(0.5)
        label_node.setPos(x, y, z)
        label_node.setBillboardPointEye()  # Ensures visibility from both sides

    def create_rotating_sphere(self):
        self.sphere_np = self.loader.loadModel("models/misc/sphere")  # Load a generic sphere model
        self.sphere_np.reparentTo(self.render)
        self.sphere_np.setScale(0.1)  # Make it small
        self.sphere_np.setColor(0.2, 0.2, 0.6, 1)  # Set color to red
        self.rotation_angle = 0

    def update_rotating_sphere(self, task):
        self.rotation_angle += 0.02
        x = math.cos(self.rotation_angle)
        z = math.sin(self.rotation_angle)
        self.sphere_np.setPos(x, 0, z)
        return Task.cont

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

app = MyApp()
app.run()

