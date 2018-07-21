import random

MATH = ('pre-algebra', 'algebra 1', 'algebra 2', 'geometry', 'trigonometry', 'statistics', 'probability', 'precalculus', 'calculus AB', 'calculus BC', 'differential equations', 'linear algebra', 'discrete mathematics')
EZ = ('easy', 'uncomplicated', 'straightforward', 'effortless', 'simple', 'unchallenging', 'undemanding', 'elementary')

print('That', (random.choice(MATH)), 'problem was so', (random.choice(EZ)), '!')
