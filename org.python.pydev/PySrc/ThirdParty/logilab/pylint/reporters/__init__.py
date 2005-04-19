# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
"""utilities methods and classes for reporters

 Copyright (c) 2000-2003 LOGILAB S.A. (Paris, FRANCE).
 http://www.logilab.fr/ -- mailto:contact@logilab.fr
"""

__revision__ = "$Id: __init__.py,v 1.6 2005-04-19 14:39:13 fabioz Exp $"

import sys

CMPS = ['=', '-', '+']

def diff_string(old, new):
    """given a old and new int value, return a string representing the
    difference
    """
    diff = abs(old - new)
    diff_str = "%s%s" % (CMPS[cmp(old, new)], diff and ('%.2f' % diff) or '')
    return diff_str


class EmptyReport(Exception):
    """raised when a report is empty and so should not be displayed"""

class BaseReporter:
    """base class for reporters"""

    extension = ''
    
    def __init__(self, output=sys.stdout):
        self.linter = None
        self.include_ids = None
        self.section = 0
        self.out = None
        self.set_output(output)
        
    def set_output(self, output):
        """set output stream"""
        self.out = output
        
    def writeln(self, string=''):
        """write a line in the output buffer"""
        print >> self.out, string
        
    def display_results(self, layout):
        """display results encapsulated in the layout tree"""
        self.section = 0
        if self.include_ids and hasattr(layout, 'report_id'):
            layout.children[0].children[0].data += ' (%s)' % layout.report_id
        self._display(layout)
        
    def _display(self, layout):
        """display the layout"""
        raise NotImplementedError()
        
