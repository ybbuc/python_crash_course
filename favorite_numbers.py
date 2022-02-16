favorite_nums = {
    'james': [1],
    'joe': [7, 8, 9],
    'jim': [13, 19],
    'jane': [3],
    'jill': [17, 11, 5, 3],
}

for name, nums in favorite_nums.items():
    if len(nums) == 1:
        print("\n" + name.title() + "'s favorite number is:")
        for num in nums:
            print("\t" + str(num))
    else:
        print(f"\n{name.title()}'s favorite numbers are:")
        for num in nums:
            print("\t" + str(num))
