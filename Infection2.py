import numpy as np
import random as rand
import math

q = input("Enter q value (0 - 1) or negative to exit: ") # probability to not contract virus
randOn = input("Enter 1 to enable randomness or any other number to disable: ")
ctr = 0
num = input("Enter number of simulations: ")
N = input("Enter Population number: ")
totDays = 0
total_Infections = 0
total_NonInfections = 0

while q > 0 and q < 1 and ctr < num:
	#N = 10000 # population number
	n = 0 # days
	In = 1 # infected at time n
	Sn = N - In # susceptible at time n
	Rn = 0 # recovered at time n
	randTag = ""

	print('\n{0:3s}| {1:9s} | {2:12s} | {3:9s} |     {4:10s}\n-----------------------------------------------------'.
	format("n", 'Infected',"Susceptible", "Recovered","Q"))
	print('{0:0d} {1:10d} {2:13d} {3:15d} {4:10f}'.format(n, In, Sn, Rn, q))
	while In > 0: # while there are infected

		# randomness component if rand is enabled
		if randOn == 1:
			if rand.random() < .49: # random chance to have effect
				if rand.random() < .49: # chance to be positive or neg effect
					r = -rand.uniform(0, q)
				else:
					r = rand.uniform(0, 1 - q)
				q += r
				randTag = 'rand'

		Pn = (1 - (q ** In)) # probability to become infected
		Rn = int(math.ceil(Rn + In)) # round up
		In = int(math.ceil(Sn * Pn)) # round up
		n += 1 # increment day
		Sn = Sn - In # set new susceptible pop.
		print('{0:0d} {1:10d} {2:13d} {3:15d} {4:10f} {5:4s}'.format(n, In, Sn, Rn, q, randTag))
	if(Sn == 0):
		total_Infections+=1
	else:
		total_NonInfections+=1
	ctr += 1
	totDays+=n
print "Total Infections: {0:5d}, Non Infections: {1:5d}, Average Days for Full Infection: {2:3f}".format(total_Infections, total_NonInfections, totDays/num)
	#q = input("\nEnter q value (0 - 1) or negative to exit: ") # probability to not contract virus
