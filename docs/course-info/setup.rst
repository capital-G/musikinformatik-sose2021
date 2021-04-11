Environment setup
=================

This document will lead you through the setup so one can run the code on a local machine.

Repository setup
----------------

To copy the course material to the local machine we will use `git <https://git-scm.com/>`_.
For the install procedure please refer to the `official website <https://git-scm.com/downloads>`_.

After one has setup git we now need to `clone <https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone>`_
the `repository <https://github.com/capital-G/musikinformatik-sose2021>`_ by opening a new shell window and head to a
directory in which you want to copy the course material and execute the command

.. code-block:: shell

  git clone https://github.com/capital-G/musikinformatik-sose2021.git

If you know what *SSH*, have a GitHub account and you want to practicipate in the creation of the course
one should use SSH instead so the command becomes

.. code-block:: shell

  git clone git@github.com:capital-G/musikinformatik-sose2021.git

Now as we have cloned the course material to a local directory we want to switch to the directory which we just
created by cloning the repository

.. code-block:: shell

  cd musikinformatik_sose2021


.. admonition:: Convention

   We will refer to this folder as *the root folder of the repository*.
   Most commands will be executed in this folder and we will always work relative
   to this path.
   
   Please make sure if you e.g. re-start *Jupyter Lab* or you activate the 
   virtual environment you are in this directory before entering the commands.

SuperCollider setup
-------------------

Please refer to the `SuperCollider download page <https://supercollider.github.io/download>`_
for the install instructions of SuperCollider.

Python setup
------------

Please make sure you have installed *Python >=3.7*, *pip3* and *virtualenv* on your machine.
A good guide on how to install *Python* on your machine can be found `here <https://realpython.com/installing-python/>`__.

After a sucessful installation please check that you have the following versions.

.. warning::

  Please refrain from *Python 3.9* as this is `not supported by Tensorflow yet <https://github.com/tensorflow/tensorflow/issues/44485>`_.
  If you use `Homebrew <https://brew.sh/>`_ on OS X you can install *Python 3.8* via

  .. code-block:: shell

    brew install python@3.8

.. code-block:: shell

  python3 --version
  # Python 3.8.2 - should be Python3 and 3.7 at least

  pip3 --version
  # pip 21.0.1 from /usr/local/lib/python3.8/site-packages/pip
  # just about any pip3 version will be fine

  virtualenv --version
  # virtualenv 20.4.2 from /usr/local/lib/python3.8/site-packages/virtualenv/__init__.py
  # just about any virtualenv version will be fine - make sure that it refers to your
  # python3 folder from above and not to e.g. python2

* Go to the root folder of the repository (see :ref:`Repository setup`) with a shell and execute
  the following commands in this folder.

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

* Go to the root directory of the repository (see :ref:`Repository setup`) with a shell window
  and execute the following commands in this folder.

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

In order to build the documentation locally one also needs to install its dependencies by executing the
following command in the root directory of the repository (see :ref:`Repository setup`)

.. code-block:: shell

  pip3 install -r requirements-docs.txt

After this the documentation can be build by executing the shell script

.. code-block:: shell

  ./build_docs.sh

from the root directory of this repository.

.. admonition:: Convention

  If you want to open the documentation in a browser after it has been build you can set the
  environment variable

  .. code-block:: shell

    export OPEN_BROWSER_AFTER_TEST=true
  
  when using the ``./build_docs.sh`` script.

  Remember that this has to be set every time you open a shell or you add it to your ``~/.zshrc`` or else.

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
