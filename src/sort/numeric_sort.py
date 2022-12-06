class NumericSort:
    def __init__(self, data: list):
        self.__data = data

    
    def __get_rating(self, summary: list, obj_keys: list) -> dict:
        return {i['name']: i['rating'] for i in summary if i['name'] in obj_keys}


    def sort_data(self, obj: dict, selector: int) -> dict:
        summary = self.__data.parse_summary()[:len(obj)]
        rating = self.__get_rating(summary, list(obj.keys())[:selector])

        sorted_selector = sorted(list(obj.items())[:selector],
                          key=lambda x: rating[x[0]], reverse=True)
        
        return {k: v for k, v in sorted_selector+list(obj.items())[selector:]}