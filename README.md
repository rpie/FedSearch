----------------------------------------------------------------------------------

# Info

*A simple API for simple people*


FedSearch is a Database search API for free but this is for the **PAID** API Version

This project is being worked on live so have fun looking at it 



- HellSec

----------------------------------------------------------------------------------

# Examples

----------------------------------------------------------------------------------

Simple Search
```python3
import fedsearch

# Configuration
API_KEY = ' '
QUERY = ' '

# Setup the API
api = fedsearch.api()

try:
    # Search & Output Results
    search = api.search(API_KEY, QUERY)
    print(search)
except Exception as e:
    # Print any Errors
    print(e)
```


----------------------------------------------------------------------------------

Database Count Records 
```python3
import fedsearch

# Configuration
API_KEY = ' '

# Setup the API
api = fedsearch.api()

try:
    # Output Count Results
    records = api.records(API_KEY)
    print(records)
except Exception as e:
    # Print any Errors
    print(e)
```

----------------------------------------------------------------------------------

FedSearch Version
```python3
import fedsearch

# Configuration
API_KEY = ' '

# Setup the API
api = fedsearch.api()

try:
    # Output Count Results
    version = api.version(API_KEY)
    print(version)
except Exception as e:
    # Print any Errors
    print(e)
```

----------------------------------------------------------------------------------
