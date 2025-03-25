#!/usr/bin/env python
from space import *
from numpy import cos, sin, dot
from numpy import pi as π
import math
from direct.task import Task
import imageio
import os

class rotating_point(space):
    def __init__(self):
        space.__init__(self)
        self.v = self.create_vector((1,1,1))
        self.θ = π/256
        self.R = self.create_rotation_matrix(self.θ)

        self.taskMgr.add(self.rotate_x, "Rotate")
        self.recording = False
        self.record_task = None

        self.accept("r", self.start_recording)

    def create_rotation_matrix(self, θ):
        return np.array([  [1, 0, 0],
                              [0, cos(θ), -sin(θ)],
                              [0, sin(θ), cos(θ)]])

    def rotate_x(self, task):
        new_loc = dot(self.R, self.v.pos)
        self.v.redraw(new_loc)
        return Task.cont

    def start_recording(self):
        if not self.recording:
            self.recording = True
            self.record_task = self.taskMgr.add(self.record_screen, "RecordScreen")
            print("Recording started. Press 'r' to stop.")

    def record_screen(self, task):
        if self.recording:
            frame_count = task.frame
            if frame_count % 10 == 0:  # Record every 5th frame
                self.win.saveScreenshot("screenshot.png")
                if not hasattr(self, "frames"):
                    self.frames = []
                self.frames.append(imageio.imread("screenshot.png"))
                if len(self.frames) >= 100:  # Adjusted to account for every 5th frame
                    self.stop_recording()
                    self.save_gif()
            return Task.cont

#    def record_screen(self, task):
#        if self.recording:
#            self.win.saveScreenshot("screenshot.png")
#            if not hasattr(self, "frames"):
#                self.frames = []
#            self.frames.append(imageio.imread("screenshot.png"))
#            if len(self.frames) >= 30:  # 10 seconds at 3 frames per second
#                self.stop_recording()
#                self.save_gif()
#            return Task.cont

    def stop_recording(self):
        self.recording = False
        self.taskMgr.remove(self.record_task)
        print("Recording stopped.")

    def save_gif(self):
        imageio.mimsave("record.gif", self.frames, fps=15)
        print("GIF saved.")


app = rotating_point()
app.run()
