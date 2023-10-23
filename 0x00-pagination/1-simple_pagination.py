#!/usr/bin/env python3
"""function that return tuple of size two containing a start index and end
 corresponding to the range of indexes to return in a list for those particular
pagination parameters
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """ Return a tuple size two containing a start index and an end index
    correspoding to range of indexes to return in alist for those particulars
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ return a page """
        assert isinstance(page, int) and page > 0, "Page must be int > 0"
        assert isinstance(page_size, int) and page_size > 0, "Page size must >\
         0"
        dataset = self.dataset()
        if not dataset:
            return []

        start_index, end_index = index_range(page, page_size)
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]
