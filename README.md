[![Build Status](https://travis-ci.org/ro-boy/ravestate.svg?branch=master)](https://travis-ci.org/ro-boy/ravestate)
[![codecov](https://codecov.io/gh/ro-boy/ravestate/branch/master/graph/badge.svg)](https://codecov.io/gh/ro-boy/ravestate)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/93ebb2077393423496669b5657ab16ac)](https://www.codacy.com/app/ro-boy/ravestate)
[![Code size](https://img.shields.io/github/languages/code-size/Roboy/ravestate.svg)](https://github.com/ro-boy/ravestate)
[![Repo size](https://img.shields.io/github/repo-size/Roboy/ravestate.svg)](https://github.com/ro-boy/ravestate)
[![Python version](https://img.shields.io/pypi/pyversions/ravestate.svg)](https://github.com/ro-boy/ravestate)
[![Release](https://img.shields.io/github/release/Roboy/ravestate.svg)](https://github.com/ro-boy/ravestate)
[![PyPi Downloads](https://img.shields.io/pypi/dm/ravestate.svg)](https://github.com/ro-boy/ravestate)

```
                                 _ __    _ __     
    _ ___ ____  __  ______  ______/ /_____/ /___     
 _ _ /  \/ __ \/ / / / __ \/ ___\, / __ \, /__  \  
_ _ / /\/ /_/ /\ \/ / /_/ /\__, / / /_/ / / /_/ /     
  _ \/ _\__/\/ _\__/ ,___/\____/\/\__/\/\/ ,___/
 _____          _ _\____/             _ _\____/                    
/_   _\
 0>  0> 
\__⊽__/  (C) Roboy 2019
   ⋂                                           
```

## About

Ravestate is a reactive library for real-time natural language dialog systems.

## Installation

### Via PIP

The easiest way to install ravestate is through pip:

``
pip install ravestate
``

### For developers

First, install dependencies:

```bash
pip install -r requirements.txt

# To run tests, install pytest, mocking, fixtures...
pip install -r requirements-dev.txt
```

Then, you may open the repository in any IDE, and mark the
`modules` folder as a sources root. 

## Running Hello World

Ravestate applications are defined by a configuration,
which specifies the ravestate modules that should be loaded.

To run the basic hello world application, run ravestate
with a config file or command line arguments:

### Running with command line spec

You can easily run a combination of ravestate modules in a shared context,
by listing them as arguments to the `rasta` command, which is installed
with ravestate:

```bash
rasta ravestate_conio ravestate_hello_world
```

Run `rasta -h` to see more options!

### Running with config file(s) 

You may specify a series of config files to configure ravestate context,
when specifying everything through the command line becomes too laborious:

```yaml
# In file hello_world.yml
module: core
config:
  import:
    - ravestate_conio
    - ravestate_hello_world
```
Then, run `rasta` with this config file:

```bash
rasta -f hello_world.yml
```

## Running tests

If you have installed the dependencies from ``requirements-dev.txt`` you
may run the ravestate test suite as follows:

``
./run_tests.sh
``

## Building/maintaining the docs

If you have installed the dependencies from ``requirements-dev.txt``,
generate the docs by running this command at project root:

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/modules
git rm -rf docs
rm -rf _build docs
pydocmd build
git add docs/*
```

The structure and content of the docs are defined in the file ``pydocmd.yml``.
