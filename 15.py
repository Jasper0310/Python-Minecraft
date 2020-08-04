# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:04 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()

x,y,z=mc.player.getPos()
try:    
    block=int(input('你要放什麼'))
    mc.setBlock(x,y,z,block)
except:
    mc.postToChat('只能寫數字')