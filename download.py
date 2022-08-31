# -*- coding: utf-8 -*-
import requests
import re

if __name__ == "__main__":

    output_path = 'data/auto-mpg.data'
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data-original'
    r = requests.get(url).content

    with open(output_path, 'wb') as f:
        f.write(r)

    filepath = 'data/auto-mpg.tsv'
    fo = open(filepath, 'w')
    colnames = [
        'mpg', 'cylinders', 'displacement','horsepower',
        'weight', 'acceleration', 'modelyear', 'origin',
        'carname'
    ]
    fo.write('\t'.join(colnames) + '\n')
    with open(output_path, 'r') as f:
        line = f.readline().strip()
        while line:
            line = re.sub(r'\s\s+', '\t', line)
            fo.write(line + '\n')
            line = f.readline().strip()
    fo.close()
