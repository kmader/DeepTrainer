import os
import argparse

parser = argparse.ArgumentParser(description='DIGITS server')

parser.add_argument(
    '-p', '--port',
    type=int,
    default=5000,
    help='Port to run app on (default 5000)'
)
args = vars(parser.parse_args())
base_prefix = '{}proxy/{}/'.format(os.environ['JUPYTERHUB_SERVICE_PREFIX'], args['port'])
