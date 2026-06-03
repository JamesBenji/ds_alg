"""
Problem: Move zeros

Given an integer array nums, movel all 0's to the end of it while maintaining the relative order of the non-zero
elements.
    Not that this must be done without making a copy of the array.


Case 1
Input:      [0,1,0,3,12]
Output:     Returns nothing, but the nums array should now be [1,3,12,0,0]

Case 2
Input:      [0]
Output:     Returns nothing, but the nums array should now be [0]

Constraints
1 <= nums.length <= 10e4
-2e31 <= nums[i] <= (2e31) - 1
In-place: Don't duplicate the input array. Any solution using O(n) extra space technically violates the constraint.
"""
from typing import List

# By swapping: O(n^2) time complexity. Simple to understand. Better options exist.
class Solution():

    def move_zeroes_by_swapping(self, nums: List[int]) -> None:
        """
        This was my first solution I wrote. This was the simplest solution I got based on the idea of bubble sort.
        The goal was to bubble the zeros to the end.
        """
        n = len(nums)
        swapped = False

        for i in range(n - 1):
            for j in range(n - 1):
                if nums[j] == 0 and nums[j+1] != 0:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
                    swapped = True

            if not swapped:
                break

    def move_zeroes_by_extra_array(self, nums: List[int]) -> None:
        """
            The idea is to insert non-zero numbers into a new local array of zeros of size n.
            The zeros are automatically in their correct positions and the problem is reduced to
            overwriting the existing zeros where need be.

            Takes O(n) space which is similar to having creating a duplicate of the nums array thus not a good
            solution given the constraints.

            Takes O(n) time which is good.
        """
        n = len(nums)

        # creating the array of zeros
        temp_array = [0] * n

        # write non-zero numbers in the order of discovery
        insert_position = 0

        for num in nums:
            if num != 0:
                temp_array[insert_position] = num
                insert_position += 1

        # write the content of the temp array into the nums array to satisfy the in-place constraint
        for i in range(n):
            nums[i] = temp_array[i]


        def move_zeroes_by_two_pointer_swap(self, nums: List[int]) -> None:
            """
                This works by using two pointer heads. The slow pointer trails behind the fast pointer.
                !! The slow pointer marks the index of the zero and never takes on the index of a non-zero element.
                The slow pointer lives outside the loop.
                The fast pointer is managed by a loop, and it triggers a swap when its number is non-zero.

                Time: O(n)
                Space: O(1)
            """

            n = len(nums)

            slow_pointer = 0

            for i in range(n):
                # swap if number at i is non-zero with the number at slow pointer (if is zero)
                # The slow pointer will get left behind and stick with the first zero it finds ie when nums[i] == 0
                # because the conditional only swaps when i is at a non-zero number. Of course, when i == slow_pointer
                # swaps are still happening but at the same index which is redundant. This can be optimized by swapping
                # only when i and slow_pointer are not the same as shown
                # In the start, both the slow and fast pointer move together
                # The
                if nums[i] != 0:
                    # optimized swap
                    if i != slow_pointer:
                        # swap
                        nums[slow_pointer], nums[i] = nums[i], nums[slow_pointer]
                    slow_pointer += 1







case_1 = [0]
case_2 = [1]
case_3 = [1,0,0,0,0]
case_4 = [0,1,0,3,12]
case_5 = [1,2,3,4,5]
case_6 = [0,0,0,0,1]
case_7 = [4,2,4,0,0,3,0,5,1,0]

test = Solution()

test.move_zeroes_by_two_pointer_swap(case_1)
print(f"Got: {case_1} Expected: [0]")

test.move_zeroes_by_two_pointer_swap(case_2)
print(f"Got: {case_2} Expected: [1]")

test.move_zeroes_by_two_pointer_swap(case_3)
print(f"Got: {case_3} Expected: [1,0,0,0,0]")

test.move_zeroes_by_two_pointer_swap(case_4)
print(f"Got: {case_4} Expected: [1,3,12,0,0]")

test.move_zeroes_by_two_pointer_swap(case_5)
print(f"Got: {case_5} Expected: [1,2,3,4,5]")

test.move_zeroes_by_two_pointer_swap(case_6)
print(f"Got: {case_6} Expected: [1,0,0,0,0]")

test.move_zeroes_by_two_pointer_swap(case_7)
print(f"Got: {case_7} Expected: [4,2,4,3,5,1,0,0,0,0]")
