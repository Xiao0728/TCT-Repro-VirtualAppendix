import pyterrier as pt ; pt.init()
from pyterrier_dr import TctColBert, NumpyIndex

def main():
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('model')
  parser.add_argument('index')
  parser.add_argument('dataset')
  parser.add_argument('out')
  args = parser.parse_args()
  index = NumpyIndex(args.index, verbose=True)
  model = TctColBert(args.model)
  dataset = pt.get_dataset(args.dataset)
  pipeline = model >> index
  res = pipeline(dataset.get_topics())
  pt.io.write_results(res, args.out)

if __name__ == '__main__':
  main()
