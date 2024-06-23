import simpy
import random

# Parameters
NUM_DENTISTS = 2
NUM_ADMIN_STAFF = 1
MEAN_ARRIVAL_TIME = 10
MEAN_REGISTRATION_TIME = 5
SERVICE_TIMES = {'check-up': 15, 'cleaning': 30, 'filling': 45}
SIMULATION_TIME = 480  # 8 hours

# Statistics
wait_times = []
service_times = []

class DentalClinic(object):
    def __init__(self, env):
        self.env = env
        # Use PriorityResource for dentists to manage priorities
        self.dentist = simpy.PriorityResource(env, NUM_DENTISTS)
        self.admin_staff = simpy.Resource(env, NUM_ADMIN_STAFF)
    
    def registration(self, patient):
        """Simulate the registration process."""
        yield self.env.timeout(random.expovariate(1.0 / MEAN_REGISTRATION_TIME))
    
    def dental_service(self, patient, service_type):
        """Simulate the dental service process."""
        yield self.env.timeout(SERVICE_TIMES[service_type])

def patient(env, name, clinic):
    """Patient process, including registration and dental service."""
    print(f'{name} arrives at the clinic at {env.now:.2f}')
    
    # Registration
    with clinic.admin_staff.request() as request:
        yield request
        yield env.process(clinic.registration(name))
    
    # Dental Service with priority
    priority = random.choice([0, 1])  # Priority 0 for emergencies, 1 for regular
    with clinic.dentist.request(priority=priority) as request:
        yield request
        service_type = random.choice(list(SERVICE_TIMES.keys()))
        print(f'{name} is undergoing {service_type} at {env.now:.2f}')
        yield env.process(clinic.dental_service(name, service_type))
        print(f'{name} completes {service_type} at {env.now:.2f}')

def setup(env):
    clinic = DentalClinic(env)
    
    for i in range(2):
        env.process(patient(env, f'Patient {i}', clinic))
    
    i = 2
    while True:
        yield env.timeout(random.expovariate(1.0 / MEAN_ARRIVAL_TIME))
        env.process(patient(env, f'Patient {i}', clinic))
        i += 1

# Setup and start the simulation
print('Dr. Strong Dental Clinic Simulation')
random.seed(42)  # for reproducible results
env = simpy.Environment()
env.process(setup(env))
env.run(until=SIMULATION_TIME)
