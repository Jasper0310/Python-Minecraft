# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:53:04 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()

mc,postToChat("I'mwatching you.")
while True:
    t=t+1
    mc.postToChat("第"+str(t)+"次")   