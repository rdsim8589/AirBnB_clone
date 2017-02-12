#!/usr/bin/python3
"""
This is the TestConsole Module. This module defines a TestConsole class that
inherits from unittest.TestCase for testing HBNBCommand class, an interactive
shell based on cmd.Cmd
"""
import sys
import unittest
from unittest import mock
from unittest.mock import create_autospec
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    Create automated tests for interactive shell based on cmd module
    """
    def setUp(self):
        """setup method for Console Test Class"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        """Test HBNBCommand class"""
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_help(self):
        """test help command"""

    def test_exit(self):
        """exit command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))

    def test_EOF(self):
        """exit command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("EOF"))

    def test_create_object(self):
        """test do_create"""
        cli = self.create()
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd('create'))
        self.assertEqual('** class name is missing **',
                         fakeOutput.getvalue().strip())

    def test_show_object(self):
        """test do_show"""
        cli = self.create()
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd('show BaseModel'))
        self.assertEqual('** no instance found **',
                         fakeOutput.getvalue().strip())

    def test_destroy_object(self):
        """test do_destroy"""
        cli = self.create()
        input_str = 'destroy BaseModel 12345678-1234-4744-9559-555555555555'
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd(input_str))
        self.assertEqual('** no instance found **', '** no instance found **')

    def test_update(self):
        """test do_update"""
        cli = self.create()
        in_put = 'update BaseModel 12345678-1234-4744-9559-555555555555 name'
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd(in_put))
        self.assertEqual('** value missing **', '** value missing **')

    def test_all(self):
        """test do_all"""
        cli = self.create()
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd('classname.all()'))
        self.assertEqual("** class doesn't exist **",
                         "** class doesn't exist **")
