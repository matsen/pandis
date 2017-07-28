#!/usr/bin/env python

'''
Export "healthy" sequences to a FASTA.
The definition of healthy is below.
'''

import os
import pandas as pd
import sys

in_path = sys.argv[1]
df = pd.read_csv(in_path)

df['has_indel'] = df['indel_reversed_seqs'].notnull()

# Add sequences without indels to indel_reversed_seqs.
for index, row in df.iterrows():
    if not row['has_indel']:
	df.loc[index, 'indel_reversed_seqs'] = df.loc[index, 'input_seqs']

# Here is our definition of healthy.
df['healthy'] = df['in_frames'] & (~ df['stops']) & (~ df['mutated_invariants'])

out_path, _ = os.path.splitext(in_path)
out_path += '.healthy.fasta'

with open(out_path, 'w') as out_f:
    for _, row in df.iterrows():
        if not row['healthy']: continue
    	out_f.write('>{}\n'.format(row['unique_ids']))
    	out_f.write('{}\n'.format(row['indel_reversed_seqs']))
