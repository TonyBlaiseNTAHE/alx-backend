#!/usr/bin/env python3
"""0. Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters
    param:
        @page: the current page number
        @page_size: the number of items per page
    return:
        tuple of size two containing a start index and an end index
    """
    return ((page - 1) * page_size, page * page_size)
