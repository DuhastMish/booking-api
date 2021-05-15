"""This module checks for the required arguments."""
import logging
from enum import Enum
from typing import Dict

from werkzeug.local import LocalProxy


class Arguments(Enum):
    """Available arguments."""

    hotels = {'minimal_price', 'stars', 'city', 'maximal_price', 'minimal_rating'}
    apartaments = {'hotel_id', 'minimal_price', 'maximal_price', 'hotel_beds'}
    extended_rating = {'hotel_id'}
    booking = {'user_id'}
    hotels_post = {'hotel_id', 'apartaments_id', 'date_in', 'date_out'}
    hotel_put = {'booking_id', 'apartaments_id', 'new_date_in', 'new_date_out'}
    booking_delete = {'booking_id'}

    @classmethod
    def members(cls):
        """Return all class attributes."""
        return cls.__members__


def validate_args(request: LocalProxy) -> Dict:
    """Check the request for extra arguments and removes them.

    Args:
        request (LocalProxy): Request to check

    Returns:
        Dict: Accepted Arguments and Their Values
    """
    url_type = request.path.split('/')[-1]

    if url_type not in Arguments.members():
        logging.warning('Can not check requested arguments')
        return {}

    required_arguments = getattr(Arguments, url_type).value
    extra_keys = set(request.args.keys()) - required_arguments

    if extra_keys:
        logging.warning('Found extra arguments for {0}. Removed: {1}'.format(
            request.path,
            ', '.join(extra_keys),
        ))

    return {key: value for key, value in request.args.items() if key in required_arguments}  # noqa: WPS110


def prepare_args(db_class, request: LocalProxy):
    arguments_dict = validate_args(request)
    arguments_list = []

    for argument, arg_value in arguments_dict.items():
        if "minimal" in argument:
            prepeared_arg = argument.split("_")[-1]
            arguments_list.append(getattr(db_class, prepeared_arg) >= arg_value)
        elif "maximal" in argument:
            prepeared_arg = argument.split("_")[-1]
            arguments_list.append(getattr(db_class, prepeared_arg) <= arg_value)
        else:
            arguments_list.append(getattr(db_class, argument) == arg_value)

    return arguments_list
