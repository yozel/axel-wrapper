# python-axel
Python wrapper of axel, a light command line download accelerator

## Installation

```
pip install axel
```

## Basic usage

```python
from axel import axel

# Download http://someurl/file.zip with 500 parallel connection
file_path = axel('http://someurl/file.zip', num_connections=500)  
```
