import argparse


api_site_configuration = argparse.ArgumentParser(add_help=True)

api_site_configuration.add_argument(
    '--debug', '-d',
    action='store_true',
    help='This argument switch on debug mod',
)
