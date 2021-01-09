from DS.help.exectime import ET

data = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,
        1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,
        1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,
        1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,
        1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,
        1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,
        1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,
        1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2
        ]
find = 90000


def f(data, find):
    if find in data:
        print("True")
    else:
        print("False")

x =ET("f")    
f(data, find)
x.stop()

def binary_iterative(data, find):
    h = len(data)-1
    l = 0
    while l <= h: 
        mid=(l+h) // 2
        if data[mid] == find:return True
        elif data[mid] > find:h = mid -1
        else: l = mid+1
    return False
    
y = ET("iterative")
print(binary_iterative(data, find))
y.stop()
         
def binary_recursive(data, find, l=0, h=(len(data)-1)):
    if l<h:
        return False
    else:
        mid = (l+h)//2
        if data[mid]==find:
            return True
        elif data[mid]<find:
            return binary_recursive(data,find,mid+1,h)
        elif data[mid]>find:
            return binary_recursive(data,find,l,mid-1)
        
z =ET("recursive")
print(binary_recursive(data,find))
z.stop()