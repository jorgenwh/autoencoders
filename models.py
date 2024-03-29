import torch
import torch.nn as nn
import torch.nn.functional as F


class MLPEncoder(nn.Module):
    def __init__(self, input_dim, latent_dim):
        super(MLPEncoder, self).__init__()
        self.fc1 = nn.Linear(input_dim, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, latent_dim)

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        x = F.relu(x)
        return x


class MLPDecoder(nn.Module):
    def __init__(self, latent_dim, output_dim):
        super(MLPDecoder, self).__init__()
        self.fc1 = nn.Linear(latent_dim, 128)
        self.fc2 = nn.Linear(128, 256)
        self.fc3 = nn.Linear(256, output_dim)

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        x = F.sigmoid(x)
        return x


class MLPAutoEncoder(nn.Module):
    def __init__(self, input_dim=784, latent_dim=3):
        super(MLPAutoEncoder, self).__init__()
        self.encoder = MLPEncoder(input_dim, latent_dim)
        self.decoder = MLPDecoder(latent_dim, input_dim)

    def encode(self, x):
        return self.encoder(x)

    def decode(self, x):
        return self.decoder(x)

    def forward(self, x):
        x = self.encode(x)
        x = self.decode(x)
        return x


class ConvEncoder(nn.Module):
    def __init__(self):
        super(ConvEncoder, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=2, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=2, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=7, stride=1, padding=0)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = self.conv3(x)
        x = F.relu(x)
        return x


class ConvDecoder(nn.Module):
    def __init__(self):
        super(ConvDecoder, self).__init__()
        self.conv1 = nn.ConvTranspose2d(128, 64, kernel_size=7, stride=1, padding=0)
        self.conv2 = nn.ConvTranspose2d(64, 32, kernel_size=3, stride=2, padding=1, output_padding=1)
        self.conv3 = nn.ConvTranspose2d(32, 1, kernel_size=3, stride=2, padding=1, output_padding=1)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = self.conv3(x)
        x = F.sigmoid(x)
        return x


class ConvAutoEncoder(nn.Module):
    def __init__(self):
        super(ConvAutoEncoder, self).__init__()
        self.encoder = ConvEncoder()
        self.decoder = ConvDecoder()

    def encode(self, x):
        return self.encoder(x)

    def decode(self, x):
        return self.decoder(x)

    def forward(self, x):
        x = self.encode(x)
        x = self.decode(x)
        return x


class ConvUpscaleAutoEncoder(nn.Module):
    def __init__(self):
        super(ConvUpscaleAutoEncoder, self).__init__()
        self.conv1 = nn.ConvTranspose2d(1, 32, kernel_size=3, stride=1, padding=0, output_padding=0, dilation=1)
        self.conv2 = nn.ConvTranspose2d(32, 64, kernel_size=3, stride=1, padding=0, output_padding=0, dilation=1)
        self.conv3 = nn.ConvTranspose2d(64, 128, kernel_size=3, stride=1, padding=0, output_padding=0, dilation=1)
        self.conv4 = nn.ConvTranspose2d(128, 256, kernel_size=3, stride=1, padding=0, output_padding=0, dilation=1)
        self.conv5 = nn.ConvTranspose2d(256, 512, kernel_size=3, stride=1, padding=0, output_padding=0, dilation=1)
        self.conv6 = nn.ConvTranspose2d(512, 256, kernel_size=3, stride=1, padding=0, output_padding=0, dilation=1)
        self.conv7 = nn.ConvTranspose2d(256, 128, kernel_size=3, stride=1, padding=0, output_padding=0, dilation=1)
        self.conv8 = nn.ConvTranspose2d(128, 64, kernel_size=3, stride=1, padding=0, output_padding=0, dilation=1)
        self.conv9 = nn.ConvTranspose2d(64, 1, kernel_size=3, stride=1, padding=0, output_padding=0, dilation=1)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = self.conv3(x)
        x = F.relu(x)
        x = self.conv4(x)
        x = F.relu(x)
        x = self.conv5(x)
        x = F.relu(x)
        x = self.conv6(x)
        x = F.relu(x)
        x = self.conv7(x)
        x = F.relu(x)
        x = self.conv8(x)
        x = F.relu(x)
        x = self.conv9(x)
        x = F.sigmoid(x)
        return x


class ColorizationNet(nn.Module):
    def __init__(self):
        super(ColorizationNet, self).__init__()
        self.conv1 = nn.Conv2d(1, 64, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(128, 256, kernel_size=3, stride=1, padding=1)
        self.conv4 = nn.Conv2d(256, 512, kernel_size=3, stride=1, padding=1)
        self.conv5 = nn.Conv2d(512, 1024, kernel_size=3, stride=1, padding=1)
        self.conv6 = nn.Conv2d(1024, 512, kernel_size=3, stride=1, padding=1)
        self.conv7 = nn.Conv2d(512, 256, kernel_size=3, stride=1, padding=1)
        self.conv8 = nn.Conv2d(256, 128, kernel_size=3, stride=1, padding=1)
        self.conv9 = nn.Conv2d(128, 64, kernel_size=3, stride=1, padding=1)
        self.conv10 = nn.Conv2d(64, 3, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        print(x.shape)
        x = self.conv1(x)
        x = F.relu(x)
        print(x.shape)
        x = self.conv2(x)
        x = F.relu(x)
        print(x.shape)
        x = self.conv3(x)
        x = F.relu(x)
        print(x.shape)
        x = self.conv4(x)
        x = F.relu(x)
        print(x.shape)
        x = self.conv5(x)
        x = F.relu(x)
        print(x.shape)
        x = self.conv6(x)
        x = F.relu(x)
        print(x.shape)
        x = self.conv7(x)
        x = F.relu(x)
        print(x.shape)
        x = self.conv8(x)
        x = F.relu(x)
        print(x.shape)
        x = self.conv9(x)
        x = F.relu(x)
        print(x.shape)
        x = self.conv10(x)
        x = F.sigmoid(x)
        print(x.shape)
        return x