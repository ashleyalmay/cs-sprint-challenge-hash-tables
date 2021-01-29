def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    # set this to be empty 
    length = len(arrays)
    # for later check
    result = []
    #the answer will go in here 
    counter = 1
    # set the counter to keep track
    for the_lists in arrays:
    # go though the all lists
        for item in the_lists:
        #looking at the elements    
            if item not in cache:
                cache[item] = counter
            # dont add to counter 
            else:
                cache[item] += 1
            #add 
    for nums in cache:
        if cache[nums] == length:
            result.append(nums)
    #this sets it in the result  
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
