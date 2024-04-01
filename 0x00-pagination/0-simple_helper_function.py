#!/usr/bin/env python3
"""
Simple helper function
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """  function should return a tuple of size two

    :param page:
    :param page_size:
    :return:
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
