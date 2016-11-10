def iq_test(numbers):
    nums = map(int, numbers.split(" "))
    evens, odds = 0, 0
    for i, n  in enumerate(nums):
        if n % 2 == 0:
            evens += 1
            ei = i
        else:
            odds += 1
            oi = i
    
    if evens == 1:
        return ei + 1
    return oi + 1