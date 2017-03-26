# axel-wrapper
Python wrapper of axel, a light command line download accelerator

## Installation
`axel-wrapper` depends on `axel`, so you must install `axel` before `python-axel`

### Install axel

#### Ubuntu

```
sudo apt-get install axel
```

#### Arch Linux

```
sudo pacman -S axel
```

### Install axel-wrapper
```
pip install axel-wrapper
```

## Basic usage

```python
from axel import axel

# Download http://someurl/file.zip with 500 parallel connection
file_path = axel('http://someurl/file.zip', num_connections=500)  
```
