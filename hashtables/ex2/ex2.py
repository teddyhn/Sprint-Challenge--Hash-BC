#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for k in tickets:
        hash_table_insert(hashtable, k.source, k.destination)
    
    for x in range(length - 1):
        if x == 0:
            route[x] = hash_table_retrieve(hashtable, "NONE")
        else:
            route[x] = hash_table_retrieve(hashtable, route[x - 1])

    return [i for i in route if i]