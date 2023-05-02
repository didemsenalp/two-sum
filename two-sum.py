def twoSum(nums, target):
    if (2 <= len(nums) <= (10 ** 4) and (-10 ** 9) <= target <= (10 ** 9)):
        for i in range(len(nums)):
            if((-10 ** 9) <= int(nums[i]) <= (10 ** 9)):
                for j in range(i + 1, len(nums)):
                    print(i,j)
                    print(int(nums[i]),int(nums[j]),target)
                    print(int(nums[i]) + int(nums[j]) == target,i != j )
                    if (i != j and int(nums[i]) + int(nums[j]) == target):
                        print(i,j)
        return (i, j)







twoSum(nums = list(input("Lütfen sayı değerlerini giriniz:")),target = int(input("Hedef değerini giriniz:")))

