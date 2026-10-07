class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        m = defaultdict(int)
        canidate = -1
        for personTrusts, trustedPerson in trust:
            m[personTrusts].append(trustedPerson)
        for personTrusts, peopleTrusted in m:
            if not peopleTrusted:
                canidate = personTrusts
        for personTrusts, peopleTrusted in m:
            if canidate not in peopleTrusted:
                return -1 
        return canidate
        