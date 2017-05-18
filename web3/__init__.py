from __future__ import absolute_import

#import pkg_resources

from .main import Web3
from .providers.rpc import (
    HTTPProvider,
    RPCProvider,
    KeepAliveRPCProvider,
)
from .providers.tester import (
    TestRPCProvider,
    EthereumTesterProvider,
)
from .providers.ipc import (
    IPCProvider,
)

__version__ = "2.4.0" #pkg_resources.get_distribution("web3").version

__all__ = [
    "__version__",
    "Web3",
    "HTTPProvider",
    "RPCProvider",
    "KeepAliveRPCProvider",
    "IPCProvider",
    "TestRPCProvider",
    "EthereumTesterProvider",
]
