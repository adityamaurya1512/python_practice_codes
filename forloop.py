fruits = ["apple","guava","mango"];
scores=[1,2,4,6,9,13,14]
total_score=0
for item in fruits:
    print(item)

for score in scores:
    if score>10:
     total_score+=score
print(total_score)



#range function loop
range_sum=0
for number in range(1,101):
    range_sum+=number
print(range_sum)

#range with step 
range_step_sum=0
for number in range(1,101,2):
    range_step_sum+=number
print(range_step_sum)
