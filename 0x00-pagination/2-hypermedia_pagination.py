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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        dataset = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(dataset),
            "page": page,
            "data": dataset,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
            }
