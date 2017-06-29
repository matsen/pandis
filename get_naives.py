#! /usr/bin/env python

'''
Take a partis CSV file and print the naive sequences. Name them naive0, naive1, etc.
'''

import collections
import csv
import os
import pandas as pd
import sys

csv.field_size_limit(10000000000000000)

in_name = sys.argv[1]

with open(in_name) as csvfile:
    reader = csv.DictReader(csvfile)

    count = 0

    for row in reader:
        print ">naive{}".format(count)
        print row['naive_seq']

        count += 1
