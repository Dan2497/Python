nums = [4, 9, 2, 17, 53, 25, 1, 30, 7]

def mergesort(nums):
    if len(nums) > 1:
        #find the midpoint
        mid = len(nums) // 2

        #split
        l = nums[:mid]
        r = nums[mid:]

        #recursive call to split until arr length...
        mergesort(l)
        mergesort(r)
        
        l_mark = 0
        r_mark = 0
        place = 0

        #sort the two lists into one
        while l_mark < len(l) and r_mark < len(r):
            if l[l_mark] < r[r_mark]:
                nums[place]=(l[l_mark])
                l_mark += 1
            else:
                nums[place]=(r[r_mark])
                r_mark += 1
            place += 1

        #Insert remaining elements from the list with largest element
        while l_mark < len(l):
            nums[place]=(l[l_mark])
            l_mark += 1
            place += 1
            
        while r_mark < len(r):
            nums[place]=(r[r_mark])
            r_mark += 1
            place += 1

mergesort(nums)
print(nums)
 
