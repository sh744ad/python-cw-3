# write your code here
favorite_animals = ['cats','dogs','monkey','rabbit']
print(favorite_animals)
print(favorite_animals[2])
favorite_animals.remove('monkey')
print(favorite_animals) 
favorite_animals.append('turtle')
print(favorite_animals)
for animal in favorite_animals:
  print(f"i love {animal}")
numbers = [5,4,3,2,1]  
numbers_sum  = 0
for num in numbers:
  numbers_sum = num + numbers_sum
  
print(numbers_sum)
  
