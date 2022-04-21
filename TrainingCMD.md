
# Train the TCT-ColBERT teacher model

```
python ./train/main.py --use_tpu=False \
               --do_train=True \
               --do_eval=True \
               --train_model=teacher \
               --eval_model=teacher \
               --num_train_steps=500000 \
               --bert_pretrained_dir=./uncased_L-12_H-768_A-12 \
               --init_checkpoint=./uncased_L-12_H-768_A-12/bert_model.ckpt \
               --data_dir=./msmarco-passage/tfrecord \
               --train_file=dataset_train_tower.tf \
               --eval_file=dataset_dev_tower.tf \
               --output_dir=./colbert_checkpoint \
               --train_batch_size=32
 ```
 

# Train the TCT-ColBERT student model

- Train the student model using our own trained teacher model (with and without initlisation;

- Train the student model using the author provided teacher checkpoint (without student initialised from teacher)

 ```python ./train/main.py --use_tpu=False \
               --do_train=True \
               --do_eval=True \
               --train_model=student \
               --eval_model=student \
               --num_train_steps=1500000 \
               --bert_pretrained_dir=./uncased_L-12_H-768_A-12 \
               --init_checkpoint=/nfs/sean/tct_colbert_spaces/tct-colbert_checkpoint \
               --data_dir=./msmarco-passage/tfrecord \
               --train_file=dataset_train_tower.tf \
               --eval_file=dataset_dev_tower.tf \
               --output_dir=/nfstrecdl/workspace_xiao/tct_colbert_checkpoint_on_ColBERTcheckpoint \
               --train_batch_size=32
 ```



-  Train the student model using the author provided teacher checkpoint (with student initialised from teacher)



```python ./train/main.py --use_tpu=False \
               --do_train=True \
               --do_eval=True \
               --train_model=student \
               --eval_model=student \
               --num_train_steps=1500000 \
               --bert_pretrained_dir=./uncased_L-12_H-768_A-12 \
               --init_checkpoint=/nfs/sean/tct_colbert_spaces/tct-colbert_checkpoint \
               --data_dir=./msmarco-passage/tfrecord \
               --train_file=dataset_train_tower.tf \
               --eval_file=dataset_dev_tower.tf \
               --output_dir=/nfstrecdl/workspace_xiao/tct_colbert_checkpoint_on_ColBERT_triples_init \
               --train_batch_size=32 
   ```
               
- Train the student model using the author provided teacher checkpoint on the Hard Negative Samples (without initialisation from teacher model)



   ```
   python ./train/main.py --use_tpu=False \
               --do_train=True \
               --do_eval=True \
               --train_model=student \
               --eval_model=student \
               --num_train_steps=1500000 \
               --bert_pretrained_dir=./uncased_L-12_H-768_A-12 \
               --init_checkpoint=/nfs/sean/tct_colbert_spaces/colbert_checkpoint \
               --data_dir=./msmarco-passage/tfrecord \
               --train_file=dataset_train_tower.tf \
               --eval_file=dataset_dev_tower.tf \
               --output_dir=/nfs/sean/workspace_xiao/tct_colbert_checkpoint_on_ColBERTcheckpoint_hnp \
               --train_batch_size=32 
   ```
               
- Train the student model using the author provided teacher checkpoint on the Hard Negative Samples (with initlisation from teacher model)

   ```
   python ./train/main.py --use_tpu=False \
               --do_train=True \
               --do_eval=True \
               --train_model=student \
               --eval_model=student \
               --num_train_steps=1500000 \
               --bert_pretrained_dir=./uncased_L-12_H-768_A-12 \
               --init_checkpoint=/nfs/sean/tct_colbert_spaces/tct-colbert.hnp \
               --data_dir=/nfs/xiao/tct_colbert/msmarco-passage/tfrecord \
               --train_file=dataset_train_tower.tf \
               --eval_file=dataset_dev_tower.tf \
               --output_dir=/nfs/sean/workspace_xiao/tct_colbert_checkpoint_on_ColBERTcheckpoint_hnp_init \
               --train_batch_size=32 
     ```


            
