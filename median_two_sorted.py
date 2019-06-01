import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_len_p_2 = len(nums1) + len(nums2)
        all_array = []
        if len(nums1) > 0 and len(nums2) > 0:
            max_value = max(nums1) + max(nums2) + 1
        elif len(nums1) == 0:
            max_value = max(nums2) + 1
        elif len(nums2) == 0:
            max_value = max(nums1) + 1
        nums1.append(max_value)
        nums2.append(max_value)
        for i in range(0, total_len_p_2):
            if nums1[0] >= nums2[0]:
                all_array.append(nums2[0])
                nums2.pop(0)
            elif nums1[0] <= nums2[0]:
                all_array.append(nums1[0])
                nums1.pop(0)
        # even
        if len(all_array)%2 == 0:
            middle = int(len(all_array)/2)
            middle_1 = all_array[middle]
            middle_2 = all_array[middle-1]
            return float((float(middle_1)+float(middle_2))/2)
        else:
            middle = int(math.floor(len(all_array)/2))
            return all_array[middle]
nums1 = [1, 2]
nums2 = [3, 4]
a = Solution()
print(a.findMedianSortedArrays(nums1, nums2))
                
    