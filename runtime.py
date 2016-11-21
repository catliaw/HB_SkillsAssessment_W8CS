def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    [      O(n)     ]


    """
    # Runtime len(s1) = O(1)
    # Runtime len(s2) = O(1)
    if len(s1) != len(s2):
        return False
    #O(2)

    # Runtime for i in range(len(s1)) :
    # len(s1) = O(1)
    # range(len(s1)): O(n) - creates a list of the length of the string to iterate over
    # for i in list: O(n)
    # Runtime for initial for loop itself: O(n) + O(n) + O(1) = O(2n + 1) = O(n)
    for i in range(len(s1)):
        # s1[i] = indexing O(1)
        # s2[i] = indexing O(1)
        # comparison: O(1)
        # total: O(3)
        if s1[i] != s2[i]:
            return False
    # O(n) x O(3) = O(3n) = O(n)

    return True


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    [      O(n)     ]

    """
    # if "hippo" in animals (a list): O(n) - have to iterate over each item to find
    # if "platpypus" in animals (a list): O(n) - same reason
    # if loop itself = O(n) + O(n) = O(2n) => O(n)
    if "hippo" in animals or "platpypus" in animals:
        return True
    else:
        return False


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [     O(n)      ]

    """

    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later

    # O(n)
    s = set(numbers)

    # for loop: O(n)
    for x in s:
        # finding in set: O(1)
        if -x in s:
            # append to list: O(1) x 2 = O(2)
            result.append([-x, x])
        # O(1) + O(2) = O(3)
    # O(n + 3) = O(n)

    # O(n) + O(n) = O(2n) = O(n)

    return result


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [    O(n^2)     ]

    """
    # Creating an empty list: O(1)
    result = []

    # iterating over something: O(n)
    for x in numbers:
        # iterating over something: O(n)
        for y in numbers:
            # comparison: O(1)
            if x == -y:
                # appending tuple to list: O(1)
                result.append((x, y))
        # O(nx1) = O(n)
    #O(nxn+1) = O(n^2)

    return result


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    [     O(n^3)    ]

    """
    # Creating an empty list: O(1)
    result = []

    # iterating over something: O(n) if numbers = 6, n=6
    for x in numbers:
        # iterating over something: O(n) if numbers = 6, n=6
        for y in numbers:
            # comparison: O(1)
            # find in list O(n)
            if x == -y and (y, x) not in result:
                # appending tuple to list: O(1)
                result.append((x, y))
            # O(1+n+1) = O(n+2) = O(n)
        # O(nxn) = O(n^2)
    # O(nxn^2) = O(n^3) is that possible?
    return result
