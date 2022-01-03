# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'Simple Sabotage Field Manual'
copyright = '1944, Office of Strategic Services'
author = 'Office of Strategic Services'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

latex_engine = 'lualatex'
latex_use_xindy = False
latex_elements = {
    'preamble': r'''
\usepackage{luatexja-fontspec}
\setmainjfont{Noto Serif CJK TC}
\setsansjfont{Noto Sans CJK TC}
''',
}
