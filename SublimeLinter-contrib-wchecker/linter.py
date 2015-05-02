#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Javier Fernandes
# Copyright (c) 2015 Uqbar Project
#
# License: MIT
#

"""This module exports the Wollok Wchecker plugin class."""

from SublimeLinter.lint import Linter, util


class Wchecker(Linter):

    """Provides an interface to Wollok wchecker."""
    
    syntax = ['wollok']
    extensions = ['wlk', 'wpgm', 'wtest']

    cmd = 'wchecker @'

    check_version = False  # deshabilitado por ahora deberia validar la version del linter
    # contra la version de wollok (que tampoco tenemos)
    version_args = '--version'
    version_re = r'\bv(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.0.0'
    
    regex = (
        r'^(?P<file>.+?):(?P<line>\d+):(?P<col>\d+) '
        r'(?:((?P<error>ERROR)|(?P<warning>WARNING))) '
        r'(?P<message>.+)'
    )
    multiline = False
    
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    
    comment_re = r'\s*/[/*]'


    def split_match(self, match):
        """
        Return the components of the match.
        We override this because included header files can cause linter errors,
        and we only want errors from the linted file.
        """
        if match:
           if match.group('file') != self.filename:
               match = None

        return super().split_match(match)
