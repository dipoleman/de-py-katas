def digital_root(num):
  nums = sum([int(x) for x in str(num)])
  if nums < 10:
    return nums
  else:
    return digital_root(nums)

print(digital_root(132189))
print(digital_root(4938783478748927874349589430805894034598834193))