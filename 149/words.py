def sort_words_case_insensitively(li):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    return sorted(li, key=lambda x: (x[0].isdigit(), str(x).lower()))