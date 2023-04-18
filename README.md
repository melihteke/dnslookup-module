## DNSLookup
The DNSLookup module provides a simple interface for performing DNS lookups in Python. It allows you to easily retrieve the IP addresses associated with a given domain name.

### Installation
To install the DNSLookup module, simply clone the repository and run the following command:
```sh
git clone https://github.com/melihteke/dnslookup-module.git
```
### Usage
Here's an example of how to use the DNSLookup module to perform a DNS lookup:

```sh
pip install dnslookup-module
```


```sh
(.venv) MTeke1@APKM2W42362BA4 dnslookup-module % ipython
Python 3.8.9 (default, Apr 13 2022, 08:48:06) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.12.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from dnslookup import DNSLookup

In [2]: query = DNSLookup(domain="www.mteke.com")

In [3]: query.get_ip()
Out[3]: ['81.129.175.158']

In [4]: 

```

### API Reference
#### DNSLookup
The DNSLookup class represents a DNS lookup object.

##### Constructor
__init__(self, domain: str) -> None
Creates a new DNSLookup object for performing DNS lookups.

##### Arguments
domain (str): The domain name to look up.

##### Methods
get_ip(self) -> List[str]
Performs a DNS lookup and returns the IP address(es) associated with the domain.

##### Returns
list (str): A list of IP addresses associated with the domain.
Raises
socket.gaierror: If the DNS lookup fails.

