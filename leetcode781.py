class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        same_rabbit_dict = {}
        result = 0
        for answer in answers:
            if answer in same_rabbit_dict:
                if answer + 1 == same_rabbit_dict[answer]:
                    same_rabbit_dict[answer] = 1
                    result += answer + 1
                else:
                    same_rabbit_dict[answer] += 1
            else:
                result += answer + 1
                same_rabbit_dict[answer] = 1
        
        return result