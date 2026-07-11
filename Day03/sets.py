nums = [1, 2, 2, 3, 3, 3]
unique = set(nums) # {1, 2, 3}
a = {"Almaz", "Dawit"}
b = {"Dawit", "Samuel"}
a | b # union -> {'Almaz', 'Dawit', 'Samuel'}
a & b # intersection -> {'Dawit'}
a - b # difference -> {'Almaz'}
print(unique)
print(a | b)
print(a & b)
print(a - b)