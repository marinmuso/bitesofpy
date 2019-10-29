import re
from typing import List

# https://stackoverflow.com/a/43147265
# just for exercise sake, real life use emoji lib
IS_EMOJI = re.compile(r'[^\w\s,]')


def get_emoji_indices(text: str) -> List[int]:
    """Given a text return indices of emoji characters"""
    emojis = IS_EMOJI.findall(text)
    indices = [ind for ind, val in enumerate(text) if val in emojis]
    return indices
