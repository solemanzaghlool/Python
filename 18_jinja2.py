import yaml
from rich import print as rprint
from jinja2 import Environment, FileSystemLoader

def pull_yaml(file_dir):
    """Function to pull yaml data"""
    config_data = yaml.safe_load(open(file_dir))
    rprint(config_data)
    rprint(config_data["BGP"]["peers"][2])


def generate_config(var_file, templates_folder, template_file):
    """
    Load in host config 
    Generate config from data
    """
    my_vars = yaml.safe_load(open(var_file))
    env= Environment(loader=FileSystemLoader(templates_folder), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(template_file)
    configuration = template.render(my_vars)
    print(configuration)



file_yaml = "SupportingFiles/18/R1.yaml"
pull_yaml(file_yaml)



bgp_vars = "SupportingFiles/18/R1.yaml"
templates_dir = "SupportingFiles/18/templates"
bgp_template = "bgp.j2"
generate_config(bgp_vars, templates_dir, bgp_template)

