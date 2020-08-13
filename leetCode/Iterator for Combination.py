from itertools import combinations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = sorted(list(combinations(characters, combinationLength)))
        
    def next(self) -> str:
        try:
            ele = self.combinations[0]
            nxt = ''.join(i for i in ele)
        
            self.combinations = self.combinations[1:]
        
            return nxt

        except:
            return False

    def hasNext(self) -> bool:
        if len(self.combinations) > 0:
            return True
        else:
            return False
