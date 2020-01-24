"""
Write a Python function that returns a list of keys in aDict with the value target. The list of keys you return should be sorted in increasing order. The keys and values in aDict are both integers. (If aDict does not contain the value target, you should return an empty list.)

This function takes in a dictionary and an integer and returns a list.
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here
    if not target in aDict.values():
        return []
    else:
        valueslist = []
        for i in aDict:
            if aDict[i] == target:
                valueslist.append(int(i))
        return sorted(valueslist)