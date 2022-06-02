# TCT-Repro-VirtualAppendix

This is the virtual appendix for the SIGIR 2022 reproducibility track paper entitled *An Inspection of the Reproducibility and Replicability of TCT-ColBERT*.

This repository allows the replication of all results reported in the paper. In particular, it provides:
 - results files for all result tables in the paper.
 - Jupyter notebooks reproducing the tables in the paper.
 - model checkpoints for each of the models tested in the paper.
 - scripts to produce indices of MSMARCO from those model checkpoints.
 - scripts to produce the model checkpoints.

## Prerequisites

This guide makes use of:
 - [PyTerrier](https://github.com/terrier-org/pyterrier) using [pyterrier_dr plugin](https://github.com/terrierteam/pyterrier_dr) for dense indexing and retrieval
 - [ir-measures](https://ir-measur.es/) for evaluation

For Python code examples below, we assume the following has already been imported:
```python
import pyterrier as pt ; pt.init()
from pyterrier_dr import TctColBert, NumpyIndex
```

## Evaluation

We use [ir-measures](https://ir-measur.es/) to compute evaluation measures. It uses [trec_eval](https://github.com/usnistgov/trec_eval)'s implementaiton of nDCG@10 and R@1000 and MS MARCO's [RR@10 script](https://github.com/microsoft/MSMARCO-Passage-Ranking/blob/master/ms_marco_eval.py).

```bash
# Command format
ir_measures dataset_or_qrels path_to_run measures

# Example for MS MARCO Dev (small)
ir_measures msmarco-passage/dev/small runs/table-2-last-metre/ours.dev-sm.tct-colbert.run.gz RR@10 R@1000

# Example for TREC DL 2019
ir_measures msmarco-passage/trec-dl-2019 runs/table-3-last-mile/ours.dl19.tct-colbert.run.gz nDCG@10 R@1000
```

## The Last Metre

The "Last Metre" setting tests whether results can be reproduced/replicated when using a built index and pre-computed query vectors.

**Can we reproduce the dense retrieval using released query/doc vectors? (Table 2)**

 - Our run files: [here](runs/table-2-last-metre)
 - Building run files: [instructions from the authors](https://github.com/castorini/pyserini/blob/master/docs/experiments-tct_colbert-v2.md).

## The Last Mile

The "Last Mile" setting tests whether results can re reproduced/replicated when a trained model.

**Can we replicate TCT-ColBERT inference and retrieval using only released models? (Table 3)**

 - Our run files: [here](runs/table-3-last-mile)
 - Indexing:

```python
model = TctColBert("castorini/tct_colbert-v2-msmarco") # or castorini/tct_colbert-v2-hn-msmarco or castorini/tct_colbert-v2-hnp-msmarco
index = NumpyIndex("path/to/my/index", batch_size=100)
dataset = pt.get_dataset("irds:msmarco-passage")
pipeline = model >> index # encode the documents using the TCT-ColBERT model and pass the results to the dense index
pipeline.index(dataset.get_corpus_iter(), batch_size=1000) # perform indexing (this will take time)
```

or create indexes for all 3 variants using:

```bash
bash scripts/table_3_index.sh
```

 - Retrieval:

```python
dataset = pt.get_dataset('irds:msmarco-passage/dev/small') # or irds:msmarco-passage/trec-dl-2019/judged
index = NumpyIndex('path/to/index', verbose=True)
model = TctColBert('castorini/tct_colbert-v2-msmarco') # or castorini/tct_colbert-v2-hn-msmarco or castorini/tct_colbert-v2-hnp-msmarco
pipeline = model >> index # encode the query using the TCT-ColBERT model and query the dense index
res = pipeline(dataset.get_topics())
pt.io.write_results('path/to/run')
```

or query all 3 variants for both datasets using:

```bash
bash scripts/table_3_retr.sh
```

## Citation

```bibtex

@inproceedings{
  author = {Xiao Wang, Sean MacAvaney, Craig Macdonald and Iadh Ounis},
  title = {An Inspection of the Reproducibility and Replicability of TCT-ColBERT},
  booktitle = {Proceedings of SIGIR 2022},
}
```

## Notes

The "shuf-ties" results reported in Table 5 originally used a non-deterministic approach for shuffling. In this appendix, we replaced this with a deterministic
approach. Consequently, the values reported vary slightly, but the conclusions do not change.
