#!/bin/bash

SAVE_ID=$1
python train.py --id $SAVE_ID --seed 0 --prune_k 1 --lr 0.5 --lr_decay 0.95 --rnn_hidden 100 --num_epoch 500 --pooling max --mlp_layers 2 --pooling_l2 0.003 --data_dir dataset/semeval
