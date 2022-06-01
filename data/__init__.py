import json

from data.base import *
from data.cityscapes_loader import cityscapesLoader
from data.gta5_dataset import GTA5DataSet
from data.synthia_dataset import SynthiaDataSet
from data.naturalImages_loader import NaturalImagesLoader


def get_loader(name):
    """get_loader
    :param name:
    """
    return {
        "cityscapes": cityscapesLoader,
        "gta": GTA5DataSet,
        "synthia": SynthiaDataSet,
        "natural": NaturalImagesLoader
    }[name]

def get_data_path(name):
    """get_data_path
    :param name:
    :param config_file:
    """
    if name == 'cityscapes':
        return '../data/CityScapes/'
    if name == 'gta' or name == 'gtaUniform':
        return '../data/gta/'
    if name == 'synthia':
        return '../data/RAND_CITYSCAPES'
    if name == 'natural':
        return '/content/drive/MyDrive/Colab Notebooks/maya.ai/DACS/data/NaturalImages/'
