# -*- coding: utf-8 -*-

# Copyright © 2012-2017 Roberto Alsina and others.

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""Render the taxonomy overviews, classification pages and feeds."""

from __future__ import unicode_literals
import blinker
import functools
import natsort
import os
import sys

from collections import defaultdict

from nikola.plugin_categories import SignalHandler
from nikola import utils


class SectionNav(SignalHandler):
    """Classify posts and pages by taxonomies."""

    name = "section_prevnext"

    def _set_navlinks(self, site):
        # Needed to avoid strange errors during tests
        if site is not self.site:
            return
        # Update prev_post and next_post
#        for lang, langposts in site.posts_per_classification['section_index'].iteritems():
#            for section, sectionposts in langposts.iteritems():
#                for i, p in enumerate(sectionposts[1:]):
#                    print(p.title)
#                    p.next_post = sectionposts[i]
#                for i, p in enumerate(sectionposts[:-1]):
#                    p.prev_post = sectionposts[i + 1]
#                sectionposts[0].next_post = None
#                sectionposts[-1].next_post = None

    def set_site(self, site):
        """Set site, which is a Nikola instance."""
        super(SectionNav, self).set_site(site)
        # Add hook for after post scanning
        blinker.signal("scanned").connect(self._set_navlinks)
