import os
import yaml
class Yaml:
    def __init__(self,yaml_path):
        self.yaml_path=yaml_path
    def read_yaml(self):
        with open(os.path.abspath(os.path.dirname(__file__)).split("common")[0]+self.yaml_path,"r",encoding="utf-8") as f :
            yaml_value=yaml.load(f,Loader=yaml.FullLoader)
        return yaml_value

# if __name__ == '__main__':
#     print(Yaml("data\data.yaml").read_yaml())

