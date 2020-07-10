def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = dict()
    result = []
    # go through the arrays
    for i, v in enumerate(arrays):
        # go through the arrays in the arrays
        for w in v:
            # if the value is in the cache and the value is greater than 0
            if (cache.get(w) is not None) and (i > 0):
                # increment count
                cache[w] += 1
            # if the value is not in teh cache and the count is 0
            elif (cache.get(w) is None) and (i == 0):
                # establish cache at 1
                cache[w] = 1
            # if the value is already not found in one of the arrays
            else:
                # continue because its already not an intersection
                continue
    # for all the counts in the cache
    for results in cache:
        # if the count is the same as the length of the arrays
        if cache[results] == len(arrays):
            # add it to the results
            result.append(results)
    # return the results
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
