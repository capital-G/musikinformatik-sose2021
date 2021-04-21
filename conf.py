# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#


# -- Project information -----------------------------------------------------

project = 'Musikinformatik'
copyright = '2021, Dennis Scheiba'
author = 'Dennis Scheiba'

# The full version, including alpha/beta/rc tags
release = 'SoSe 2021'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'myst_nb',
    'jupyter_sphinx',
    'sphinxcontrib.bibtex',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['docs/_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'docs/_build'
    'Thumbs.db',
    '.DS_Store',
    'venv',
    'README.md',
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['docs/_static']

# custom

html_title = "Musikinformatik SoSe2021"

todo_include_todos = True

html_theme_options = {
    "use_edit_page_button": True,
    "github_url": "https://github.com/capital-G/musikinformatik-sose2021",
}

html_context = {
    "github_user": "capital-G",
    "github_repo": "musikinformatik-sose2021",
    "github_version": "main",
    "doc_path": "",
}

bibtex_bibfiles = ['refs.bib']

jupyter_execute_notebooks = "off"
