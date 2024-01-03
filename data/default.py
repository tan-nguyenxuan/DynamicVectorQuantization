from easydict import EasyDict as edict

DefaultDataPath = edict()

DefaultDataPath.ImageNet = edict()

# DefaultDataPath.ImageNet.root = "Your Data Path/Datasets/ImageNet"
# DefaultDataPath.ImageNet.train_write_root = "Your Data Path/Datasets/ImageNet/train"
# DefaultDataPath.ImageNet.val_write_root = "Your Data Path/Datasets/ImageNet/val"

DefaultDataPath.ImageNet.root = "/content/drive/My Drive/DynamicVectorQuantization/Datasets/ImageNet"
DefaultDataPath.ImageNet.train_write_root = "/content/drive/My Drive/DynamicVectorQuantization/Datasets/ImageNet/train"
DefaultDataPath.ImageNet.val_write_root = "/content/drive/My Drive/DynamicVectorQuantization/Datasets/ImageNet/val"