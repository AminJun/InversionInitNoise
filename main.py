import pdb

import torch
import torchvision
from tqdm import tqdm

from imagenet import ImageNetMultiVariate


def main():
    d = ImageNetMultiVariate()
    images = [torch.cat([d[i].sample().view(1, 3, 224 // 4, 224 // 4) for i in range(len(d))]) for _ in
              tqdm(range(len(d)))]
    pdb.set_trace()
    torchvision.utils.save_image(torch.cat(images), 'examples/samples.png', nrow=len(d))


if __name__ == '__main__':
    main()
