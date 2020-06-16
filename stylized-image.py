from models import TransformerNet
from utils import *
import torch
from torch.autograd import Variable
import argparse
import os
import tqdm
import sys
from torchvision.utils import save_image
from PIL import Image

if __name__ == "__main__":
    image_path=sys.argv[1]
    model_path=sys.argv[2]
	
    os.makedirs("images/outputs", exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    transform = style_transform()

    # 定义生成网络并且加载训练好的模型
    transformer = TransformerNet().to(device)
    transformer.load_state_dict(torch.load(model_path))
    transformer.eval()

    # 将要进行转换的内容图片进行张量化准备
    image_tensor = Variable(transform(Image.open(image_path))).to(device)
    image_tensor = image_tensor.unsqueeze(0)

    # 进行风格迁移
    with torch.no_grad():
        stylized_image = denormalize(transformer(image_tensor)).cpu()

    # 保存图片
    fn = image_path.split("/")[-1]
    sn = model_path.split("/")[-1]
    save_image(stylized_image, f"images/outputs/{sn}-{fn}")
