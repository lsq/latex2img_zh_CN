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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = u'LaTex (tikz) 转换为图像'
copyright = u'2019, 高斯羽 博士 (Dr. Gāo, SīYǔ)'
author = u'高斯羽 博士 (Dr. Gāo, SīYǔ)'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.images',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

locale_dirs = ['locale']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

source_suffix = '.rst'
# The master toctree document.
master_doc = 'index'
# html_show_sourcelink = False
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for LaTeX output ------------------------------------------------
latex_engine = 'xelatex'
latex_use_xindy = False
# latex_docclass = {
#    'manual': 'ctexbook',
# }

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''

    \usepackage[UTF8]{ctex}

    \usepackage{float}

    % \usepackage{xeCJK}
    % \setCJKmainfont{Source Han Serif TC}
    % \setCJKsansfont{Source Han Sans Bold Bold}

    \usepackage{graphicx}

    \usepackage{indentfirst}
    \setlength{\parindent}{2em}

    ''',

    # \setCJKmainfont{Microsoft YaHei}


    # 'fontpkg': '\\usepackage{lmodern}',

    # LaTex figure (float) alignment
    #
    'figure_align': 'H',
}

latex_documents = [
    (master_doc,
     'latex2img.tex',
     u'LaTex (tikz)转换为图像',
     u'高斯羽\ 博士 (Dr. Gāo, Sī Yǔ)', 'manual'),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'late2img', u'LaTex (tikz) to Images Documentation',
     [author], 1)
]