# JQ 1st Mapping
numbers = [2435.654,456,456465,45,654]
"""new_nums=[]

for number in numbers:
    new_nums.append(number/3)

print(new_nums)"""
def divide(num):
    return num/3

new_nums = map(lambda num: num/3 ,numbers)
print(list(new_nums))
for num in new_nums:
    print(num)
