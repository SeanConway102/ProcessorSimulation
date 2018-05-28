
import random
import ProcessGenorator
import time
import os

class Test():
    processor1=None
    processor2=None
    processnumber=0
    length = []
    interarrival = []
    lastrun=[]
    name=''

    def __init__(self,name,processor1,processor2,length,interarrival,processnumber=1000):
        self.name=name
        self.processor1=processor1
        self.processor2=processor2
        self.processnumber=processnumber
        self.length=length
        self.interarrival=interarrival
    def run(self):
        next=int(random.uniform(self.interarrival[0], self.interarrival[1]))
        queue1=self.processor1.pq
        queue2 = self.processor2.pq
        p = ProcessGenorator.generatenew(self.length[0], self.length[1])
        queue1.recieve(p, self.processor1.currtime)
        queue2.recieve(p, self.processor2.currtime)
        while (len(queue1.finished) < self.processnumber) or (len(queue2.finished) < self.processnumber):
            # Perform 1 action for 1 clock tick, a tick is the time unit
            if (len(queue1.finished) < self.processnumber):
                self.processor1.tick()
            if (len(queue2.finished) < self.processnumber):
                self.processor2.tick()
            next -= 1
            # if it is time to add a new process generate it, give it to both queues, and decide another interarrival
            if next <= 0:
                proc = ProcessGenorator.generatenew(self.length[0], self.length[1])
                if (len(queue1.finished) < self.processnumber):
                    queue1.recieve(proc, self.processor1.currtime)
                if (len(queue2.finished) < self.processnumber):
                    queue2.recieve(proc, self.processor2.currtime)
                next = int(random.uniform(self.interarrival[0], self.interarrival[1]))
        self.lastrun= [self.processor1.getsummary(),self.processor2.getsummary()]
        return self.lastrun
    def getlastrun(self):
        return self.lastrun
    def export(self,loc,p1Name,p2Name):
        label = self.name +str(int(time.time()%(60*60*24)))
        if os.path.isdir(loc)==False:
            os.mkdir(loc)
        if self.lastrun==[]:
            self.run()
        print(self.lastrun)
        with open(loc+label+'.csv','w') as f:
            f.write(self.name + '\n')
            f.write(','+ p1Name   + ',' + p2Name + ',\n')
            f.write('Finished,'   + str(self.lastrun[0]['finnished']) + ',' + str(self.lastrun[1]['finnished']) + ',\n')
            f.write('Left,'       + str(self.lastrun[0]['left'])      + ',' + str(self.lastrun[1]['left']) + ',\n')
            f.write('TotalCS,'    + str(self.lastrun[0]['totalcs'])   + ',' + str(self.lastrun[1]['totalcs']) + ',\n')
            f.write('Turnaround,' + str(self.lastrun[0]['turnaround']) + ',' + str(self.lastrun[1]['turnaround']) + ',\n')
            f.write('Initwait,'   + str(self.lastrun[0]['initwait'])  + ',' + str(self.lastrun[1]['initwait']) + ',\n')
            f.write('TotalWait,'  + str(self.lastrun[0]['totalwait']) + ',' + str(self.lastrun[1]['totalwait']) + ',\n')
            f.write('Time,'       + str(self.lastrun[0]['time'])      + ',' + str(self.lastrun[1]['time']) + ',\n')

