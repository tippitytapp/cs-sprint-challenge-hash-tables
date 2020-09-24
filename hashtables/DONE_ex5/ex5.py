# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    index = dict()
    paths = dict()
    result = list()
    # to get the folders
    for folder in files:
        # to extract just the folders
        folders = folder.split('/')
        # to get the file and link to folder
        for i, file in enumerate(folders):
            # cache the file to its folder
            index[folder] = file 
    # print(index)
    # map the files to their paths
    for i, v in index.items():
        paths[v] = i
    # print(paths)
    # run the queries
    for q in queries:
        # if the query is found in the paths
        if q in paths:
            # append the path to the results
            result.append(paths[q])
            # if their is no paths found, return an empty array
        if result == 0:
            return []
    # sort the results
    result.sort()
    # and then return them
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
