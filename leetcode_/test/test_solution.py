#!/usr/bin/python3

# linux pip3 install pytest pytest-benchmark

import sys, os, time
myPath = os.path.dirname(os.path.abspath(__file__))
print("myPath", myPath)
sys.path.insert(0, myPath + '/../')

from libs.leetCode39_hash_Find_Words_That_Can_Be_Formed_by_Characters import Solution

def something(duration=0.000001):
    """
    Function that needs some serious benchmarking.
    """
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    solution = Solution()
    solution.init(words, chars)
    return solution.count()

def test_my_stuff(benchmark):
    # benchmark something
    result = benchmark(something)

    # Extra code, to verify that the run completed correctly.
    # Sometimes you may want to check the result, fast functions
    # are no good if they return incorrect results :-)
    assert result == 6