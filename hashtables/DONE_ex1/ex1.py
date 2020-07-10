def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # cache
    cache = {}
    # needed for duplicate values
    dup = False
    # cache to store duplicate values
    dups_cache = {}

    for i in range(0, length):
        # w is the current weight
        w = weights[i]
        cache[w] = i
        # left is the weight left to hit target
        left = limit - w
        # if the left over weight is in the cache
        if left in cache:
            if w > left:
                # return the higher value on the left and larger value on the right
                return (i, cache[left])
            elif w < left:
                # return the higher value on the left and the larger value on the right
                return (i, cache[left])
            # duplicate values
            elif left == w:  # if a duplicate value is found
                if dup is False:
                    # set dup to True and add to the dups_cache
                    dup = True
                    dups_cache[w] = i
                elif dup is True:
                    # return the values, no need to check which is larger
                    return (i, dups_cache[w])
    # if a solution cant find a pair that adds up to the limit, return none
    return None
