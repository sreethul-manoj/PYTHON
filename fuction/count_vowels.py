def count_vowels(a):
    count=0
    for i in a:
        if i in 'aeiouAEIOU':
            count+=1
    print("count of vowels =",count)
a=input("enter the string : ")
count_vowels(a)