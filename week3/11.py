def spy_game(nums):
    for i in range(0,len(nums)):
        if nums[i] == 0:
            for x in range(i+1,len(nums)):
                if nums[x] == 0:
                    for y in range(x+1,len(nums)):
                        if nums[y] == 7:
                            return True
                else:
                    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))