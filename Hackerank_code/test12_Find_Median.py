#leetcode
class Solution(object):
    def findMedianSortedArrays(self,nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) == 1 or len(nums1) == 2:
            x = (float(sum(nums1)) / float(len(nums1)))
        else:
            if len(nums1) % 2 != 0:
            	x = nums1[((int(len(nums1)-1)/2))]
            if len(nums1) % 2 == 0:
            	x = float((float(nums1[(int(len(nums1)/2))]) + float(nums1[((int(len(nums1)/2))-1)]))/2)
        return x
a = [1,3]
b = [2]
s = Solution()   
print (s.findMedianSortedArrays(a,b))