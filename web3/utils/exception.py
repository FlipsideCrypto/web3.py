import sys


# raise MyException() from original_exception compatibility
if sys.version_info.major == 2:
    from web3.utils.exception_py2 import raise_from  # noqa: F401
else:
    from web3.utils.exception_py3 import raise_from  # noqa: F401
