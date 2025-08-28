class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged_array = nums1 + nums2
        merged_array.sort()

        lenght = len(merged_array)

        print("This is the lenght " +str(lenght))

        if lenght % 2 != 0:
            median_index = lenght // 2
            median = merged_array[median_index]
        else:
            upper_median_index = lenght // 2
            lower_median_index = upper_median_index - 1
            median = (merged_array[lower_median_index] + merged_array[upper_median_index]) / 2

        return median