#!/usr/bin/env python3
"""
Module contains a modified Server Class
"""
import csv
import math
from typing import List, Tuple, Dict, Any, Optional

index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Method to retrieve the pages"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        dataset: List[List] = self.dataset()
        content_indexs: Tuple[int, int] = index_range(page, page_size)
        contents: List[List] = []
        try:
            for index in range(content_indexs[0], content_indexs[1]):
                contents.append(dataset[index])
            return contents
        except IndexError as e:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Method that takes the same arguments (and defaults)
          as get_page and returns a dictionary containing the following key-value pairs
        """
        data: List[List] = self.get_page(page, page_size)
        total_pages: int = math.ceil(len(self.dataset()) / page_size)
        page: int = page
        page_size: int = page_size
        next_page: Optional[int] = page + 1 if data else None
        prev_page: Optional[int] = page - 1 if page > 1 else None
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
