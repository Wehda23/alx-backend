#!/usr/bin/env python3
"""
Module contains Server Class
"""
import csv
import math
from typing import List, Tuple

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
