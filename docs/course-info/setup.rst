Environment setup
=================

In order to run and edit the course material on a local machine one needs to install

* Python 3.8 with pip3 - a good instruction can be found `here <https://realpython.com/installing-python>`_
* `SuperCollider <https://supercollider.github.io/download>`_

SuperCollider setup
-------------------

Make sure you have SuperCollider setup before one continues with the setup of python because
we will rely on SuperCollider for that step.

Python setup
------------

Please make sure you have installed *Python 3.8*, *pip3* and *virtualenv* on your machine

.. code-block:: shell

  python3 --version
  # Python 3.8.2

  pip3 --version
  # pip 21.0.1 from /usr/local/lib/python3.8/site-packages/pip

  virtualenv --version
  # virtualenv 20.4.2 from /usr/local/lib/python3.8/site-packages/virtualenv/__init__.py


* Create a new virtual environment in the folder `venv` by executing
  
  .. code-block:: shell

    virtualenv venv
  

  and activate the environment by executing
  
  .. code-block:: shell

    source venv/bin/activate
  
  A virtual environment serves as a isolated environment for all the dependencies that are needed for this project.
  Creating a new virtual environment for each project is a good practice as project *a* relies on dependency *x* in
  version 0.7, but project *b* relies on the same dependency but in version 2.2.
  Welcome to `dependency hell <https://en.wikipedia.org/wiki/Dependency_hell>`_.

  But this also forces us to always activate the virtual environment when we start our project.

* Install all necessary dependencies by executing

  .. code-block:: shell
    
    pip3 install -r requirements.txt

* Register your created environment in the *Jupyter Lab* instance

  .. code-block:: shell

    ipython kernel install --user --name=musikinformatik_sose2021

Start *Jupyter Lab*
^^^^^^^^^^^^^^^^^^^

* Make sure one has activated the virtual environment by executing

  .. code-block:: shell

    source venv/bin/activate

  while being in the root directory of this repository.

* Start *Jupyter Lab* by executing
  
  .. code-block:: shell

    jupyter lab

* To shut down the *Jupyter Lab* server enter the keyboard combination of `<Ctrl> + c` 
  in the shell window in which the Jupyter server is running.
  A prompt will appear in which one has to verify that one wants to shut down the
  server by entering `y`.

Documentation
^^^^^^^^^^^^^

In order to build the documentation locally one also needs to install its dependencies via

.. code-block:: shell

  pip3 install -r requirements-docs.txt

After this the documentation can be build by executing the shell script

.. code-block:: shell

  ./build_docs.sh

from the root directory of this repository.

Setup via Docker
----------------

Alternatively, if one has `Docker <https://www.docker.com>`_ installed, one can also run the notebooks in a docker container by executing

.. code-block:: shell

    docker build -t musikinformatik . && docker run -p 8888:8888 -v ${PWD}:/home/musikinformatik musikinformatik


while being in the root directory of the repository and click on the appearing link.

.. todo::

  Currently it is difficult to run SuperCollider in an headless environment such as Docker,
  therefore SuperCollider is omitted in the docker image.

  Any help on this is appreciated.
