from vpython import *
from numpy import *
import math

step = 0.05
scene.background = vec(0.9, 0.9, 0.9)
sphere(make_trail = True, retain =30, trail_color = vec(1, 1, 0))
angle = 0
Moon = sphere(pos = vec(20, 0, 0),retain = 50, radius = 1, color = color.yellow, make_trail = True)
Earth = sphere(pos = vec(0, 0, 0), radius = 5, texture = textures.earth)
for i in arange(-1, 1, step):
    angle += 0.1
    if(angle >= 6.2799999):
        break
    sleep(1)
    Moon.pos = vec(Moon.pos.x * cos(angle) - Moon.pos.z * sin(angle), 0, Moon.pos.z * sin(angle) + Moon.pos.x * cos(angle))
    
    
    
    
    