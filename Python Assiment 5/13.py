# Write a generator function that generates the first 10 even numbers.
def evennum() :
    count = 0 
    number = 0 
    while count<10 :
        yield number 
        count+=1
        number+=2

for even_number in evennum() :
    print(even_number,end=" ")
