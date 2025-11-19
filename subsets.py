def all_subsets(nums):
    subsets =[[]]

    for num in nums:
        new_subset = []
        for s in subsets:
            new_subset.append(s +[num])
        subsets += new_subset
    return subsets

A = ["hello",1,2]
print(all_subsets(A))