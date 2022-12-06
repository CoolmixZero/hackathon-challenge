from src.utils import ProcessData
from .semantic_sort import SemanticSort
from .numeric_sort import NumericSort
import json


class MainSort:
    def __init__(self, request: str):
        data = ProcessData()
        self.__semantic_sort = SemanticSort(request, data)
        self.__numeric_sort = NumericSort(data)

    def __json_preprocess(self, obj: dict) -> list:
        return [{"name": key, "fitness": obj[key]} for key in obj]

    def sort_data(self, count: int, rating_count: int) -> dict:
        sorted_semantic = self.__semantic_sort.sort_data(count)
        sorted_numeric = self.__numeric_sort.sort_data(sorted_semantic, rating_count)

        with open('result.json', 'w') as fp:
            json.dump(self.__json_preprocess(sorted_numeric), fp)

        return sorted_numeric
