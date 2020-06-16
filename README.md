# Fast-style-transfer-with-GUI

![华师校门](https://github.com/Ryammmmm/Fast-style-transfer-with-GUI/blob/master/images/outputs/%E5%8D%8E%E5%B8%88%E6%A0%A1%E9%97%A8/All.jpg)

我们在上面的models文件夹中放了9个我们训练好的模型，可以直接运行gui.py文件来使用这些模型生成图像。

## Stylized-image

```
python gui.py

```
![gui界面](https://github.com/Ryammmmm/Fast-style-transfer-with-GUI/blob/master/images/gui.png)

## Train
自己训练的时候要先找数据集。
推荐数据集大小要大于4W张图片
```
python train.py   --dataset_path <path-to-dataset> \
                  --style_image <path-to-style-image> \
                  --epochs 1 \
                  --batch_size 4 \
                  --image_size 256
```
