# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:04 2020

@author: SCE
"""
import time
import random
from mcpi.minecraft import Minecraft

mc=Minecraft.create()

x,y,z = mc.player.getTilePos()
    
while True:
    color=random.randrange(16)
    mc.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,95,color)
    time.sleep(0.5)
    color=random.randrange(16)
    mc.setBlocks(x+3,y-1,z+3,x-3,y-1,z-3,95,color)
    time.sleep(0.5)
    color=random.randrange(16)
    mc.setBlocks(x+5,y-1,z+5,x-5,y-1,z-5,95,color)
    time.sleep(0.5)