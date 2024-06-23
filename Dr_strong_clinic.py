import simpy
import random

# Parameters
NUM_DENTISTS = 2
MEAN_ARRIVAL_TIME = 10
MEAN_SERVICE_TIME = 20
SIMULATION_TIME = 480 # 8 hours

# Statistics
wait_times = []

class DentalClinic(object):
    def __init__(self, env):
        self.env = env
        self.dentist = simpy.Resource(env, NUM_DENTISTS)
    
    def dental_service(self, patient):
        """Simulate the dental service process."""
        yield self.env.timeout(random.expovariate(1.0 / MEAN_SERVICE_TIME))

def patient(env, name, clinic):
    """Patient process."""
    arrival_time = env.now
    print(f'{name} arrives at the clinic at {arrival_time:.2f}')
    with clinic.dentist.request() as request:
        yield request
        
        wait = env.now - arrival_time
        wait_times.append(wait)
        print(f'{name} waited for {wait:.2f} minutes')
        
        yield env.process(clinic.dental_service(name))
        print(f'{name} leaves the clinic at {env.now:.2f}')

def setup(env):
    """Setup the simulation."""
    clinic = DentalClinic(env)
    
    # Start with some patients
    for i in range(2):
        env.process(patient(env, f'Patient {i}', clinic))
    
    # Generate more patients while the simulation is running
    while True:
        yield env.timeout(random.expovariate(1.0 / MEAN_ARRIVAL_TIME))
        i += 1
        env.process(patient(env, f'Patient {i}', clinic))

# Setup and start the simulation
print('Dr. Strong Dental Clinic')
random.seed(42) # for reproducible results
env = simpy.Environment()
env.process(setup(env))
env.run(until=SIMULATION_TIME)

# Analysis
average_wait_time = sum(wait_times) / len(wait_times)
print(f'\nAverage wait time: {average_wait_time:.2f} minutes')
print(f'Patients served: {len(wait_times)}')
