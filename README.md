----------------------------------------------------------------------------------

# Info

*A simple API for simple people*


FedSearch is a Database search API for free but this is for the **PAID** API Version

This project is being worked on live so have fun looking at it 


Workers :
- HellSec
- NanoSec
- Scoot
- Cruel
- George

----------------------------------------------------------------------------------

# Examples

----------------------------------------------------------------------------------

Simple Search
```python3
from fedsearch import Api

# Configuration
API_KEY = ' '
QUERY = ' '

try:
    # Search & Output Results
    search = Api.search(API_KEY, QUERY)
    print(search)
except Exception as e:
    # Print any Errors
    print(e)
```


----------------------------------------------------------------------------------

Database Count Records 
```python3
from fedsearch import Api

# Configuration
API_KEY = ' '

try:
    # Output Count Results
    records = Api.records(API_KEY)
    print(records)
except Exception as e:
    # Print any Errors
    print(e)
```

----------------------------------------------------------------------------------

FedSearch Version
```python3
from fedsearch import Api

# Configuration
API_KEY = ' '

try:
    # Output FedSearch Version
    version = Api.version(API_KEY)
    print(version)
except Exception as e:
    # Print any Errors
    print(e)
```

----------------------------------------------------------------------------------
