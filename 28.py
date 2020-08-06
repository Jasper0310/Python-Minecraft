# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:04 2020

@author: SCE
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

number=1

for i in range(10):
    
    for i in range(number):
        mc.spawnEntity(x,y,z,60)
        
    mc.postToChat("這次生了"+str(number)+'隻')

    number*=2
        
















