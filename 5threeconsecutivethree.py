# Return True if a list contains two consecutive threes (3 next to a 3) anywhere within the list
def has_consecutive_threes(num_list):
    # check for consecutive threes
    for i in range(len(num_list) - 1):
        if num_list[i] == 3 and num_list[i + 1] == 3:
            return True

    # If no consecutive threes found, return False
    return False

print(has_consecutive_threes([1, 2, 3, 3, 5]))
print(has_consecutive_threes([1, 2, 4, 5, 6]))