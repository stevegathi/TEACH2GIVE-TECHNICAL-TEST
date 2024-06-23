from __future__ import annotations

import random
from typing import Dict, List, NamedTuple, Optional

import simpy

RANDOM_SEED = 42
TICKETS = 50  # Number of tickets per movie
SELLOUT_THRESHOLD = 2  # Fewer tickets than this is a sellout
SIM_TIME = 120  # Simulate until


def moviegoer(env, movie, num_tickets, theater):
   
    with theater.counter.request() as my_turn:
        # Wait until it's our turn or until the movie is sold out
        result = yield my_turn | theater.sold_out[movie]

        # Check if it's our turn or if movie is sold out
        if my_turn not in result:
            theater.num_renegers[movie] += 1
            return

        # Check if enough tickets left.
        if theater.available[movie] < num_tickets:
            # Moviegoer leaves after some discussion
            yield env.timeout(0.5)
            return

        # Buy tickets
        theater.available[movie] -= num_tickets
        if theater.available[movie] < SELLOUT_THRESHOLD:
            # Trigger the "sold out" event for the movie
            theater.sold_out[movie].succeed()
            theater.when_sold_out[movie] = env.now
            theater.available[movie] = 0
        yield env.timeout(1)


def customer_arrivals(env, theater):
    while True:
        yield env.timeout(random.expovariate(1 / 0.5))

        movie = random.choice(theater.movies)
        num_tickets = random.randint(1, 6)
        if theater.available[movie]:
            env.process(moviegoer(env, movie, num_tickets, theater))


class Theater(NamedTuple):
    counter: simpy.Resource
    movies: List[str]
    available: Dict[str, int]
    sold_out: Dict[str, simpy.Event]
    when_sold_out: Dict[str, Optional[float]]
    num_renegers: Dict[str, int]


# Setup and start the simulation
print('Movie renege')
random.seed(RANDOM_SEED)
env = simpy.Environment()

# Create movie theater
movies = ['Python Unchained', 'Kill Process', 'Pulp Implementation']
theater = Theater(
    counter=simpy.Resource(env, capacity=1),
    movies=movies,
    available={movie: TICKETS for movie in movies},
    sold_out={movie: env.event() for movie in movies},
    when_sold_out={movie: None for movie in movies},
    num_renegers={movie: 0 for movie in movies},
)

# Start process and run
env.process(customer_arrivals(env, theater))
env.run(until=SIM_TIME)

# Analysis/results
for movie in movies:
    if theater.sold_out[movie]:
        sellout_time = theater.when_sold_out[movie]
        num_renegers = theater.num_renegers[movie]
        print(
            f'Movie "{movie}" sold out {sellout_time:.1f} minutes '
            f'after ticket counter opening.'
        )
        print(f'  Number of people leaving queue when film sold out: {num_renegers}')