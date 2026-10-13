class TimeMap:

    def __init__(self):
        # t_dict is a dictionary where keys are the k, and value
        # is a list of sorted timestamps
        self.t_dict = dict()
        # v_dict is a dictionary where keys are the keys, and value
        # is a list of values whose index shares the same index of their
        # timestamp in the corresponding spot in t_dict
        self.v_dict = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.t_dict:
            self.t_dict[key] = [timestamp]
            self.v_dict[key] = [value]
        else:
            self.t_dict[key].append(timestamp)
            self.v_dict[key].append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        print("YO", self.t_dict)
        # Find index of timestamp via binary search
        if key not in self.t_dict or timestamp < self.t_dict[key][0]:
            return ""
        lst = self.t_dict[key]
        l, r = 0, len(lst) - 1
        idx = -1
        while l <= r:
            m = (l + r) // 2
            idx = m
            if lst[m] == timestamp:
                break
            elif lst[m] < timestamp:
                l = m + 1
            else:
                r = m - 1
        if lst[idx] > timestamp:
            idx -= 1
        
        
        return self.v_dict[key][idx]
            
        
