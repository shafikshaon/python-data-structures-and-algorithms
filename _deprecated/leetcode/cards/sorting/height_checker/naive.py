def main(heights):
    sorted_height = sorted(heights)

    student_count_wrong_place = 0
    for i in range(len(heights)):
        if heights[i] != sorted_height[i]:
            student_count_wrong_place += 1
    print(f"Total student in wrong place: {student_count_wrong_place}.")
    return student_count_wrong_place


main(heights=[1, 1, 4, 2, 1, 3])

"""
Output:
Total student in wrong place: 3.

Time complexity: O(nlog(n))
Space complexity: O(n) for saving the sorted heights array sorted_height.
"""
