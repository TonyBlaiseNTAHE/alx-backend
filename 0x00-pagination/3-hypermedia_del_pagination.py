#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """function to return data from dataset in a dictionary,
            handling deletion-resilient pagination
           args:
               index: the start index of the return page
               page_size: the length of the returned dataset page
        """
        assert isinstance(index, int) and index >= 0 \
            and index < len(self.dataset())
        assert isinstance(page_size, int) and page_size > 0

        data = []
        current_index = index
        next_index = index

        while len(data) < page_size and current_index < len(self.__indexed_dataset):
            if current_index in self.__indexed_dataset:
                data.append(self.__indexed_dataset[current_index])
            current_index += 1

        next_index = current_index
        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
