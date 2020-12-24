from itertools import chain

passcodes = []

def read_data():
    with open('Day2_data', 'r', encoding = 'utf8') as data:
        for x in data:
            passcodes.append(x.strip())

read_data()

keys = []
values = []
for y in passcodes:
    new_pass = y.split(': ')
    keys.append(new_pass[0])
    values.append(new_pass[1])

    

alphabet = []
numbers = []
for vals in keys:
    cnt = 0
    for find in vals.split():
       if cnt % 2 == 0:
           numbers.append(find)
           cnt += 1
       else:
           alphabet.append(find)




final_list = []
range_list = []
for e in numbers:
    val = (e.split('-'))
    low_val = val[0]
    max_val = val[1]
    range_list.append([low_val, max_val])

#print(len(range_list))


cnt_val = 0
for x in range_list:
    x.append(alphabet[cnt_val])
    x.append(values[cnt_val])
    cnt_val += 1 

#print(range_list)
 

#Answer:

valid_passwords = 0 
for occurance in range_list:
    min_val = int(occurance[0])
    max_val = int(occurance[1])
    substring = occurance[2]
    string = occurance[3]
    if (string.count(substring) >= min_val and string.count(substring) <= max_val):
        valid_passwords += 1 
    
print("The number of valid passwords is " + str(valid_passwords))
        

    
   


    
    
    

    
           
       
       
   

    
    
    








