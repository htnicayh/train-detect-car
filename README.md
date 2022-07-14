### Training Detect Car Models

- Starting train
```bash
cd yolov5
python train.py --img 416 --batch 16 --epochs 1000 \ 
  --data ../custom/custom_dataset.yaml \
  --cfg ../custom/custom_model.yaml \
  --weights '' --name model --cache
```
