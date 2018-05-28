from ProcessQueue import *
from Process import *
import ProcessGenorator
from Processor import *
import random


#format: [min,max]
length=[4,10]
interarrival=[3,6]
allowancetime=1
quantum=3
contextswitch=1
number_processes=500



#Queue for modified processor (With allowance)
queuem = ProcessQueue()
#Queue for regular processor (Without allowance)
queuer = ProcessQueue()
#Modified processor Q:2 CS:2 AT:1
modified = Processor(quantum,contextswitch,allowancetime)
#Regular processor Q:2 CS:2 AT:0
regular  = Processor(quantum,contextswitch)

#Attach the processor with the q
modified.attachQueue(queuem)
regular.attachQueue(queuer)

#counter for arrival time, when it equals 0 a new process arrives
next=interarrival[0]

#Add the same initial process
p=ProcessGenorator.generatenew(length[0],length[1])
queuem.recieve(p,modified.currtime)
queuer.recieve(p,regular.currtime)

while len(queuer.finished)<number_processes:
    #Perform 1 action for 1 clock tick, a tick is the time unit
    modified.tick()
    regular.tick()
    next-=1
    #if it is time to add a new process generate it, give it to both queues, and decide another interarrival
    if next<=0:
        proc=ProcessGenorator.generatenew(length[0],length[1])
        queuem.recieve(proc,modified.currtime)
        queuer.recieve(proc, modified.currtime)
        next=int(random.uniform(interarrival[0],interarrival[1]))


print('Modified: '+str(modified.getsummary()))
print('Regular:  '+str(regular.getsummary()))


