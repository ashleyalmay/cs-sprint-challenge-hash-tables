def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
# cache and result are both empty 
    for i in a:
        x = -i
        #go though the list and set x to neg 
        if cache.get(x,False):
            if i >= 0:
                result.append(i)
        #set the int to postive and put it in i
            else:
                result.append(-i)
        cache[i] = True
        # else neg and the cache will always be true 
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
