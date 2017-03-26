# python-axel
Python wrapper of axel, a light command line download accelerator

## Installation
`python-axel` depends on `axel`, so you must install `axel` before `python-axel`

### Install axel

#### Ubuntu

```
sudo apt-get install axel
```

#### Arch Linux

```
sudo pacman -S axel
```

### Install python-axel
```
pip install axel
```

## Basic usage

```python
from axel import axel

# Download http://someurl/file.zip with 500 parallel connection
file_path = axel('http://someurl/file.zip', num_connections=500)  
```
