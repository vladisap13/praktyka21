import random
rand_list = [random.randint(-100, 100) for x in range(30)]
max_num = max(rand_list)
rand_list.index(max_num)
print("list: ",rand_list)
print("max: ",max_num)
print("max index: ",rand_list.index(max_num)+1)
print("result list :")
for i in range(29):
  if rand_list[i]<0 and rand_list[i+1]<0:
    print(rand_list[i],rand_list[i+1], end =" ")