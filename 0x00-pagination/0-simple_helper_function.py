#!/usr/bin/env python3
"""
Module contains function named index_range
 that takes two integer arguments page and page_size.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Function that takes two integer arguments page and page_size.

    Args:
        page (int): Page number.
        page_size (int): Page content size.

    Returns:
        Tuple: First index represents Start Size of content
          Second index rerpresents End point.
    """
    start: int = (page - 1) * page_size
    end: int = start + page_size
    return (start, end)
