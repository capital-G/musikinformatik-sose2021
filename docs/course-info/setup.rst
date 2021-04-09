Environment setup
=================

In order to run and edit the course material on a local machine one needs to install

* Python 3.8 with pip3 - a good instruction can be found `here <https://realpython.com/installing-python>`_
* `SuperCollider <https://supercollider.github.io/download>`_


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

* Install all necessary dependencies by executing

  .. code-block:: shell
    
    pip install -r requirements.txt

* Register your created environment in the *Jupyter Lab* instance

  .. code-block:: shell

    ipython kernel install --user --name=musikinformatik_sose2021

* Start *Jupyter Lab* by executing
  
  .. code-block:: shell

    jupyter lab


Supercollider
-------------

Docker
------

Alternatively, if one has `Docker <https://www.docker.com>`_ installed, one can also run the notebooks in a docker container by executing

.. code-block:: shell

    docker build -t musikinformatik . && docker run -p 8888:8888 -v ${PWD}:/home/musikinformatik musikinformatik


and click on the appearing link.

.. todo::

  Currently it is difficult to run SuperCollider in an headless environment such as Docker.
  Any help on this is appreciated.
