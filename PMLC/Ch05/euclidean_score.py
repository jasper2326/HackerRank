import json
import numpy as np


def euclidean_score(dataset, user1, user2):
    if user1 not in dataset:
        raise TypeError('User' + user1 + 'not in dataset')
    if user2 not in dataset:
        raise TypeError('User' + user2 + 'not in dataset')

    rated_by_both = {}
    for item in dataset[user1]:
        if item in dataset[user2]:
            rated_by_both[item] = 1

    if len(rated_by_both) == 0:
        return 0

    squared_difference = []
    for item in dataset[user1]:
        if item in dataset[user2]:
            squared_difference.append(np.square(dataset[user1][item] - dataset[user2][item]))

    return 1 / (1 + np.sqrt(np.sum(squared_difference)))


if __name__ == '__main__':
    file_name = '/Users/jasper/Desktop/HackerRank/PMLC/Ch05/movie_ratings.json'
    with open(file_name, 'r') as f:
        data = json.loads(f.read())
    user1 = 'John Carson'
    user2 = 'Michelle Peterson'

    print("Euclidean score:")
    print(round(euclidean_score(data, user1, user2), 3))
    