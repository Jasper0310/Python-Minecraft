# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:04 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()
while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlocks(x+10,y-1,z+10,x-10,y-1,z-10,46)



   
 
   
    