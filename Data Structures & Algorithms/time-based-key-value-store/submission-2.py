from collections import defaultdict
class TimeMap:
    # {test: (one, 10), (two, 20), (three, 30) } test 15
    #                      l
    #           m
    #           r

    def __init__(self):
        self.key_to_val = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_val[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        time_list = self.key_to_val[key]
        l, r = 0, len(time_list) - 1
        while l <= r:
            m = (l + r) // 2
            if time_list[m][1] == timestamp:
                return time_list[m][0]
            elif time_list[m][1] < timestamp:
                l = m + 1  
            else:
                r = m - 1

        return time_list[l - 1][0] if r >= 0 else ""
     
        




