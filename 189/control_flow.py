IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    filtered = []
    for name in names:
        if name.startswith(IGNORE_CHAR):
            continue
        if not all(c.isalpha() for c in name):
            continue
        if name.startswith(QUIT_CHAR):
            break
        if len(filtered) == 5:
            break
        filtered.append(name)
    return filtered