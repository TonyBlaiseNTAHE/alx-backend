#!/usr/bin/env python3
"""2. Hypermedia pagination
"""
from typing import Tuple, List
import csv
import math


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

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
        """Returns the appropriare page of the dataset
        i.e the correct list of rows
        param:
            @page: the current page number
            @page_size: the number of items per page
        return:
            list of rows
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        if end > len(self.dataset()):
            return []
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a dictionary containing the following key-value pairs:
            - page_size: the length of the returned dataset page
            - page: the current page number
            - data: the dataset page
            - next_page: the next page number
            - prev_page: the previous page number
            - total_pages: the total number of pages
        param:
            @page: the current page number
            @page_size: the number of items per page
        return:
            dictionary of key-value pairs
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)

        data = self.dataset()[start:end]
        if page == 1:
            prev_page = None
            next_page = page + 1
        elif page == math.ceil((len(self.dataset()) / page_size)):
            prev_page = page - 1
            next_page = None
        else:
            prev_page = page - 1
            next_page = page + 1

        return {
                "page_size": len(data),
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": math.ceil(len(self.dataset()) / page_size)
        }
