class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string = encoded_string + "#" + str(len(word)) + " " + word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        start = 0
        end = 0
    
        while end < len(s):
            start = s.find("#", int(end), len(s))
            if start == -1:
                break
            count = s.find(" ", start + 1, len(s))
            length = int(s[start + 1: count])
            end = count + length + 1
            decoded_strs.append(s[count + 1: int(end)])

        return decoded_strs
