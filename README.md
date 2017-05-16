# Web3.py (Google Appengine Fork)

Web3.py package to use in [Google Appengine](https://cloud.google.com/appengine/docs/python/)

Included packages:

* [pylru](https://github.com/mozilla/positron/blob/master/python/pylru/pylru.py)
* [ethereum-utils](https://github.com/pipermerriam/ethereum-utils)

====================================

Sample Code:

```
import logging
from web3 import Web3, RPCProvider

web3rpc = Web3(RPCProvider(host="GETH_SERVER_IP", port="8545")) 

logging.info(web3rpc.eth.blockNumber) #909483
```


======================================

[![Join the chat at https://gitter.im/pipermerriam/web3.py](https://badges.gitter.im/pipermerriam/web3.py.svg)](https://gitter.im/pipermerriam/web3.py?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Build Status](https://travis-ci.org/pipermerriam/web3.py.png)](https://travis-ci.org/pipermerriam/web3.py)
   

A python implementation of [web3.js](https://github.com/ethereum/web3.js)

* Python 2.7, 3.4, 3.5 support

Read more in the [documentation on ReadTheDocs](http://web3py.readthedocs.io/)
