# 자꾸 시간이 초과했다는 에러가 뜬다.
# class NumberContainers:
#     def __init__(self):
#         self.index_dict = {}
#         self.number_dict = {}
        
#     def change(self, index: int, number: int) -> None:
#         if index in self.index_dict:
#             prev_number = self.index_dict[index]
#             self.number_dict[prev_number].remove(index)

#             if not self.number_dict[prev_number]:
#                 del self.number_dict[prev_number]

#         self.index_dict[index] = number
#         if number in self.number_dict:
#             self.number_dict[number].add(index)
#         else:
#             self.number_dict[number] = {index}

#     def find(self, number: int) -> int:
#         if number not in self.number_dict:
#             return -1
        
#         return sorted(self.number_dict[number])[0]


## 정답지를 봤다.
# class NumberContainers:

#     def __init__(self):
#         # Initializing the defaultdict with SortedSet and the regular dictionary
#         # Map from number to set of indices
#         self.number_to_indices = collections.defaultdict(SortedSet)
#         # Map from index to number
#         self.index_to_number = {}

#     def change(self, index: int, number: int) -> None:
#         # If index already has a number, remove it from the old number's index set
#         if index in self.index_to_number:
#             previous_number = self.index_to_number[index]
#             self.number_to_indices[previous_number].remove(index)
#             if not self.number_to_indices[previous_number]:
#                 del self.number_to_indices[previous_number]

#         # Update the number and add the index to the new number's set
#         self.index_to_number[index] = number
#         self.number_to_indices[number].add(index)

#     def find(self, number: int) -> int:
#         # Return the smallest index for the given number, or -1 if not found
#         if number in self.number_to_indices and self.number_to_indices[number]:
#             return self.number_to_indices[number][0]
#         return -1


## Best Practice -> heapq를 사용했는데 python내장 library를 잘 활용할 필요가 있을 것 같다..
# class NumberContainers:

#     def __init__(self):
#         self.indexToNum = {}
#         self.numToIndices = {}

#     def change(self, index: int, number: int) -> None:
#         self.indexToNum[index] = number
#         if number not in self.numToIndices:
#             self.numToIndices[number] = []
#         heapq.heappush(self.numToIndices[number], index)

#     def find(self, number: int) -> int:
#         if number not in self.numToIndices:
#             return -1
#         pq = self.numToIndices[number]        
#         while pq:
#             currIndex = pq[0]
#             if self.indexToNum[currIndex] != number:
#                 heapq.heappop(pq)
#             else:
#                 return currIndex
#         return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
