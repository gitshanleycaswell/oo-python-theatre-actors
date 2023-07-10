import ipdb
from lib import *

# Test your code below...

actor1 = Actor("Michelle Pfeiffer")
actor2 = Actor("Margot Robbie")
actor3 = Actor("Jennifer Lawrence")

r1 = Role("Harley Quinn")
r2 = Role("Catwoman")
r3 = Role("Superwoman")

audition1 = Audition("Santa Monica", False, r1, actor2)
audition2 = Audition("North Hollywood", False, r2, actor1)
audition3 = Audition("Hollywood", False, r3, actor2)
audition4 = Audition("Downtown", False, r2, actor3)



# the below line allows us to stop & try stuff!
ipdb.set_trace()