import os
import torch
import torchvision.transforms as transforms
import torchvision.datasets as datasets

def get_imagenet_data_loader(image_size=224, batch_size=128):
    assert image_size <= 256, "Image size cannot be larger than 256"

    train_dir = "/home/jorgen/projects/imagenet/ILSVRC2012_images/train/"

    train_dataset = datasets.ImageFolder(
        train_dir,
        transforms.Compose([
            transforms.RandomResizedCrop(image_size),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
        ])
    )

    train_loader = torch.utils.data.DataLoader(
        train_dataset, 
        batch_size=batch_size, 
        shuffle=True,
        num_workers=4
        #pin_memory=True
    )

    return train_loader


if __name__ == "__main__":
    train_loader = get_imagenet_data_loader(batch_size=128)
    print(len(train_loader))

    for i, (images, labels) in enumerate(train_loader):
        print(type(images))
        print(type(labels))
        print(images.shape)
        print(labels.shape)
        print(images.dtype)
        print(labels.dtype)
        print(images.max())
        print(images.min())
        print(labels.max())
        print(labels.min())
        break
