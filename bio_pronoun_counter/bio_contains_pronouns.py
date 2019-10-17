import re

from enum import Enum


class ContainsBio(Enum):
    YES = 1
    NO = 0
    MAYBE = 2


def bio_contains_pronouns(bio):
    perfect_matches = ['he/him', 'she/her', 'they/them', 'ze', 'hir']
    probably_matches = ['they', 'he', 'her', 'him', 'her', 'pronouns']

    words = re.findall(r"[\w'/]+", bio.lower())
    for match in perfect_matches:
        if match in words:
            return ContainsBio.YES

    for match in probably_matches:
        if match in words:
            return ContainsBio.MAYBE
    return ContainsBio.NO
