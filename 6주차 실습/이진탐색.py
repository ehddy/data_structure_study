def binary_search(left, right, t, list):

    if left > right: 
        return None 

    mid = (left + right) // 2  
    
    if list[mid] == t: 
        return mid
    
    if list[mid] > t:
        binary_search(left, mid-1, t) # 앞부분 탐색 
    
    else:
        binary_search(mid+1, right, t) # 뒷부분 탐색 


a = [20, 30, 40, 45, 48, 50, 55]


binary_search(0, 6, 40, a)