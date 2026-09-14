import json
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = json.dumps(strs)
        #print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:

        strs = json.loads(s)
        #print(strs)

        return strs
