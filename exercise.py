import random
d1= random.randint(1, 7)
d2= random.randint(1, 7)
if d1 + d2 == 7:
    print("Winner")
elif d1 + d2 == 11:
    print("Winner")
elif d1 + d2 == 2:
    print("Loser")
elif d1 + d2 == 3:
    print("Loser")
elif d1 + d2 == 12:
    print("Loser")
else:
    print("Roll Again!")