#!/usr/bin/env python3
"""
Simple helper function
"""
import csv
import math
from typing import List, Dict


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


class Server:
    """Server class to paginate a database of popular baby names
    """
    DATA_FILE = "popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        args: page: the page index
              page_size: the length of the returned dataset page
        returns: the right pagination
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start_idx, end_idx = index_range(page=page, page_size=page_size)

        if end_idx > len(self.dataset()):
            return []
        return self.dataset()[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """function that returns data from dataset in a dictionary
           args: page: the page index
                 page_size: the length of the returned dataset page
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        data = self.get_page(page=page, page_size=page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
