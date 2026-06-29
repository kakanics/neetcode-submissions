class Solution:

    def encode(self, strs: List[str]) -> str:
        return "|-|".join(strs) if len(strs) else "emp"

    def decode(self, s: str) -> List[str]:
        return s.split("|-|") if s != "emp" else []