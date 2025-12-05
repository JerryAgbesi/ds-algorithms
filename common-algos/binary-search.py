nums = [12, 24, 34, 36, 43, 48, 54, 56, 76, 98]

def binary_search(nums,s):
  l,r = 0,len(nums)-1

  while l <= r:
    mid = l + (r-l)//2

    if nums[mid] == s:
      return mid

    elif nums[mid] < s:
      l = mid + 1

    else:
      r = mid -1

  return -1

print(binary_search(nums,90))
