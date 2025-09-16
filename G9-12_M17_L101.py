# Activity 1 Coin CDF

import scipy.stats as stats

prob = 1 - stats.binom.cdf(6, 10, 0.5)
print("the probability of getting more than 6 heads in 10 coin flips is :", prob)

print("*************************************************************************8")

# Activity2 Rain exoectation 

prob1 = stats.poisson.pmf(6, 10)
print("probability of raining for exactly 6 days :",prob1)

prob2 = stats.poisson.pmf(12, 10)+stats.poisson.pmf(13, 10) + stats.poisson.pmf(14,10)
print("probability of raining for 12-14 days :",prob2)

print("*************************************************************************8")

#Activity 3  Calls Poison

prob1 = 1-stats.poisson.cdf(20, 15)
print(prob1)

prob2 = stats.poisson.cdf(21, 15)-stats.poisson.cdf(16, 15)
print(prob2)


