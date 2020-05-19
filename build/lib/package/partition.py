
def partition(nums, left, right):

    pivot = nums[left]
    i = left + 1
    j = i
    
    while j <= right:
        curr = nums[j]

        if curr <= pivot:
            inter = curr
            nums[j] = nums[i]
            nums[i] = inter
            i += 1
        j += 1
        
    inter = nums[i-1]
    nums[i-1] = pivot
    nums[left] = inter

    return i - 1

#nums = [3, 7, 8, 2, 1]

#print(partition(nums, 0, len(nums)-1))
      
