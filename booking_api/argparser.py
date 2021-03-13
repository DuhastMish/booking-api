"""This module contains all the possible application arguments."""
import argparse

booking_api_configuration = argparse.ArgumentParser(add_help=True)

booking_api_configuration.add_argument(
    '--debug',
    '-d',
    action='store_true',
    help='This argument switch on debug mode',
)
