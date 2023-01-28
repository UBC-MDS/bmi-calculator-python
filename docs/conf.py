# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Required by Plotly graphs
# See https://sphinx-gallery.github.io/stable/auto_examples/plot_9_plotly.html
import plotly.io as pio
pio.renderers.default = 'sphinx_gallery'

# -- Project information -----------------------------------------------------

project = u"bmigraph"
copyright = u"2023, Qurat-ul-Ain Azim, Natalie Cho, HanChen Wang, Kelvin Wong"
author = u"Qurat-ul-Ain Azim, Natalie Cho, HanChen Wang, Kelvin Wong"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]
autoapi_dirs = ["../src"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# An ugly hack because `include`d MDs can't get its path rewritten to map
# as relative paths...
html_extra_path = [
    "../img"
]

# For the gallery to be rendered properly in browsers
html_js_files = [
    "require-2.3.6.min.js"
]
html_static_path = [
    "assets/require-2.3.6.min.js"
]
