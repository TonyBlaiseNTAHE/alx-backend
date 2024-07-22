#!/usr/bin/env python3

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """return indices
    """
    start_idx = (page - 1) * page_size
    end_idx = (page * page_size)
    return (start_idx, end_idx)


class Server:
    """Server classs to paginate a database of popular baby names.
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
        return the appropriate page of the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_idx, end_idx = index_range(page, page_size)

        if end_idx >= len(self.dataset()):
            return []

        return self.dataset()[start_idx:end_idx]
