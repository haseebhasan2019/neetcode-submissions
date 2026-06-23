class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            m = (l+r) // 2
            b = total//2 - m -2
            
            a_left = A[m] if m >= 0 else float('-inf')
            a_right = A[m+1] if (m+1) < len(A) else float('inf')
            b_left = B[b] if b >= 0 else float('-inf')
            b_right = B[b+1] if (b+1) < len(B) else float('inf')

            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return min(b_right, a_right)
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