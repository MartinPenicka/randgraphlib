import os, sys

def recursive_contains(array, value):
    '''
    Search given list of objects (nested lists, list of nested lists ...) if contains given value
    '''
    for item in array:
        if str(type(item)) == '<type \'list\'>':
            if recursive_contains(item, value) == True:
                return True
        else:       
            if item == value:
                return True
            
    return False

def contains_same_value(list1, list2):
    '''
    If list1 and list2 contains at least one same value, returns true
    '''
    
    for item in list1:
        if item in list2:
            return True
    return False

def mkdir(path):
    '''
    Checks if directory exists. If not, tries to create. If it is not possible to create dir (insuficient rights, etc.), returns message to stderr.
    '''
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except:
            sys.stderr.write('utiltools:: Error -> cannot create directory')