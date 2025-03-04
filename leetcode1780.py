class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        index = 0
        three = 3
        three_list = []
        number = 1
        while number <= n:
            number = three ** index

            if number == n:
                return True

            if not three_list:
                three_list.append(number)
                index += 1
                continue

            current_new_list = [number]
            for i in three_list:
                new_num = i + number
                if new_num == n:
                    return True
                current_new_list.append(new_num)
            three_list.extend(current_new_list)
            index += 1
        
        return False

        