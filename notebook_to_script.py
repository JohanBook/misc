"""
Print notebook python code to stdout
"""
import yaml


def read_yaml(path):
    with open(path, "r") as file:
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as error:
            raise error


def cells_to_script(cells):
    scripts = []
    for cell in cells:
        if cell['cell_type'] != 'code':
            continue;
        string = ''
        for line in cell['source']:
            string += line
        scripts.append(string)
    return "\n".join(scripts)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description="Extract Python scripts from a Jupyter notebook",
        add_help=True
    )
    parser.add_argument('path', type=str, help="path to notebook file")
    args = parser.parse_args()

    cells = read_yaml(args.path)['cells']
    script = cells_to_script(cells);
    print(script)
