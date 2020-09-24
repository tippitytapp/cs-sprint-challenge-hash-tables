#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    flights = {}
    # allocate enough space for amount of tickets you have
    route = [None] * length
    # add the tickets to the flights dictionary
    for i in range(length):
        cur_flight = tickets[i]
        # We can hash each ticket such that the starting location is the key and
        # the destination is the value. 
        flights[cur_flight.source] = cur_flight.destination
    # create a starting point
    route[0] = flights["NONE"]
    # print(route[0])
    # Then, when constructing the entire
    # route, the `i`th location in the route can be found by checking the
    # hash table for the `i-1`th location.
    route[1] = flights[route[0]]
    # print(route[1])
    if length > 2:
        for i in range(2, length):
            # Then, when constructing the entire
            # route, the `i`th location in the route can be found by checking the
            # hash table for the `i-1`th location.
            route[i] = flights[route[i-1]]
    return route
