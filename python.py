'''
Specify gpu ids to be utilised.
Helpful while training multi gpu models on specific gpus/ pytorch pin memory True on gpu id != 0
'''
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

'''
read yaml file as attrdict
'''

from attrdict import AttrDict
import yaml

def read_yaml(yamlFile):
    with open(yamlFile) as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)
        cfg = AttrDict(config)
    return cfg

'''
all file paths from a nested folder
'''

from pathlib import Path

def get_files(path, extension):
    if isinstance(path, str): path = Path(path).expanduser().resolve()
    list(path.rglob(f'*{extension}'))
    return list(path.rglob(f'*{extension}'))
