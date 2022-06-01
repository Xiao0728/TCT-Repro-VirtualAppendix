# TCT-Repro-VirtualAppendix

This is the virtual appendix for the SIGIR 2022 reproducibility track paper entitled *An Inspection of the Reproducibility and Replicability of TCT-ColBERT*.

This repository allows the replication of all results reported in the paper. In particular, it provides:
 - results files for all result tables in the paper.
 - Jupyter notebooks reproducing the tables in the paper.
 - model checkpoints for each of the models tested in the paper.
 - scripts to produce indices of MSMARCO from those model checkpoints.
 - scripts to produce the model checkpoints.

## Prerequisites

This codebase makes use of:
 - [PyTerrier](https://github.com/terrier-org/pyterrier)

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
