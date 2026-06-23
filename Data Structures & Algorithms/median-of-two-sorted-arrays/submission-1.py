class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A)
        while True:
            m = (l+r) // 2
            b = (total+1)//2 - m
            
            a_left = A[m-1] if m > 0 else float('-inf')
            a_right = A[m] if m < len(A) else float('inf')
            b_left = B[b-1] if b > 0 else float('-inf')
            b_right = B[b] if b < len(B) else float('inf')

            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return max(a_left, b_left)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                r = m-1
            else:
                l = m+1


# 1 1 1 2 3 4
#     b
# 4 5 6
#   m

# We have array A and B
# A is the shorter array
# We perform binary search on A for a partition point
# the partition in A is the complement of the partition in B
# (A+B - elements in A's left partition = B's partition point)
# valid partition -> a_left <= b_right and b_left <= a_right