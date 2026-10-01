# create a class
class pair_elements:

    def twosum(self, nums, target):
        # Create an empty dictoinary
        lookup = {}

        # Iterate through tuple
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num],i)
            lookup[num] = i

# Will take input of dum from user 
value = int(input("Enter sum for which you want to make this search: "))
print("index1=%d, index2=%d" % pair_elements().twosum((10,20,30,40,50,60,70),value))