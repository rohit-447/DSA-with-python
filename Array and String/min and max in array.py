#Find the Maximum and Minimum Element in an arrray
import numpy as np
temp=0

#method 1 to convert array into list and sort
#Complexity: O(n log n) due to sorting.
def sortt1(arrray):
        a=arrray.tolist()
        a.sort()
        print("Min",a[0],"Max",a[-1])

#method 2 to sort array
#Complexity: O(n²) due to nested loops
def sortt2(arrray):
        for i in range(0,len(arrray)):
                for j in range (0,len(arrray)):
                        if (arrray[i]>arrray[j]):
                                temp=arrray[i]
                                arrray[i]=arrray[j]
                                arrray[j]=temp
        print("Min",arrray[-1])
        print("Max",arrray[0])

#method 3 direct min and max
#Complexity: O(n) as it traverses the array once.
def sortt3(arrray):
        print(min(arrray))
        print(max(arrray))

#method 4 sort fun
#Complexity: O(n log n) due to sorting.
def sortt4(arrray):
        arrray.sort()
        print("Min",arrray[0])
        print("Max",arrray[-1])

#method 5 compare
#Complexity: O(n) since it goes through the array once.
def sortt5(arrraay):
        mini=arrraay[0]
        maxi=arrraay[0]
        for i in range(0,len(arrraay)):
            if (arrraay[i])<mini : mini =arrraay[i]
            if (arrraay[i])>maxi : maxi =arrraay[i]
        print("Min",mini)
        print("Max",maxi)

arrray=np.array([1,2,7,3,4])
sortt1(arrray)
sortt2(arrray)
sortt3(arrray)
sortt4(arrray)
sortt5(arrray)
