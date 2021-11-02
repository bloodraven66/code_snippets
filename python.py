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
save torch model
'''

'''
load torch model
'''
def load_pretrained(path, model, device='cuda:1'):
    model.load_state_dict(torch.load(path,  map_location=device))
    return model
