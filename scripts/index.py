import pyterrier as pt ; pt.init()
from pyterrier_sbert import TctColBert, NumpyIndex

def main():
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('model')
  parser.add_argument('target')
  parser.add_argument('dataset')
  args = parser.parse_args()
  model = TctColBert(args.model)
  index = NumpyIndex(args.target, batch_size=100)
  pipeline = model >> index
  pipeline.index(pt.get_dataset(args.dataset).get_corpus_iter(), batch_size=1000)

if __name__ == '__main__':
  main()
