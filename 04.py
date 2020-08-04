# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:04 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.setBlock(x,y,z,7)
mc.setBlock(x,y+1,z,7)
mc.setBlock(x,y+2,z,7)
mc.setBlock(x,y+3,z,7)
mc.setBlock(x,y+4,z,7)



