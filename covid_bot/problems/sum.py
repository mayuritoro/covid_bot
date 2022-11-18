from audioop import reverse


numbers={1,3,4,5,9,10}
numbers=list(numbers)
sub_set1=[]
sub_set2=[]
for i in range(len(numbers)-2,-1,-1):
    if numbers[-1]+numbers[i]:
        
