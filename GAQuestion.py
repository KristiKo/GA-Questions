#Question1
def user_in_experiment(user_id):
    if int(user_id) % 2 == 0:
        print('Matteo')
        return False
    else:
        print('Kristi')
        return True
user_in_experiment('5')


#Question2
POPULAR_RESTAURANTS = ['Laut', 'Rosa Mexicano', 'Ootoya', 'Dig Inn']
MY_List = ['Latte', 'Buritto', 'Fasolka', 'Chechevica', 'Stuffed Pepers', 'Laut']
def get_popular_restaurants(MY_List):
    for i in MY_List:
        if i in POPULAR_RESTAURANTS:
            print(i)
get_popular_restaurants(MY_List)

#Question3

from operator import itemgetter

restaurants = [
  {"name": "Ootoya", "rating": 8.0},
  {"name": "Chipotle", "rating": 6.6},
  {"name": "Burger&Lobster", "rating": 7.2},
  {"name": "Laut", "rating": 8.1}
]

sorted_restaurants = sorted(restaurants, key=itemgetter('rating'), reverse=True)

print(sorted_restaurants)

#Question 4

import itertools

for i in itertools.count():
    result = i^2 - 49
    result = -i^2 - 49
    if result == 0:
        print(result)
        break

#Question5
previousResult = 0
 
for i in itertools.count():
    result = (-i ^ 2) + (5 * i) + 7
    if result > previousResult:
        print(result)
    previousResult = result
    
