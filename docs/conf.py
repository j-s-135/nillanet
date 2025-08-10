import os, sys
from datetime import datetime
sys.path.insert(0, os.path.abspath('..'))  # so Sphinx can import nn.model

project = 'nillanet'
author = 'James Smith'
copyright = f'{datetime.now():%Y}, {author}'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',          # Google/NumPy docstrings
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx_autodoc_typehints',     # nice type-hint rendering
]

# If CuPy isn't available on docs builder, prevent import errors:
autodoc_mock_imports = ['cupy']     # you can add 'numpy' here too if needed

# Autosummary: create stub pages for documented members
autosummary_generate = True

# Autodoc defaults
autodoc_default_options = {
    'members': True,
    'undoc-members': False,
    'show-inheritance': False,
    'inherited-members': False,
}

# Napoleon (Google-style) tweaks
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_use_param = True
napoleon_use_rtype = True

# Intersphinx: link out to external docs
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'cupy': ('https://docs.cupy.dev/en/stable/', None),
}

templates_path = ['_templates']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'     # or 'alabaster' (default)
html_static_path = ['_static']

