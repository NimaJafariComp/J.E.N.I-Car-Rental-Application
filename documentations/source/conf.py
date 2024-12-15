import os
import sys
sys.path.insert(0, os.path.abspath(r"C:\Users\nimam\J.E.N.I-Car-Rental-Application"))
sys.path.insert(0, os.path.abspath('../../'))



# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'J.E.N.I Car Rental App'
copyright = '2024, Nima Jafari'
author = 'Nima Jafari'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # For Google/NumPy-style docstrings
    'sphinx.ext.viewcode',  # Links to source code
]


templates_path = ['_templates']
exclude_patterns = ['back_end\backend_test.py']

suppress_warnings = ['autodoc.importer', 'autodoc']




# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
