# 原始数组
data = [42, 7, 19, 88, 3, 56, 31, 12]

# 1. 求和
total = sum(data)
print("原始数据:", data)
print("求和结果:", total)

# 2. 排序（升序，不影响原数组）
sorted_asc = sorted(data)
print("升序排序:", sorted_asc)

# 3. 排序（降序）
sorted_desc = sorted(data, reverse=True)
print("降序排序:", sorted_desc)

# 4. 原地排序（直接修改原数组）
data.sort()
print("原地排序后:", data)

# 5. 平均值
average = total / len(data)
print("平均值:", average)

# 6. 最大值 / 最小值
print("最大值:", max(data))
print("最小值:", min(data))
