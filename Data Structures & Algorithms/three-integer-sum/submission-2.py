class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        output = []
        skip = False

        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            tmp = nums[i] 
            if(i != 0 and nums[i]==nums[i-1]):
                skip = True
            else:
                skip = False
            while(left < right and not skip):
                mySum = nums[left] + nums[right]
                if(tmp + mySum == 0):
                    output.append([nums[left], nums[right], nums[i]])
                    right -= 1
                    left += 1
                    while(left < right and nums[left-1] == nums[left]):
                        left +=1
                elif ( tmp + mySum > 0):
                    right -=1
                else:
                    left += 1

            
        return output


