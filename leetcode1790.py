class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        length = len(s1)

        switch_index_list = []

        for i in range(length):
            if s1[i] != s2[i]:
                switch_index_list.append(i)

        if not switch_index_list:
            return True
    
        if len(switch_index_list) != 2:
            return False

        first_index = switch_index_list.pop()
        second_index = switch_index_list.pop()

        if s1[first_index] == s2[second_index] and s1[second_index] == s2[first_index]:
            return True
        else:
            return False        