#import pkg_resources

from .abi import (  # NOQA
    decode_single,
    decode_abi,
    encode_single,
    encode_abi,
)


__version__ = "0.4.0" #pkg_resources.get_distribution('ethereum-abi-utils').version
