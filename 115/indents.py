def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    count = 0
    for letter in text:
        if letter == " ":
            count+=1
        else:
            break
    return count
        
