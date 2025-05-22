# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'VideoTuna'
copyright = 'VideoTuna Team'
author = 'Donghao Zhao'

release = '0.1'
version = '0.2.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "myst_parser",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_title = "VideoTuna"
html_theme = "furo"
html_static_path = ["_static"]

# -- Options for EPUB output
epub_show_urls = 'footnote'
