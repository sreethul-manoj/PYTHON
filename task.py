nums1=[1,2,3,]
nums2=[1,1,1]
a=[]
for i in nums1:
    for j in nums2:
        if i==j:
            if i not in a:
                a.append(i)
print(a)

