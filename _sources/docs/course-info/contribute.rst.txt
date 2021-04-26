Contribute
==========

This document will guide you through the necessary setup
and conventions on order to contribute to this project.

Jupyter notebook conventions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The versioning of Jupyter Notebooks is not the greatest as for example
the execution count of each cell is stored in the notebook.
We will use an automatic tool called *pre-commit* to clean the notebook
of any unnecessary content (see :ref:`pre-commit-setup`).

Also storing binary blobs such as images can lead to a big repository
soon - so if we decide to include such blobs it is best to make
the generation of these as stateless as possible.
To achieve this one can use tools such as  
`setting the random seed <https://stackoverflow.com/questions/21494489/what-does-numpy-random-seed0-do>`__
to make any randomness deterministic.

.. _pre-commit-setup:

pre-commit
^^^^^^^^^^

`pre-commit <https://pre-commit.com/>`__ allows us to run certain checks before a commit is made,
so much like `git hooks <https://git-scm.com/book/pl/v2/Customizing-Git-Git-Hooks>`__
but configurable through a ``.pre-commit-config.yaml`` file.

This gives us the ability to e.g. clean the notebooks of the execution count of each cell
as this can lead to lot of noise in the VCS.

*pre-commit* is already installed as a dependency (see :ref:`Installing dependencies`),
but in order to activate it we need to install the necessary hooks to our git
repository by running

.. code-block:: shell

    pre-commit install

After this just use your normal git workflow - keep in mind that
*pre-commit* can prevent you from committing files because *pre-commit*
found an issue with them - most often *pre-commit* will automatically
try to fix the issue and you need to stage this changes to your commit
after which the commit should work without issues.

Building the documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to build the documentation locally one also needs to install the dependencies of the documentation
by executing the following command in the root directory of the repository (see :ref:`Repository setup`)
and activating the virtual environment (see :ref:`virtualenv-activate`).

.. code-block:: shell

  pip3 install -r requirements-docs.txt

After this the documentation can be build by executing the shell script

.. code-block:: shell

  ./build_docs.sh

from the root directory of the repository.

.. admonition:: Convention

  If you want to open the documentation in a browser after it has been build you can set the
  environment variable

  .. code-block:: shell

    export OPEN_BROWSER_AFTER_TEST=true
  
  when using the ``./build_docs.sh`` script.

  Remember that this has to be set every time you open a shell or you add it to your ``~/.zshrc`` or else.
