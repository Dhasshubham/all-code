# WAP to check if a list contains a palindrom of element(hints: use copy () method)
list1 = ["MAAM"]
list2 = [1,2,3]

copy_list1 = list1.copy() 
copy_list1.reverse()

if( copy_list1 == list1):
    print("palindrom")
    
else:
    print("not palindrom")
    
