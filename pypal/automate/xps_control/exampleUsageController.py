'''
XPS exmaple

@author: henrik
'''
import osciCard.controller as card
import matplotlib.pyplot as plt 
import numpy as np
import sys
import getopt

def initializeStuff():
    from XPS_C8_drivers import XPS
    global xps
    xps = XPS()
    xps.GetLibraryVersion()
    global socketId
    socketId = xps.TCP_ConnectToServer("130.216.54.129",5001,3)
    print "connected to: ", socketId
    #print xps.CloseAllOtherSockets(socketId) #NEED ADMINISTRATIVE RIGHTS (ERROR -107)
    xps.ControllerStatusGet(socketId)
    xps.Login(socketId, "Administrator", "Administrator")
    #print self.xps.GroupStatusListGet(self.socketId)
    print "Controller is initialized."

def doStuff():
    global xps
    #print self.xps.GroupKill(self.socketId, "GROUP3")
    #print self.xps.GroupInitialize(socketId, "GROUP3")
    #print self.xps.GroupStatusGet(socketId, "GROUP3")
    #print xps.GroupHomeSearch(socketId, "GROUP3")
    #print xps.GatheringConfigurationSet(socketId,["GROUP3.POSITIONER.CurrentPosition"])
    #print xps.GatheringRun(socketId, 1000, 100)
    #print xps.GroupHomeSearch(socketId, "GROUP3")
    print xps.GroupJogParametersSet(socketId, "GROUP1", [0.05], [1.])
    print 'Jog Command sent'
    #print xps.GroupMoveAbsolute(socketId, "GROUP3", [10.])
    #print xps.GatheringStopAndSave(socketId)
    #data= xps.GatheringDataGet(socketId, 1)
    #print xps.GatheringConfigurationGet(socketId)

    xps.TCP_CloseSocket(socketId)
    print "connection to Controller finished."

if __name__ == '__main__':
    main()