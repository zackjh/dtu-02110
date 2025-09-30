count = int(input())
seen = set()
nums = sorted(list(map(int, input().split())))
prev = nums[0]
count = 1
for num in nums:
    if num != prev:
        count += 1
        prev = num
print(count)
