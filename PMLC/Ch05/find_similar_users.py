import json
import numpy as np

from PMLC.Ch05.pearson_score import pearson_score


def find_similar_users(dataset, user, num_users):
    if user not in dataset:
        raise TypeError('User ' + user + 'not present in the dataset')

    scores = np.array([[x, pearson_score(dataset, user, x)] for x in dataset if x != user])
    scores_sorted = np.argsort(scores[:, 1])
    scores_sorted_desc = scores_sorted[::-1]
    top_k = scores_sorted_desc[:num_users]
    return scores[top_k]


if __name__=='__main__':
    data_file = 'movie_ratings.json'

    with open(data_file, 'r') as f:
        data = json.loads(f.read())

    user = 'Michael Henry'
    print("\nUsers similar to " + user + ":\n")
    similar_users = find_similar_users(data, user, 3)
    print("User\t\t\tSimilarity score\n")
    for item in similar_users:
        print(item[0], '\t\t', round(float(item[1]), 2))