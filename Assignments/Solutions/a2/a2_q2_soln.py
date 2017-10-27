from collections import defaultdict
from itertools import combinations
import pprint


def reverse_transform_rating_matrix(dict_):
    transform = defaultdict(dict)
    for key in dict_:
        inner_dict = dict_[key]
        for key_ in inner_dict:
            transform[key_][key] = inner_dict[key_]

            ## Reverse transform can also be done first principles. defaultdict only makes it easier and shorter
            ## As an exercise, figure out what the following is doing using debug mode.
            #  transform = {}
            #  for outer_key, outer_value in dict_.items():
            #	  for inner_key, inner_value in outer_value.items():
            #	      try:
            #	          transform[inner_key][outer_key] = inner_value
            #  		  except KeyError:
            #     	      transform[inner_key] = {outer_key: inner_value}

    return dict(transform)


def compute_pairwise_rating_dissimilarity(dict1, dict2):
    common_keys = set(dict1.keys()).intersection(set(dict2.keys()))
    ## you can use for loops to extract common_keys
    # common_keys = []
    # for key1 in dict1.keys():
    #     if key1 in dict2:
    #	      common_keys.append(key1)
    abs_rating_diff_list = [abs(dict1[key] - dict2[key]) for key in common_keys]
    avg_abs_rating_diff = sum(abs_rating_diff_list) / len(common_keys)
    return avg_abs_rating_diff


def find_most_similar_pair(rating_matrix, by=None):
    pairs = combinations(rating_matrix.keys(), 2)
    ## pairwise combinations can also be obtained from first principles as follows:
    ## compare the 2 methods as an exercise
    # pairs = []
    # for idx, key1 in enumerate(rating_matrix.keys()):
    # 	 for key2 in keys[idx+1: ]:
    # 		 pairs.append((key1, key2))
    dissimilarity = []
    for key1, key2 in pairs:
        pair_dissimilarity = compute_pairwise_rating_dissimilarity(rating_matrix[key1], rating_matrix[key2])
        dissimilarity.append([(key1, key2), pair_dissimilarity])
    # dissimilarity is a list like: [[(user1, user2), 1.3], [(user1, user3), 0.4], ...]
    # so that, dissimilarity[0] = [('user1', 'user2'), 1.3];
    # 		   dissimilarity[0][1] = 1.3
    # To sort this complex list by the dissimilarity value, we have use lambda
    dissimilarity.sort(key=lambda y: y[1])
    print('\nPairwise %s dissimilarity: ' % by)
    pprint.pprint(dissimilarity)
    return dissimilarity[0]  # return the least dissimilar, or most similar pair (1st element after sorting)


if __name__ == "__main__":
    user_item_rating = {
        'user1': {'item1': 2.5, 'item2': 3.5, 'item3': 3.0,
                  'item4': 3.5, 'item5': 2.5, 'item6': 3.0},
        'user2': {'item1': 3.0, 'item2': 3.5, 'item3': 1.5,
                  'item4': 5.0, 'item5': 3.5, 'item6': 3.0},
        'user3': {'item1': 2.5, 'item2': 3.0, 'item4': 3.5,
                  'item6': 4.0},
        'user4': {'item2': 3.5, 'item3': 3.0, 'item4': 4.0,
                  'item5': 2.5, 'item6': 4.5},
        'user5': {'item1': 3.0, 'item2': 4.0, 'item3': 2.0,
                  'item4': 3.0, 'item5': 2.0, 'item6': 3.0},
        'user6': {'item1': 3.0, 'item2': 4.0, 'item4': 5.0,
                  'item5': 3.5, 'item6': 3.0},
        'user7': {'item2': 4.5, 'item4': 4.0, 'item5': 1.0}
    }

    item_user_rating = reverse_transform_rating_matrix(user_item_rating)
    print('Original dict: ')
    pprint.pprint(user_item_rating)
    print('\nReversed dict: ')
    pprint.pprint(item_user_rating)
    print('Most similar users: ', find_most_similar_pair(user_item_rating, by='user'))
    print('Most similar items: ', find_most_similar_pair(item_user_rating, by='item'))