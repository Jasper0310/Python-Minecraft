# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:04 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.setBlock(x,y,z,7)
mc.setBlock(x-1,y,z+1,7)
mc.setBlock(x,y,z+1+1,7)
mc.setBlock(x+1,y,z+1,7)
mc.setBlock(x+2,y,z,7)
mc.setBlock(x+1,y,z-1,7)
mc.setBlock(x,y,z,7)
mc.setBlock(x-1,y,z-1,7)
mc.setBlock(x-2,y,z,7)