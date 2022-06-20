import os

import yaml
def get_object_path():
    return os.path.dirname(__file__).split("common")[0]
def read_yaml(yaml_path):
    with open(get_object_path()+yaml_path,mode="r",encoding="utf-8") as f:
        value=yaml.load(f,Loader=yaml.FullLoader)
        return value

#
# if __name__ == '__main__':
#     read_yaml(r"/data/test1.yaml")