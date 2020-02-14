#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for k in weights:
        hash_table_insert(ht, k, weights.index(k))

    indices = None

    for k in weights:
        if (limit - k == k):
            index = weights.index(k)
            indices = (weights.index(k, index + 1), hash_table_retrieve(ht, limit - k))
        if (hash_table_retrieve(ht, limit - k)):
            indices = (hash_table_retrieve(ht, k), hash_table_retrieve(ht, limit - k))

    if indices is not None:
        print(indices)
        return indices

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
