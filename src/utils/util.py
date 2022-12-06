from dotenv import load_dotenv
import json, os


class ProcessData:
    load_dotenv()
    def __init__(self, filepath=os.getenv("FILEPATH")):
        self.__filepath: str = filepath
        self.data = self.__open()

    def __open(self) -> dict:
        try:
            with open(self.__filepath, "r", encoding="utf-8") as f:
                return json.load(f)

        except Exception as e:
            print(e)

    def parse_focus(self) -> list:
        return [el["focus"] for el in self.data]

    def parse_portfolio(self) -> list:
        return [el["portfolio"] for el in self.data]

    def parse_reviews(self) -> list:
        return [el["reviews"] for el in self.data]

    def parse_summary(self) -> list:
        return [el["summary"] for el in self.data]

    @staticmethod
    def parse_scores_and_description(self, summary_data: list) -> dict:
        return {el["name"]: (el["rating"], el["description"])
                for el in summary_data}
