"""
Print notebook python code to stdout
"""
import argparse
import yaml

parser = argparse.ArgumentParser()
parser.add_argument('path', type=str)
args = parser.parse_args()


def read_yaml(path):
    with open(path, "r") as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as error:
            raise error


if __name__ == '__main__':
    data = read_yaml(args.path)['cells']
    for d in data:
        if d['cell_type'] == 'code':
            string = ''
            for line in d['source']:
                string += line
            print(string, '\n')
