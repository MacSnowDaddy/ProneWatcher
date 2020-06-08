from scene import *
from sound import *
import time
import threading
import motion
from objc_util import *

class MyScene():
    def __init__(self):
        self.isProne=False
        self.isLowBattery = False
        
        UIDevice = ObjCClass('UIDevice')
        self.device = UIDevice.currentDevice()
        self.device.setBatteryMonitoringEnabled_(True)

        self.t1 = threading.Thread(target=self.beep)
        self.t1.start()

    def update(self):
        motion.start_updates()
        time.sleep(0.3)
        g3 = motion.get_gravity()
        motion.stop_updates()
 #       for g in g3:
 #           print(round(g, 3), end = '\t')
 #       print()
        self.isProne = g3[2] > 0.3
        
        self.isLowBattery = self.device.batteryLevel() < 0.05
    
    def beep(self):
        while True:
            if self.isProne:
                se = play_effect(name='game:Error')
                time.sleep(0.5)
                stop_effect(se)
                time.sleep(0.5)
            elif self.isLowBattery:
                se = play_effect('game:Pulley')
                time.sleep(0.5)
                stop_effect(se)
                time.sleep(0.5)
            else:
                time.sleep(5)

if __name__ == '__main__':
    ms = MyScene()
    while True:
        ms.update()
        time.sleep(5)
