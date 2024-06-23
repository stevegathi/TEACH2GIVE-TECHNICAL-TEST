import simpy
import random

# Define the car process
def car(env):
    while True:
        print(f"Start parking at {env.now}")
        parking_duration = 5
        yield env.timeout(parking_duration)
        print(f"Start driving at {env.now}")
        trip_duration = 2
        yield env.timeout(trip_duration)

# Define the theater simulation
def theater_simulation(env):
    # Initialize the theater resources, e.g., ticket counter
    ticket_counter = simpy.Resource(env, capacity=1)
    
    # Define the customer arrival process
    def customer_arrival():
        while True:
            yield env.timeout(random.expovariate(1.0 / 5.0))  # Adjust the arrival rate as needed
            env.process(customer(env, ticket_counter))

    env.process(customer_arrival())

# Define the customer process
def customer(env, ticket_counter):
    with ticket_counter.request() as request:
        yield request  # Request access to the ticket counter
        if len(ticket_counter.queue) == 0:  # Check if tickets are available
            print(f"Customer buys a ticket at {env.now}")
            # Simulate the time it takes to buy a ticket
            yield env.timeout(1)  # Adjust as needed
        else:
            print(f"Customer leaves the queue at {env.now} because tickets are sold out")

# Create the SimPy environment and start the simulation
env = simpy.Environment()
env.process(car(env))
env.process(theater_simulation(env))
env.run(until=50)  # Adjust the simulation time as needed
