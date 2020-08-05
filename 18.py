# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:04 2020

@author: SCE
"""
import time
import random
from mcpi.minecraft import Minecraft

mc=Minecraft.create()
pos=mc.player.getTilePos()
    
while True:
    y=pos.y+2
    x=pos.x+random.uniform(-20,20)
    z=pos.z+random.uniform(-20,20)
    
    mc.spawnEntity(x,y,z,10)
