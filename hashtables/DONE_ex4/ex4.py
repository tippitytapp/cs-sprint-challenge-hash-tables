def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # store the values of the positive numbers and their negative equivalents
    cache = dict()
    # store the results
    result = []
    # for the numbers in the array
    for v in a:
        # if there is a (v - v - v) AKA absolute value in the cache for v
        if cache.get(abs(v)):
            # add v to the results array
            result.append(abs(v))
        else:
            # if one doesn't exist, then add it to the cache for future uses
            cache[abs(v)] = v
    # return the result array        
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
