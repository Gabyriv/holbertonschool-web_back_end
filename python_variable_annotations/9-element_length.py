#!/usr/bin/env python3
"""
Annotate the function parameters
and return values with the appropriate types
"""


from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function to annotate
    """
    return [(i, len(i)) for i in lst]
