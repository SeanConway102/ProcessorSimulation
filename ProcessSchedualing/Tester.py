

from Test import *
from ProcessGenorator import *
from ProcessQueue import *
from Processor import *

loc='c://results/'

p1 = Processor(2,1,2)
q1 = ProcessQueue()
p1.attachQueue(q1)

p2 = Processor(2,1)
q2 = ProcessQueue()
p2.attachQueue(q2)

test=Test('High Arrival Rate - Small Process Size',p1,p2,[2,5],[2,4],500)
t=test.run()
test.export(loc,'Modified','Regular')
q1=ProcessQueue()
p1.attachQueue(q1)
q2=ProcessQueue()
p2.attachQueue(q2)

test=Test('High Arrival Rate - Large Process Size',p1,p2,[4,10],[2,4],500)
t=test.run()
test.export(loc,'Modified','Regular')
q1=ProcessQueue()
p1.attachQueue(q1)
q2=ProcessQueue()
p2.attachQueue(q2)

test=Test('Slow Arrival Rate - Large Process Size',p1,p2,[4,10],[4,8],500)
t=test.run()
test.export(loc,'Modified','Regular')
q1=ProcessQueue()
p1.attachQueue(q1)
q2=ProcessQueue()
p2.attachQueue(q2)

test=Test('Slow Arrival Rate - Small Process Size',p1,p2,[2,5],[4,8],500)
t=test.run()
test.export(loc,'Modified','Regular')

print(t)