


class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        unsortedArray = []
        result = []
        hash_map = {}

        for i in range(len(arr2)):
            hash_map[arr2[i]] = 0 

        for i in range(len(arr1)):
            if arr1[i] in hash_map:
                hash_map[arr1[i]] += 1 
            else:
                unsortedArray.append(arr1[i])

        # print(hash_map)
        # print(unsortedArray)

        for num in arr2:
            result.extend([num] * hash_map[num])

        result.extend(sorted(unsortedArray)) 
        return result


# print(Solution.relativeSortArray([7, 8, 2, 2, 3], [2,3]))
