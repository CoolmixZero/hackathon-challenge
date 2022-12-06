from src import MainSort
import time


if __name__ == '__main__':
    request = "Recruiting company"

    start = time.perf_counter()
    ss = MainSort(request)
    print(ss.sort_data(100, 5))
    end = time.perf_counter()
    print(f"Time = {end - start}")