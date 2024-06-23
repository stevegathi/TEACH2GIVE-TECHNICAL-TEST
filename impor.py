import random
def rollDice():
    roll = random.randint(1,100)
    if roll ==100:
       print (roll,"roll was 100, you lose. what are the odds? play again!")
       return False
    elif 100 > roll >=50:
         print(roll, "roll was 51-99, you win! pretty lights flash(play more!)")
         return True
def simple_bettor (funds, intial_wager, wager_count):
    value=funds
    wager= intial_wager
    currentwager = 0
    while currentwager < wager_count:
          if rollDice():
             value += wager
          else:
              value -= wager
          currentwager += 1
          print ('Funds:' , value)
simple_bettor(10000, 100, 100)