import subprocess
import unittest
from unittest.mock import MagicMock, patch

import axel


class TestArgs(unittest.TestCase):
    def setUp(self):
        self.args = {
            'url': 'test', 'output_path': None, 'num_connections': None,
            'headers': None, 'extra_args': None, 'use_tsocks': None
        }

    def _test_arg(self, name, value, expected_result):
        self.args[name] = value
        args = axel._get_arg_list(**self.args)
        self.assertEqual(subprocess.list2cmdline(args), expected_result)

    def test_url(self):
        self._test_arg('url', 'http://test_url',
                       'axel http://test_url')

    def test_output_path(self):
        self._test_arg('output_path', 'test/path',
                       'axel --output=test/path test')

    def test_num_connections(self):
        self._test_arg('num_connections', 1000,
                       'axel --num-connections=1000 test')

    def test_num_headers(self):
        self._test_arg('headers', {'A': 'b', 'C': 'd'},
                       'axel "--header=A: b" "--header=C: d" test')

    def test_num_extra_args(self):
        self._test_arg('extra_args', {'test_arg1': 'test_val1',
                                      'test_arg2': 'test_val2'},
                       'axel --test_arg1=test_val1 --test_arg2=test_val2 test')

    def test_use_tsocks(self):
        self._test_arg('use_tsocks', True,
                       'tsocks axel test')


class TestAxelWrapper(unittest.TestCase):
    @patch('axel.subprocess')
    def test_happy_path(self, mocked_subprocess):
        mocked_subprocess.check_output = MagicMock(
            return_value='Opening output file /path/to/file.zip')
        result = axel.axel('http://example.local/file.zip')
        self.assertEqual(result, '/path/to/file.zip')

    @patch('axel.subprocess')
    def test_no_path_returned(self, mocked_subprocess):
        mocked_subprocess.check_output = MagicMock(return_value='Nonsense')
        with self.assertRaises(axel.AxelError) as cm:
            axel.axel('http://example.local/file.zip')
        self.assertEqual(cm.exception.args[0],
                         "Something is wrong, path doesn't exists")

    @patch('axel.subprocess')
    def test_process_error(self, mocked_subprocess):
        def raise_CalledProcessError(*args, **kwargs):
            raise subprocess.CalledProcessError(1, '', stderr='Test 123')

        mocked_subprocess.CalledProcessError = subprocess.CalledProcessError
        mocked_subprocess.check_output = MagicMock(
            side_effect=raise_CalledProcessError)
        with self.assertRaises(axel.AxelError) as cm:
            axel.axel('http://example.local/file.zip')
        self.assertEqual(cm.exception.args[0], "Test 123")
