#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    args:
        page: the page where the items are displayed
        page_size: the number of element on a page
        return: the starting and ending index in a tuple
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)
