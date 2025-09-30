count = int(input())
seen = [False] * count
nums = [int(x) for x in input().split(" ")]
for i in range(count - 1):
    num = nums[i]
    seen[num - 1] = True
for i in range(count):
    if not seen[i]:
        print(i + 1)
        break
