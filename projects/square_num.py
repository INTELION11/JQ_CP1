# JQ 1st Square root Numbers
# import math
# numbers list 1-20
#new num is map(num is num**2, numbers)
#for num in new nums: display originial {int(math.sqrt(num))} squared = {num}
import math; numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]; new_nums = map(lambda num: num**2 ,numbers)
for num in new_nums: print(f"original:{int(math.sqrt(num))} squared: {num}")