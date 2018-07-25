
import random

math = ('pre-algebra', 'algebra 1', 'algebra 2', 'geometry', 'trigonometry', 'statistics', 'probability', 'precalculus', 'calculus AB', 'calculus BC', 'differential equations', 'linear algebra', 'discrete mathematics')
easy = ('easy', 'uncomplicated', 'straightforward', 'effortless', 'simple', 'unchallenging', 'undemanding', 'elementary')

num_of_iterations = int(input("How many times do you want to hear the joke? (please enter a natural number) "))

#What an unnamed student said for a geometry problem (s)he answered. Later, (s)he realized (s)he was incorrect. :)
for i in range(num_of_iterations):
    print('That '+(random.choice(math))+' problem was so '+(random.choice(easy))+'!')

input()
