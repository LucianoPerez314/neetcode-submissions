class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            length = len(s)
            res.append(str(length))
            res.append("#")
            res.append(s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        end = len(s)
        i = 0
        res = []
        while i < end:
            num = []
            c = s[i]
            while c != "#":
                num.append(c)
                i += 1
                c = s[i]
            number = int("".join(num))
            i += 1
            one_s = s[i:i+number]
            i = i + number
            res.append(one_s)
        return res






