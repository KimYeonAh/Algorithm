def all_sum_of_subsets(S, M) :
    DFS_sum_of_subsets(S, M, 0, [], sum(S))

nums = [3, 34, 4, 12, 5, 2]
M = 9
solution = all_sum_of_subsets(nums, M)
print("입력 집합: ", nums, 'M= ', M)