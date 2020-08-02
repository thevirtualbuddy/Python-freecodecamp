import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.Originalcontents = dict()
        self.contents = []
        for key, value in kwargs.items(): 
            self.Originalcontents[key]=value
            for i in range(value):
                self.contents.append(key)
    
    def draw(self, no_of_balls):
        if no_of_balls > len(self.contents):
            return self.contents
        else:
            i = 0
            ballsDrawn = []
            while i<no_of_balls:
                a = random.choice(self.contents)
                ballsDrawn.append(a)
                self.contents.remove(a)
                i = i+1
            return ballsDrawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    # Note to self:
    # Expected balls is a dictionary
    # num_balls_drawn is a number/integer
    # num_experiments is also a number indicating no of expt

    probability = 0
    for i in range(num_experiments):

        #Making a deep copy of the hat, so the original hat is not hampered
        hat_clone = copy.deepcopy(hat)

        #Obtaining num_balls no of drawn balls from the hat 
        drawnBalls = hat_clone.draw(num_balls_drawn)

        #Converting the obtained drawnballs to dictionary
        drawnBalls_dict = {ball : drawnBalls.count(ball) for ball in set(drawnBalls)}

        #Comparing the drawn balls we obtained with expected_balls
        found = True
        for key, value in expected_balls.items():
            if (key not in drawnBalls_dict) or (drawnBalls_dict[key]<expected_balls[key]):
                found = False
                break
                
        if found:
            probability+=1
    return probability/num_experiments


    

