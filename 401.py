class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        out = []
        for h in range(12) :
            for m in range(60) :
                if h.bit_count() + m.bit_count() == turnedOn :
                    out.append(f"{h}:{m:02d}")
        return out