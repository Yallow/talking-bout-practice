import random

def random_walker(n):
    """input a number of blocks to walk and return how far away from home you end up """
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        x+=dx
        y+=dy
    return (x,y)

number_of_walks = 10000
for walk_len in range(1, 31):
    no_transport = 0 # walk home if you are less than or equal to 4 blocks away
    for i in range(number_of_walks):
        (x, y) = random_walker(walk_len)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport+=1
    no_transport_perc = (float(no_transport) / number_of_walks) * 100
    print("Percentage of no transport walks at %s: %f" % (walk_len, no_transport_perc))   