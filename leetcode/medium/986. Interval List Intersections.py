# Time Complexity: O(min(n,m)) where n and m - number of elements in the lists
# Space Complexity: O(1), if not count returned list of intersection


def intervalIntersection(
    firstList: list[list[int]], secondList: list[list[int]]
) -> list[list[int]]:
    intersection = []
    i, j = 0, 0
    while i < len(firstList) and j < len(secondList):
        left_bound = max(firstList[i][0], secondList[j][0])
        right_bound = min(firstList[i][1], secondList[j][1])
        if left_bound <= right_bound:
            intersection.append([left_bound, right_bound])
        if firstList[i][1] > secondList[j][1]:
            j += 1
        else:
            i += 1
    return intersection


"""
cases:
[[]] [[1,5]] -> [[]]
[[1,2], [3,4]] [[2,4]] -> [[2,2],[3,4]]
"""
