class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = dict()
        for c1, c2 in zip(s, t):
            
            # key에 존재하지 않지만 value에 존재한다면 이미 다른 값에 들어가 있다는 의미이미로 False
            if c1 not in d and c2 in d.values():
                return False;
            
            # key에 존재하지 않으면 추가
            elif c1 not in d:
                d[c1] = c2
                
            # key에 존재한다면, 값을 비교했을 때 다르다면 한쌍의 key-value가 아니므로 False
            else:
                if d[c1] != c2:
                    return False
                
        return True
