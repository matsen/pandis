#! /usr/bin/env python

'''
Take a partis CSV file and split each line into CSV files named .family0.csv, .family1.csv, etc.
'''

import collections
import csv
import os
import pandas as pd
import sys

csv.field_size_limit(10000000000000000)

coloned_rows = \
    "unique_ids mut_freqs input_seqs indel_reversed_seqs mutated_invariants in_frames stops".split()

in_name = sys.argv[1]

with open(in_name) as csvfile:
    reader = csv.DictReader(csvfile)
    count = 0

    d = collections.OrderedDict()

    for row in reader:
        for k, v in row.items():
            if k in coloned_rows:
                d[k] = v.split(':')
            elif k == "duplicates":
                d[k] = v.split(';')
            #elif k == "indelfos":
            # support?

        df = pd.DataFrame(d)
        out_name,_ = os.path.splitext(in_name)
        out_name += ".family_{}.csv".format(count)
        df.to_csv(out_name, index=False)

        count += 1
