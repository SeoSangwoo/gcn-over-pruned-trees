#!/bin/bash

SAVE_ID=$1
python train.py --id $SAVE_ID --seed 0 --prune_k 1 --lr 0.7 --rnn_hidden 100 --num_epoch 100 --pooling max --mlp_layers 1 --pooling_l2 0.0002 --alpha 0.3
