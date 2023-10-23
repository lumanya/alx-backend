#!/usr/bin/env python3
"""function that return tuple of size two containing a start index and end
 corresponding to the range of indexes to return in a list for those particular
pagination parameters
"""


def index_range(page, page_size):
    """ Return a tuple size two containing a start index and an end index
    correspoding to range of indexes to return in alist for those particulars
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
