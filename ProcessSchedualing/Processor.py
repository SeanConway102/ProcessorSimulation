from ProcessQueue import *
from Process import *
from ProcessGenorator import *

'''
    Processor object: 
        PQ    - ProcessQueue to process from
        Q     - Quantum Time
        CS    - Context switch time
        AT    - Allowance time
        CurrQ - What interval of the current quantum the processor is on
        CurrCS- What interval of the current context switch the processor is on
        Currtime - Current time of the processor
        Numcs - Total number of context switches preformed
    Methods/Functions
        Constructor - Take the Quantum time, Context Switch time, Allowance time default 0
        AttachQueue - Attach a process queue to process from
        Tick        - Process or switch for one time unit
        Process     - Process for one time unit
        Switch      - Switch for one time unit
        Getsummary  - Get current summary 
'''
class Processor():
    pq=None
    q=0
    cs=0
    at=0
    currq=0
    currcs=0
    currtime=0
    numcs=0
    def __init__(self,q=0,cs=0,at=0):
        self.pq = None
        self.q=q
        self.currq=q
        self.cs=cs
        self.at=at
        self.currtime=0
        self.currcs = 0
        self.numcs = 0
    def attachQueue(self,queue):
        self.pq=queue
        queue.settime(self.currtime)
    def tick(self):
        if self.currq>=1:
            #print('Processing')
            self.process()
        else:
            if self.currcs>=1:
                #print('Switching')
                self.switch()
        self.currtime+=1
        self.pq.settime(self.currtime)
    def process(self):
        p=self.pq.peek()
        if p != None:
            p.run(self.currtime)
            if p.length <= self.at:
                self.currq = p.length+1
            #print(str(p.pid)+': Processing '+str(p.length))
        self.currq-=1
        if self.currq<=0 or p ==None or p.length==0:
            if p != None:
                if p.length<=0:
                    self.pq.consume()
                    self.pq.addfinished(p)
            self.currq=0
            self.currcs=self.cs
    def switch(self):
        self.currcs -= 1
        if self.currcs<=0:
            self.numcs+=1
            self.currq=self.q
            p = self.pq.consume()
            if p != None:
                if p.active():
                    self.pq.add(p)
                else:
                    self.pq.addfinished(p)
    def getsummary(self):
        summ={}
        summ['finnished']=len(self.pq.finished)
        summ['left'] = len(self.pq.items)
        summ['totalcs'] = self.numcs
        info=[]
        for process in self.pq.finished:
            info+=[process.getinfo()]
        ta=0
        iw=0
        tw=0
        for i in info:
            ta+=i['turnaround']
            iw+=i['initwait']
            tw+=i['totalwait']
        total=len(self.pq.finished)
        summ['turnaround']=ta/total
        summ['initwait']=iw/total
        summ['totalwait']=tw/total
        summ['time']=self.currtime
        return summ