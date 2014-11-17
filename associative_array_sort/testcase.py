#!/usr/bin/env python
import sys
import time
from random import randint

from collections import OrderedDict

MAX_INT = 2**32-1

def run_test(num_entries):
    start = time.time()
    d = { randint(0, MAX_INT) : randint(0, MAX_INT) for count in xrange(num_entries) }
    r = OrderedDict()
    for key in sorted(d):
        r[key] = d[key]
    end = time.time()
    return end-start

if __name__ == "__main__":
    entries = 1
    retries = 5
    print "\t\t\t\t%s\t\tMIN\t\tMAX\t\tAVG" % ("\t\t".join(["%d" % i for i in range(retries)]))
    while entries < 10000000:
        sys.stdout.write("Running with % 10d:\t" % entries)
        sys.stdout.flush()
        results = []
        for retry in range(5):
            results.append(run_test(entries))
            sys.stdout.write("%e\t" % (results[-1]))
            sys.stdout.flush()
        sys.stdout.write("%e\t%e\t%e\n" % (min(results), max(results), sum(results) / 5.0))
        sys.stdout.flush()
        entries = (entries * 2)


