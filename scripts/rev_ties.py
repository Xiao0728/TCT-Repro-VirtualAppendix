"""
This file reverses the sequence of the docnos in TREC qrel/run files for MS MARCO (v1),
such that lower docnos correspond with those that are higher in the original corpus, and vise versa.

stdin: TREC qrel/run file
stdout: TREC qrel/run file with replaced docnos
"""

import fileinput

def trec_iter(inp):
  for line in inp:
    yield line.split()

def main():
  for r in trec_iter(fileinput.input()):
    r[2] = str(10_000_000 - int(r[2]))
    print(' '.join(r))

if __name__ == '__main__':
  main()
