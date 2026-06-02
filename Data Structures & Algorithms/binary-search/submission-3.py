class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        up = len(nums) -1 

        while(low <= up):
            mid = (up - low) // 2 + low

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                up = mid - 1
        return -1



            