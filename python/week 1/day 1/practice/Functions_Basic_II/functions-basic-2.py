
# the countdown function 

def countdown(i):
    for i in range(i,0,-1):
        print(i)

# Print and return Function
list=[2,3]
def print_and_return(list):
    print (list[0])
    return list[1]


print_and_return(list)


print("*"*30)

# first_plus_length function 



def first_plus_length(list):
    return(list[0]+ len(list))

print(first_plus_length(list))


print("*"*30)

#values_greater_than_second function 
list=[10,3,2,3,5,7]
newlist=[]

def values_greater_than_second(list):
    sum=0
    for i in range (len(list)):
        if list[i]>list[1]:
            newlist.append(list[i])
            sum=sum+1
    print(sum)
    return(newlist)   

print (values_greater_than_second (list))     

# length_and_value

print("*"*30)

def length_and_value(a,b):
    createdlist=[]
    for i in range(a):
        createdlist.append(b) 
    return (createdlist)
print(length_and_value(4,7))       