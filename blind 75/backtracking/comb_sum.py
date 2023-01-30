class Solution:
    def combinationSum(self, candidates: list, target: int) -> list[list[int]]:
        '''
        create array of size target + 1
        array[i] = [[i]] for i in candidates, [] for all others
        for i <= target:

            half = ceiling(i/2) if i/2 is fraction else i/2
            for candidate in candidates:
                if i-candidate between half and target:
                    for each subarr in array[i-candidate]:
                        array[i].extend( subarr + [candidate])


        return array[target]
        '''