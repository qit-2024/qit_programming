# primes.py - compute/count prime numbers for specific range
import argparse
from math import ceil, log2
from copy import copy
from time import time


def compute_primes(max_number_of_primes:int or None=None,
                   max_range_for_primes:int or None=None,
                   precomputed: list[int] or None=None) -> list[int]:
    # NOTE: allow for behavior customization by
    if max_number_of_primes is not None:
        assert(max_number_of_primes >= 1)
        # NOTE: in case max_number_of_primes will exceed hardcoded integer limit,
        # will exit anyways
        pass
    if max_range_for_primes is not None:
        assert(max_range_for_primes >= 2)
        # NOTE: python's int is a 32-bit signed integer type
        # able to represent approx. +-2e9 values
        # Regardless, will limit it to 1e9 values
        assert(max_range_for_primes <= 1e9)
        pass

    # Handle trivial cases
    if max_number_of_primes == 1 or \
       max_range_for_primes == 2:
        return [2]
    elif max_number_of_primes == 2 or \
         max_range_for_primes == 3:
        return [2, 3]

    # Need to handle also first odd prime, as will look for primes starting from the last odd number
    if max_range_for_primes is None and max_number_of_primes is None:
        # NOTE: there's no class derivation which handles "logic errors" (similar to C++11?)
        raise SyntaxError("Invalid function call: expected either or both positional arguments; none provided")
    elif max_range_for_primes is None:
        # Note: hardcoded limit is 1e9
        # maximum range could be increased with e.g. numpy library implementation for 
        max_range_for_primes = int(1e9)
        pass
    elif max_number_of_primes is None:
        # NOTE: there's slightly less than 51 million primes in range up to 1 billion
        max_number_of_primes = 51e6
        pass

    # if precomputed primes array is provided:
    if precomputed is None:
        primes = [2, 3]
    else:
        primes = precomputed
        if len(precomputed) >= max_number_of_primes:
            # return slice of precomputed primes array
            return primes[0:max_number_of_primes]
        elif precomputed[-1] > max_range_for_primes:
            # Assuming precomputed primes are of  utilize binary search to find index of the last applicable prime candidate
            (left, right) = (0, len(precomputed) - 1)
            # have learned about // - floor division shortcut
            for i in range(1, ceil(log2(len(precomputed)))):
                middle = (left + right) // 2
                if primes[middle] > max_range_for_primes:
                    right = middle
                else:
                    left = middle
            # if still haven't found - signal an error
            if primes[middle] > max_range_for_primes:
                raise RuntimeError("Binary search of last candidate through precomputed primes failed!")
            else:
                return primes[0:middle+1]
        pass

    # At this point, normal primes search procedure shall be executed
    # initialize/instantiate `candidate_prime` variable
    candidate_prime = primes[-1]
    # Index variable used in stop condition for searching prime
    sqrt_prime_index = 1

    while True:
        candidate_prime += 2
        if candidate_prime > max_range_for_primes:
            return primes
        elif len(primes) >= max_number_of_primes:
            return primes

        # check if stop-condition index variable should be iterated
        temp_stop_value = primes[sqrt_prime_index]
        while temp_stop_value * temp_stop_value <= candidate_prime:
            sqrt_prime_index += 1
            temp_stop_value = primes[sqrt_prime_index]
            pass

        # stop-condition is up-to-date, proceed with searching
        divisor_found = False
        for i in range(sqrt_prime_index + 1):
            if candidate_prime % primes[i] == 0:
                divisor_found = True
                break
            else:  # note: redundant, leaving for readability
                continue

        if divisor_found:
            continue
        else:
            primes.append(candidate_prime)
        continue
    pass


if __name__ == "__main__":
    tic = time()

    parser = argparse.ArgumentParser(description="compute or count primes for specific numberic range",
                                     epilog="NOTE: current hard-coded range limit for computing primes is 1 billion")
    
    parser.add_argument("-c", "--count", action="store_true",
                        help="Print number of primes for the range specified, and exit immediately",
                        required=False)
    parser.add_argument("-l", "--lower-bound", type=int, default=None, required=False,
                        help="Lower range bound for the primes")
    parser.add_argument("-u", "--upper-bound", type=int, default=None, required=False,
                        help="Upper range bound for the primes to stop at. Complementary (nonexclusive) to \"--max-number\" argument, if given.")
    parser.add_argument("-m", "--max-number", type=int, default=None, required=False,
                        help="Maximum number of primes to compute. Complementary (nonexclusive) to \"--upper-range\" argument, if given.")
    # Implicitly parse program arguments
    args = parser.parse_args()

    precomputed = None
    filename = "primes"
    if args.lower_bound is not None:
        assert(1 < args.lower_bound < 1e9)
        precomputed = compute_primes(max_range_for_primes=args.lower_bound)
        filename = filename + ("_low_{}".format(args.lower_bound))
        pass

    if args.upper_bound is not None:
        assert(2 <= args.upper_bound <= 1e9)
        filename = filename + ("_up_{}".format(args.upper_bound))
        if args.lower_bound is not None:
            assert(args.upper_bound > args.lower_bound)
        pass

    if args.max_number is not None:
        assert(1 <= args.max_number <= 51e6)
        filename = filename + ("_max_{}".format(args.max_number))
        pass


    primes = compute_primes(max_number_of_primes=args.max_number if precomputed is None or args.max_number is None \
                                                                  else args.max_number + len(precomputed),
                            max_range_for_primes=args.upper_bound,
                            precomputed=None if precomputed is None else copy(precomputed))

    # print(precomputed)
    # print(primes)

    toc = time()
    tictoc_diff = toc - tic
    print("Execution took {:.0f} seconds, {:.0f} milliseconds.".format(tictoc_diff // 1,
                                                               (tictoc_diff - (tictoc_diff // 1))*1000))

    filename = filename + ("_num_{}".format(len(primes)))
    filename = filename + ".txt"


    if precomputed is not None:
        primes = primes[len(precomputed)::]
        pass
    if args.count:
        print("There are {} primes for specified constraints.".format(len(primes)))
    else:
        print("Opening file for writing: \"{}\"".format(filename))
        output = open(file=filename, mode="w")
        # print(primes)
        for prime in primes:
            output.write("{}\n".format(prime))
        output.close()
        pass

    exit(code=len(primes))
    raise RuntimeError("Should not be in here!")