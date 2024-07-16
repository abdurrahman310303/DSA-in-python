from collections import Counter

def intersectionOfArrays(nums1,nums2):

    count1 = Counter(nums1)
    count2 = Counter(nums2)

    intersection = []
    for element in count1:
        if element in count2:
            min_count = min(count1[element],count2[element])
            intersection.extend([element] * min_count)
    return intersection

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

intersect = intersectionOfArrays(nums1,nums2)

print(intersect)