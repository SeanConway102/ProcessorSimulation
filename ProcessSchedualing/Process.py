
'''
    Process object:
        PID    - Process ID
        Length  - Current length of project
        Arrival - When the process arrived
        Start   - Start of execution(first run)
        End     - When the process finished computing
        InitLen - How long the process was when it arrived
    Methods/Functions
        Constructor - Take the PID and length
        Run         - Run for one interval
        Active      - Check if this process is still active/incomplete
        Getinfo     - Return turnaround, totalwait, and initialwait for analysis
        Arrive      - Signal the process has arrived in the processor
'''
class Process:
    pid=0
    length=0
    arrival=-1
    start=-1
    end=-1
    initlen=-1
    def __init__(self,pid,length):
        self.pid=pid
        self.length=length
        self.initlen=length
    def run(self,currtime):
        if self.length>0:
            if self.start<0:
                self.start=currtime
            self.length-=1
            if self.length==0:
                self.end= currtime+1
            return True
        return False
    def active(self):
        if self.length>0:
            return True
        return False
    def getinfo(self):
        dict={}
        if self.active()==False:
            dict['turnaround']=self.end-self.start
            dict['totalwait']=self.end-self.arrival-self.initlen
            dict['initwait']=self.start-self.arrival
        return dict
    def arrive(self,time):
        self.arrival=time