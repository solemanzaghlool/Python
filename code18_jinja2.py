"""This is to demonstrate jinja2 Library"""

import yaml
from rich import print as rprint
from jinja2 import Environment, FileSystemLoader


def pull_yaml(file_dir):
    """Function to pull yaml data"""
    with open(file_dir) as file:
        config_data = yaml.safe_load(file)
        rprint(config_data)
        rprint(config_data["BGP"]["peers"][2])


def generate_config(var_file, templates_folder, template_file):
    """
    Load in host config
    Generate config from data
    """
    with open(var_file) as file:
        my_vars = yaml.safe_load(file)
        env = Environment(
            loader=FileSystemLoader(templates_folder), trim_blocks=True, lstrip_blocks=True
        )
        template = env.get_template(template_file)
        configuration = template.render(my_vars)
        print(configuration)


FILE_YAML = "SupportingFiles/18/R1.yaml"
pull_yaml(FILE_YAML)


BGP_VARS = "SupportingFiles/18/R1.yaml"
TEMPLATES_DIR = "SupportingFiles/18/templates"
BGP_TEMPLATE = "bgp.j2"
generate_config(BGP_VARS, TEMPLATES_DIR, BGP_TEMPLATE)
