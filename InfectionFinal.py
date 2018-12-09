import numpy as np
import random as rand
import matplotlib.pyplot as plt

# input validation helper function
def get_input(prompt, type_ = None, min = None, max = None):
    if min is not None and max is not None and max < min:
        raise ValueError("Min must be less than or equal to max.")
    while True:
        input = input(prompt)
        if type_ is not None:
            try:
                input = type_(input)
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        if max is not None and input > max:
            print("Input must be less than or equal to {0}.".format(max))
        elif min is not None and input < min:
            print("Input must be greater than or equal to {0}.".format(min))
        else:
            return input

opt = get_input("Enter 1 to enable realism or 0 for original: ", type_ = int, min = 0, max = 1)
p = get_input("Enter probability of transmission: ", type_ = float, min = 0, max = 1)
n = get_input("Enter population size: ", type_ = int, min = 1)
I0 = get_input("Enter initial infected: ", type_ = int, min = 0, max = N)
RP = get_input("Enter recovery period: ", type_ = int, min = 1)
if (opt == 1):
	niPrompt = "Enter average number of contacts: "
else:
	niPrompt = "Enter number of contacts: "
Ni = get_input(niPrompt, int)
trials = get_input("Enter number of trials: ", int)

In = np.zeros(RP, dtype=int) # infected array size RP
durations, infections = [], [] # arrays for tracking durations and infections for each trial

#print('\n{0:5s}| {1:12s} | {2:12s} | {3:9s} | {4:10s}\n---------------------------------------------------------------'.
#format("Day", 'New Infected', "Total Infected", "Susceptible", "Recovered"))
#print('{0:2d} {1:13d} {2:13d} {3:15d} {4:12d}'.format(day, In[0], I, S, R))
for i in range(trials):
	In[0] = I = I0 # initial infected and total infected
	S = n - In[0] # initial susceptible
	R = 0 # initial recovered
	day = 0 # days for infection
	while I > 0: # while there are infected
		if (opt == 1): # if realistic sim enabled
			Nir = rand.randint(0, (2 * Ni) + 1) # contacts are random int from 0 - 2Ni
		else:
			Nir = Ni # contacts equals input
		q = 1 - (1 - ((p * I) / (n - 1))) ** Nir # probability to become infected
		In = np.roll(In, 1) # shift infected array by 1
		R = R + In[0] # add the "wrapped" value to recovered
		In[0] = int(np.random.binomial(S, q, 1)) # calculate newly infected
		I = sum(In) # total of current infected
		S = n - I - R # set new susceptible pop.
		day += 1 # increment day
	#	print('{0:2d} {1:13d} {2:13d} {3:15d} {4:12d}'.format(day, In[0], I, S, R))
	#print "Infections: {0:5d}, Days for Full Infection: {1:3d}".format(R, day)
	durations.append(day) # add day to durations array
	infections.append(R) # add total infected to infections array

f1 = plt.figure(1)
plt.hist(durations, bins=30)
plt.title('durations Frequency in {0:d} trials\nVariance: {1:3f}, Mean: {2:3f}'.format(trials, np.var(durations), sum(durations) / float(trials)))
plt.ylabel('Frequency');
plt.xlabel('durations of Epidemic');

f2 = plt.figure(2)
plt.hist(infections, bins=30)
plt.title('Total Infections Frequency in {0:d} trials\nVariance: {1:3f}, Mean: {2:3f}'.format(trials, np.var(infections), sum(infections) / float(trials)))
plt.ylabel('Frequency');
plt.xlabel('Total Infections');
plt.show()
