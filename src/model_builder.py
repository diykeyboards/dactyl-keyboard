import os
import copy
import importlib
from generate_configuration import *


base = shape_config

# The below array tells the generator what model variants to iterate.
# Keep in mind that each variation is multiplied by the others. It can get massive pretty quickly.
config_options = [
    {
        'name': '{}', 'vars': ['ball_side'], # Set ball side to both, as other half can come from other renders.
        'vals': ['both'],
        'val_names': ['']
    },
    {
        'name': '{}x{}', 'vars': ['nrows', 'ncols'],
        'vals': [(4, 5), (4, 6), (5, 6), (5, 7), (6, 6), (6, 7)], # Row/Column layouts to iterate.
    },
    {
        'name': '{}', 'vars': ['plate_style'],
        'vals': ['NOTCH', 'HS-NOTCH'], # Plate styles to be iterated.
        'val_names': ['MX-NOTCH', 'HOTSWAP'],
        # 'vals': ['HOLE','NUB', 'HS-NUB', 'HS-NOTCH', 'HS-UNDERCUT', 'NOTCH', 'HS-NOTCH'],
    },
    {
        'name': '{}', 'vars': ['thumb_style'],
        'vals': ['DEFAULT', 'MINI', 'CARBONFET', 'MINIDOX', 'TRACKBALL_WILD', 'TRACKBALL_BTU'], # Thumb styles to be iterated.
        'val_names': ['DEFAULT', 'MINI', 'CARBONFET', 'MINIDOX', 'TB-WILD', 'TB-BTU'] # Corresponding names of styles output in filenames.
        # 'DEFAULT' 6-key, 'MINI' 5-key, 'CARBONFET' 6-key, 'MINIDOX' 3-key,
        #'TRACKBALL_ORBYL', 'TRACKBALL_CJ', 'TRACKBALL_WILD', 'TRACKBALL_BTU'
    },
    {
        'name': '{}', 'vars': ['oled_mount_type'],
        'vals': ['CLIP', 'NONE'], # OLED screen mount styles to be iterated.
        'val_names': ['OLED', 'NO-LED'] # Corresponding names of styles output in filenames.
    },
    #{
    #    'name': '{}CTRL', 'vars': ['controller_mount_type'],
    #    'vals': ['EXTERNAL', 'RJ9_USB_WALL'], # Controller mount styles to be iterated.
    #    'val_names': ['EXT', 'DEF'],  # Corresponding names of styles output in filenames.
    #},
]


def create_config(config_options):
    configurations = [{
        'config_name': 'DM',
        'save_dir': 'DM',
    }]
    config_options = copy.deepcopy(config_options)
    for opt in config_options:
        new_configurations = []
        for config in configurations:
            # config['vals'] = []
            for i_vals, vals in enumerate(opt['vals']):
                temp_opt = copy.deepcopy(opt)
                new_config = copy.deepcopy(config)
                if len(temp_opt['vars']) == 1:
                    vals=[vals]
                    if 'val_names' in temp_opt:
                        temp_opt['val_names'][i_vals] = [temp_opt['val_names'][i_vals]]
                for i_val, val in enumerate(vals):
                    new_config[opt['vars'][i_val]] = val


                if 'val_names' in temp_opt:
                    n_input = temp_opt['val_names'][i_vals]
                else:
                    n_input = vals

                name_ext = temp_opt['name'].format(*n_input)
                if not name_ext == '':
                    new_config['config_name'] += "_" + name_ext
                new_config['save_dir'] = new_config['config_name']
                new_configurations.append(new_config)
        configurations = new_configurations

    return configurations



def build_release(base, configurations, engines=('cadquery')): # Choose generation engines: 'solid','cadquery'
    init = True
    for config in configurations:
        shape_config = copy.deepcopy(base)
        for item in config:
            shape_config[item] = config[item]

        for engine in engines:
            shape_config['ENGINE'] = engine
            with open('run_config.json', mode='w') as fid:
                json.dump(shape_config, fid, indent=4)

            if init:
                import dactyl_manuform as dactyl_manuform
                dactyl_manuform.make_dactyl()
                #init = False # This should be enabled but causes Docker error.
            else:
                importlib.reload(dactyl_manuform)
                dactyl_manuform.make_dactyl()

if __name__ == '__main__':
    configurations = create_config(config_options)

    ENGINES = ['cadquery'] # Choose generation engines: 'solid','cadquery'

    build_release(base, configurations, ENGINES)
