
from random import randint, random


def quick_sort(list_number:list):
    if len(list_number)>1:
        min,max= list_number[0],list_number[0]
        for i in list_number[1:]:
            if i <min:
                min=i
            if i>max:
                max=i
        l1=list()
        l2 =list()
        for i in list_number:
            if i <=(max+min)/2 :
                l1.append(i)
            else:
                l2.append(i)
        if (max+min)//2!=max :
            l1=quick_sort(l1)
            l2=quick_sort(l2)
        return l1+l2
    else: 
        return list_number    
l1=[randint(1,200) for x in range(1,200,1)]
print(len(l1),quick_sort(l1))