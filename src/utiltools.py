

def recursive_contains(array, value):
    '''
    Search given list of objects (list of lists, list of lists of lists ...) if contains given value
    '''
    for item in array:
        if str(type(item)) == '<type \'list\'>':
            if recursive_contains(item, value) == True:
                return True
        else:       
            if item == value:
                return True
            
    return False

if __name__ == '__main__':
    
    # Test recursive_contains()
    a = [1,2,3,4,5]
    b = [[1,2],[3,4],5]
    c = [[1,2,[3,[4]],5]]
    
    assert recursive_contains(a, 3) == True
    assert recursive_contains(b, 3) == True
    assert recursive_contains(c, 3) == True
    assert recursive_contains(c, 7) == False
    #TODO: Proper unittests for utiltools.py