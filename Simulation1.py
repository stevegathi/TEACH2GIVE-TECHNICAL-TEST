import random

#Define a class for the random population
class Population:
	# initialize the population with a given size
	def__init__(self, size, infections_rate):
		self.size = size
		self.infection_rate = infection_rate
		self.healthy = size
		self.infected = 0
		self.recovered = 0
	
	# function to model the spread of disease within the population
	def spread_disease(self):

		# calculate the number of new infection
		new_infections = self.infection_rate * self.healthy

		# update the number of healthy, infected and the recovered individual
		self.healthy -= new_infections
		self.infected = new_infections

		# calculate the number of individual who recovered
		recoveries = self.infected * random.uniform(0.1, 0.015)

		# calculate the number of individual who recovered
		self.infected -= recoveries
		self.recovered += recoveries

# initialize the population with 1000 individuals and infection rate 0.01
population = Population(1000, 0.01)

# simulate the spread of the disease for 100 times steps
for i in range(100):
	population.spread_disease()
        
#print the final numbers
print('Health: ', population.heathy)
print('Infected: ', population.infected)
print('Recovered: 'population.recovered)
	