# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import sys
import re
import unittest

from nikola.utils import LOGGER
import logbook

from .test_rst_compiler import ReSTExtensionTestCase


class TestPublication(ReSTExtensionTestCase):

    extra_plugins_dirs = ["v7/publication_list/"]

    @staticmethod
    def setUpClass():
        LOGGER.notice('--- TESTS FOR publication_list')
        LOGGER.level = logbook.WARNING

    @staticmethod
    def tearDownClass():
        sys.stdout.write('\n')
        LOGGER.level = logbook.NOTICE
        LOGGER.notice('--- END OF TESTS FOR publication_list')

    def test_default(self):
        # the result should be
        expected = (
            '<div class = "publication-list">'
            '<h3>2015</h3><ul>'
            '<li class = "publication">.*One article in 2015.*</li>'
            '<li class = "publication">.*One conference in 2015.*</li>'
            '</ul><h3>2010</h3><ul>'
            '<li class = "publication">.*One Book in 2010.*</li>'
            '</ul></div>'
        )
        self.sample = '.. publication_list:: tests/data/publication_list/test.bib'
        self.basic_test()
        assert re.search(expected.replace('\n', '').strip(), self.html.replace('\n', '').strip())

if __name__ == '__main__':
    unittest.main()
