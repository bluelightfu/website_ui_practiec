arr = [5,8,3,4,2]

def merge(left,right):
    res = []
    while len(left) and len(right):
        if(left[0] < right[0]):
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res = res + left if len(left) else res+right
    return res


def sort(arr):
    if len(arr) < 2 :
        return arr
    mid = len(arr)//2
    l = arr[:mid]
    r = arr[mid:]

    return merge(sort(l),sort(r))

print(sort(arr))