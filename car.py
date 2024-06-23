import simpy

def car(env):
    while True:
        print(f"Start parking at {env.now}")
        parking_duration = 5
        yield env.timeout(parking_duration)
        print(f"Start driving at {env.now}")
        trip_duration = 2
        yield env.timeout(trip_duration)

def customer(env, theater):
    # Logic for customer arrival and ticket buying
    ...

def theater_simulation(env):
    # Setup for theater, including resource for ticket counter
    ...
    while True:
        # Logic for customer arrival
        yield env.timeout(random_interval)

env = simpy.Environment()
env.process(theater_simulation(env))
env.run(until=simulation_time)
