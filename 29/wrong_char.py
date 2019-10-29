from collections import Counter


def get_index_different_char(chars):
    alpha_num = [str(char).isalnum() for char in chars]
    counts = Counter(alpha_num)
    return alpha_num.index(counts.most_common(2)[1][0])