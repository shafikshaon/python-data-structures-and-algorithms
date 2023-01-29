def main(heights):
    print(f"Input: {heights}.")
    height_count = {}

    for height in heights:
        if height not in height_count:
            height_count[height] = 1
        else:
            height_count[height] += 1

    print(f"Height count: {height_count}.")
    student_count_right_place = 0
    student_count_wrong_place = 0
    for height in heights:
        print(
            f"Student in right place: {student_count_right_place} and wrong place: {student_count_wrong_place}. "
            f"Height count is: {height_count}."
        )
        while (
            student_count_right_place not in height_count
            or height_count[student_count_right_place] == 0
        ):
            print(f"Student in right place: {student_count_right_place + 1}.")
            student_count_right_place += 1
        if height != student_count_right_place:
            print(
                f"Current height is {height}. Currently student in right place: {student_count_right_place}. "
                f"As {height} != {student_count_right_place}, "
                f"so increment student wrong place to {student_count_wrong_place + 1}."
            )
            student_count_wrong_place += 1
        height_count[student_count_right_place] -= 1
        print(f"Height count is now: {height_count}.\n")
    print(f"Total student in wrong place: {student_count_wrong_place}.")
    return student_count_wrong_place


main(heights=[1, 1, 4, 2, 1, 3])

"""
Output:
Input: [1, 1, 4, 2, 1, 3].
Height count: {1: 3, 4: 1, 2: 1, 3: 1}.
Student in right place: 1.
Height count is now: {1: 2, 4: 1, 2: 1, 3: 1}.

Height count is now: {1: 1, 4: 1, 2: 1, 3: 1}.

Current height is 4. Currently student in right place: 1. As 4 != 1, so increment student wrong place to 1.
Height count is now: {1: 0, 4: 1, 2: 1, 3: 1}.

Student in right place: 2.
Height count is now: {1: 0, 4: 1, 2: 0, 3: 1}.

Student in right place: 3.
Current height is 1. Currently student in right place: 3. As 1 != 3, so increment student wrong place to 2.
Height count is now: {1: 0, 4: 1, 2: 0, 3: 0}.

Student in right place: 4.
Current height is 3. Currently student in right place: 4. As 3 != 4, so increment student wrong place to 3.
Height count is now: {1: 0, 4: 0, 2: 0, 3: 0}.

Total student in wrong place: 3.


Time complexity: O(n)
Space complexity: O(m) for m the number of unique heights in heights. This is due to us saving the hashmap height_counter. 
In worst case m=n and we get O(n).
"""
