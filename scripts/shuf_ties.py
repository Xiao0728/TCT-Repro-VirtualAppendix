"""
This file shuffles the sequence of the docnos in TREC qrel/run files for MS MARCO (v1).

stdin: TREC qrel/run file
stdout: TREC qrel/run file with replaced docnos
"""

import fileinput
from hashlib import md5

def trec_iter(inp):
  for line in inp:
    yield line.split()

def main():
  for r in trec_iter(fileinput.input()):
    r[2] = md5(r[2].encode()).hexdigest()[:12]
    print(' '.join(r))

if __name__ == '__main__':
  main()
