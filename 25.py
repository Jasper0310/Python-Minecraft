# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:04 2020

@author: SCE
"""
import time
from mcpi.minecraft import Minecraft

mc=Minecraft.create()

def plantTree(x,y,z):    
    mc.setBlocks(x-1,y+9,z-1,x+1,y+3,z+1,1)
    mc.setBlocks(x,y+3,z,x,y,z,3)
    
x,y,z=mc.player.getTilePos()

for i in  range(20):
    for j in  range(20):
        for k in  range(20):
            plantTree(x+i*5,y+i*j,z+i*k)
        
   