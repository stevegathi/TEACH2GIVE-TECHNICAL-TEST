
import random


def toss():
    return random.choice(['Heads', 'Tails'])  
def main():
  n_tosses = int(input("Enter the number of tosses: "))
  heads_count = 0
  tails_count = 0
  for _i in range(n_tosses):

    results = toss ()
    if results== 'Heads':
      heads_count += 1
    else:
      tails_count += 1
  print(f"Results after {n_tosses} tosses")
  print( f"Heads: {heads_count} Tails: {tails_count}")
if __name__== "__main__":
   main()
