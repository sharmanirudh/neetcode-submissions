class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        solution = []
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            l = i + 1
            r = len(numbers) - 1
            while l <= r:
                mid = (l + r) // 2
                if numbers[i] + numbers[mid] == target:
                    solution.append(i + 1)
                    solution.append(mid + 1)
                    break
                elif numbers[i] + numbers[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            if len(solution) == 2:
                break

        return solution
