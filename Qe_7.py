
print("Enter integers 1:")
list1 = list(map(int, input()))
print("Enter integers 2:")
list2 = list(map(int, input()))
if len(list1) == len(list2):
    print("lists have the same length.")
else:
    print("Lists do not have the same length.")
sum1 = 0
for i in list1:
    sum1 += i
sum2 = 0
for i in list2:
    sum2 += i
if sum1 == sum2:
    print("lists have the same sum.")
else:
    print("Lists do not have the same sum.")
common_values = set(list1) & set(list2)
if common_values:
    print("Common values found in both lists:", common_values)
else:
    print("No common values found in both lists.")
