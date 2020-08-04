# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:04 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.setBlock(x+1,y-1,z+1,x-1,y-1,z-1,256)