import json

from requests import post


CONFIGS = None
TEMPLATE = 'https://maker.ifttt.com/trigger/{event:s}/with/key/{key:s}'
VALUES = (
    'value1',
    'value2',
    'value3',
)


def maybe_load_configs(args):
    global CONFIGS
    if CONFIGS is not None:
        return

    if args.config_path is None:
        return

    with open(args.config_path, 'r') as f:
        CONFIGS = json.load(f)


def IFTTT(*values):
    url = TEMPLATE.format(**CONFIGS)
    payload = dict(zip(VALUES, values))
    response = post(
        url,
        data=json.dumps(payload),
    )