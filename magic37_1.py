# 神秘圖騰

from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()

while True:
    mc.executeCommand("time add 10000")
    sleep(0.001)

