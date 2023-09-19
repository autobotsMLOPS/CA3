[![Docker Image CI](https://github.com/autobotsmlops/CA3/actions/workflows/docker_image.yml/badge.svg)](https://github.com/autobotsmlops/CA3/actions/workflows/docker_image.yml)
[![branch main](https://github.com/autobotsmlops/CA3/actions/workflows/main_branch.yml/badge.svg)](https://github.com/autobotsmlops/CA3/actions/workflows/main_branch.yml)

# MLOPS CA3

## setup

### for windows

- create a virtual environment

```bash
python -m venv venv
```

- set execution policy

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

- activate the virtual environment

```bash
venv\Scripts\activate
```

- install pip

```bash
python.exe -m pip install --upgrade pip
```

- run makefile

```bash
make install
```

### for linux and mac

- create a virtual environment

```bash
python3 -m venv venv
```

- activate the virtual environment

```bash
source venv/bin/activate
```

- run makefile

```bash
make install
```
