#!/bin/bash
echo starting
cd neuraltalk2
#th eval.lua -model "model_id.t7" -num_images 10  -image_folder "data" -input_json coco/output.json -gpuid -1
th train.lua -checkpoint_path "checkpoint" -cnn_model "model/VGG_ILSVRC_16_layers.caffemodel" -max_iters 30000 -seq_per_img 3  -input_h5 coco/output.h5 -input_json coco/output.json -save_checkpoint_every 300 -gpuid -1
cd ..
echo ending
th train2.lua -max_iters 30000 -seq_per_img 3  -input_h5 coco/output.h5 -input_json coco/output.json -save_checkpoint_every 300 -gpuid -1
