class Solution:
    indexes = []

    def encode(self, strs: List[str]) -> str:
        self.indexes = []
        # goal: turn a list of strings into one string
        # [0: len(word)] - 1], [len(word), len(prev) + (len(curr_word) + 1)]
        # strs = ["Hello", "World", "!"]
        #                            10
        #                       
        # "".join(strs)
        # "HelloWorld"
        #  [[0,4], [5,9], [10,10]]
        # start = 5
        
        start = 0
        for word in strs:
            self.indexes.append([start, start + len(word) - 1])
            start += len(word)
        encoded_string = "".join(strs)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # goal: turn our string from the first function into a list of strings
        # "HelloWorld!"
        # result = [s[start:end + 1], s[start: end + 1]]
        #          [Hello], [World]
        # [[0,4], [5,9], [10,10]]
        # [Hello, World, !]
        decoded_strs = []
        for start, end in self.indexes:
            decoded_strs.append(s[start: end + 1])

        return decoded_strs







