Environment setup
=================

In order to run the notebooks you will need to install Python on your local machine.

Python
------

Please make sure you have installed Python 3.8 and pip on your machine as well as `virtualenv`.

* Create a new virtual environment in the folder `venv` by executing
  
  .. code-block:: shell

    virtualenv venv
  

  and activate the environment by executing
  
  .. code-block:: shell

    source venv/bin/activate

* Install all necessary dependencies by executing

  .. code-block:: shell
    
    pip install -r requirements.txt

* Register your created environment in the Jupyter Lab instance

  ..code-block:: shell

    ipython kernel install --user --name=musikinformatik_sose2021

* Start *Jupyter Lab* by executing
  
  .. code-block:: shell

    jupyter lab


Docker
^^^^^^

Alternatively, if one has `Docker <https://www.docker.com>`_ installed, one can also run the notebooks in a docker container by executing

.. code-block:: shell

    docker build -t musikinformatik . && docker run -p 8888:8888 -v ${PWD}:/home/musikinformatik musikinformatik


and click on the appearing link.

Supercollider
-------------
