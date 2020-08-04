# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:04 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()

x,y,z = mc.player.getTilePos()
    
width=10
height=20
length=15

biock=57
air=0
    
mc.setBlocks(x,y,z,x+width,y+height,z+length,biock,)
mc.setBlocks(x+1,y+1,z+1,x+width-1,y+height-1,z+length-1,air,)    
    