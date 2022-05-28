import os
from types import NotImplementedType
import torch
import numpy as np
import scipy.misc as m

from torch.utils import data

from data.city_utils import recursive_glob
from data.augmentations import *


class NaturalImagesLoader(data.Dataset):
  raise NotImplementedError()
