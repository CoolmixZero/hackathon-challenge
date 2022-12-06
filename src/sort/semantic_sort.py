import spacy


class SemanticSort:
    def __init__(self, request: str, data: list):
        self.__nlp = spacy.load('en_core_web_md')
        self.__request = ''.join([i for i in request if i.isalpha() or i == ' '])
        self.__data = data


    def __fitness_score(self, target: str) -> float:
        sentence1 = self.__nlp(self.__request)
        sentence2 = self.__nlp(target)

        return sentence1.similarity(sentence2)


    def __find_focus_fitness(self, focus_vals: list, obj: dict):
        for key, topics in zip(obj, focus_vals):
            for topic in topics:
                obj[key] += self.__fitness_score(topic['name'])/len(topics)

    
    def __find_description_fitness(self, summary: list) -> dict:
        return {i['name']: self.__fitness_score(i['description'])
                for i in summary}

    
    def sort_data(self, selector: int) -> dict:
        focus_vals = [i[0]['values'] for i in self.__data.parse_focus()[:selector]]
        result = self.__find_description_fitness(self.__data.parse_summary()[:selector])
        
        self.__find_focus_fitness(focus_vals, result)
        sorted_result = {k: v for k, v in sorted(result.items(), key=lambda x: x[1], reverse=True)}

        return sorted_result