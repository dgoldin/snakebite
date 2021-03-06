# -*- coding: utf-8 -*-
# Copyright (c) 2013 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
from minicluster_testbase import MiniClusterTestBase
from snakebite.errors import InvalidInputException
from snakebite.errors import FileNotFoundException
import os


class StatTest(MiniClusterTestBase):

    def test_valid_path(self):
        client_output = self.client.stat(['/'])
        self.assertEqual(client_output['path'], '/')
        self.assertEqual(client_output['permission'], 0755)
        self.assertEqual(client_output['owner'], os.environ['USER'])
        self.assertEqual(client_output['group'], 'supergroup')

    def test_missing_path(self):
        self.assertRaises(InvalidInputException, self.client.stat, [])

    def test_invalid_path(self):
        self.assertRaises(FileNotFoundException, self.client.stat,
                          ['/does/not/exist'])
