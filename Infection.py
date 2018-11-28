import numpy as np

N = 100 # population number
n = 0 # number of days
b = 1 # number bitten by coyote

# Initial Distribution of population
S_0 = (N - b) # of susceptible population
I_0 = b # of infected population
R_0 = 0 # of recovered population

# the probability that a susceptible individual does not contract the virus from
# a given infective individual.
q = .75

I_n = I_0 # infected at time n

# Transition probability matrix
P = np.array([
	[q ** I_n, 0, 0],
	[1 - (q ** I_n), 0, 0],
	[0, 1, 1]
	])

# number of days in the simulation
# Will run the process for num_days total generations,
# X_0, X_1, ..., X_{num_days}
num_days = 10

# initialize a matrix to hold the
# probability distributions
X = np.zeros((num_days,3))

# the initial probability distribution
X[0] = np.array([S_0, I_0, R_0])

# obtain the probability distributions on
# $S = \{B, W\}$ corresponding to
# X_1, X_2, ...,  X_{num_days}
np.set_printoptions(suppress=True)
for i in range(1, np.size(X, 0)):
	X[i] = P.dot(X[i-1]).round()
	I_n = X[i]
	I_n = I_n[2]
	print("I_n: ", I_n)
	P = np.array([
		[(q ** I_n), 0, 0],
		[(1 - (q ** I_n)), 0, 0],
		[0, 1, 1]
		])
	print("P: ", P)

# print the results.
# The ith row of $X$ is the probability mass function
# on $S = \{B, W\}$ corresponding to $X_i$.
print 'X = \n', X
