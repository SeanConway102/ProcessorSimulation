import copy

'''
    Processor object: 
        CurrentTime  - Current time of the processor processing the queue
        Items        - Current active processes
        Finished     - List of all finished processes
        PriorityFunc - Function to be used to prioritize the functions

    Methods/Functions
        Constructor     - Create a blank queue
        Peek            - Look at the first process 
        Consume         - Take the first process out
        Add             - Add process directly to queue
        Addfinished     - Add process directly to finished
        Recieve         - Add copy  of process directly to queue
        Show            - Display queue
        Showfinished    - Display finished
        Settime         - Set current time from the processor
        SetPriorityFunc - Set the priority function to use
        Getpriority     - get the priority of a specific process
        defaultpriority - All priorities are 1 
        VRRPP           - algorithm from "Varying Response Ratio Priority"
                            Amit Pandey, Andargachew Mekonnen
        Sortbypriority  - sort the list by the PriorityFunc
'''


class ProcessQueue():
    currtime=0
    items=[]
    finished=[]
    priorityfunc=None
    def __init__(self):
        self.items=[]
        self.finished=[]
        self.priorityfunc=self.defaultpriority
    def peek(self):
        if len(self.items)>0:
            return self.items[0]
    def consume(self):
        if len(self.items)>0:
            return self.items.pop(0)
    def add(self,process):
        self.items += [process]
    def addfinished(self,process):
        self.finished+=[process]
    def recieve(self,process,time):
        process.arrive(time)
        self.items+=[copy.copy(process)]
        self.sortbypriority()
    def show(self):
        for process in self.items:
            print(str(process.pid) + ':\t' +str(process.length) + ' '+ str(self.getpriority(process)))
    def showfinished(self):
        for process in self.finished:
            print(str(process.pid) + ':\t' +str(process.length))
    def settime(self,time):
        self.currtime=time

    def setPriorityFunc(self,func):
        self.priorityfunc=func
    def getpriority(self,proc):
        return self.priorityfunc(proc)
    def defaultpriority(self,proc):
        return 1
    def VRRPP(self,process):
        if process.length<=0:
            return 0
        if process.arrival<0:
            return (1/process.initlen)
        else:
            return (1+(self.currtime-process.arrival))/(process.length)

    def sortbypriority(self):
        self.items.sort(key=self.getpriority,reverse=True)
