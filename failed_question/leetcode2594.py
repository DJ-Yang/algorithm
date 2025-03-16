class Solution:

    def repairCars(self, ranks: List[int], cars: int) -> int:
        low = 1
        high = cars ** 2 * ranks[0]


        while low < high:
            mid = int(low + ((high - low) / 2))
            count = 0
            for rank in ranks:
                count += int((mid // rank) ** 0.5)
            
            if count >= cars:
                high = mid
            else:
                low = mid + 1
            
        return low
        