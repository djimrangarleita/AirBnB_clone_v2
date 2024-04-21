#!/usr/bin/python3
"""Tests for the console module"""
import unittest
import os
from models import storage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """Test suite for the commands"""

    def setUp(self):
        """Setup common behavior for each test"""
        storage._FileStorage__file_path = 'test_file.json'
        storage._FileStorage__objects = {}
        self.class_names = ['BaseModel', 'User', 'State', 'City',
                            'Place', 'Amenity', 'Review']

    def tearDown(self):
        """Remove changes applied by setup"""
        try:
            os.remove(storage._FileStorage__file_path)
        except Exception:
            pass

    def test_quit(self):
        """Test the quit cmd"""
        with patch('sys.stdout', new=StringIO()) as out:
            result = HBNBCommand().onecmd("quit")
            self.assertTrue(result)
            self.assertEqual(out.getvalue(), '')

    def test_eof(self):
        """Test the EOF cmd"""
        with patch('sys.stdout', new=StringIO()) as out:
            result = HBNBCommand().onecmd("EOF")
            self.assertTrue(result)
            self.assertEqual(out.getvalue(), '\n')

    def test_help(self):
        """Test the execute cmd"""
        h_header = "\nDocumented commands (type help <topic>):\n"
        h_separator = "========================================\n"
        h_list = "EOF  all  count  create  destroy  exit  help  \
quit  show  update\n\n"
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("help")
            self.assertNotEqual(out.getvalue(), '')
            self.assertIsInstance(out.getvalue(), str)
            self.assertEqual(out.getvalue(), h_header + h_separator + h_list)

    def test_empty_line(self):
        """Test the empty line cmd"""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd("      ")
            self.assertEqual(out.getvalue(), '')

    def test_create(self):
        """Test the create for all classes cmd"""
        for name in self.class_names:
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd(f"create {name}")
                self.assertIsNotNone(out.getvalue())
                self.assertIsInstance(out.getvalue(), str)

    def test_show(self):
        """Test show cmd"""
        for name in self.class_names:
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd(f"create {name}")
                self.assertNotEqual(out.getvalue(), '')
                instance_id = out.getvalue().rstrip('\n')
                out.truncate(0)
                out.seek(0)
                HBNBCommand().onecmd(f"show {name} {instance_id}")
                output = out.getvalue()
                self.assertIn(f"[{name}]", output)
                self.assertIn(f"{instance_id}", output)
                self.assertIn("id", output)
                self.assertIn("created_at", output)
                self.assertIn("updated_at", output)
                out.truncate(0)
                out.seek(0)
                HBNBCommand().onecmd(f"{name}.show({instance_id})")
                output = out.getvalue()
                self.assertIn(f"[{name}]", output)
                self.assertIn(f"{instance_id}", output)
                self.assertIn("id", output)
                self.assertIn("created_at", output)
                self.assertIn("updated_at", output)

    def test_destroy(self):
        """Test destroy cmd"""
        for name in self.class_names:
            with patch('sys.stdout', new=StringIO()) as out:
                # Create instance
                HBNBCommand().onecmd(f"create {name}")
                self.assertIsNotNone(out.getvalue())
                instance_id = out.getvalue().rstrip('\n')
                # Clear output (console)
                out.truncate(0)
                out.seek(0)
                # Execute destroy and assert output
                HBNBCommand().onecmd(f"destroy {name} {instance_id}")
                self.assertEqual('', out.getvalue())
                HBNBCommand().onecmd(f"show {name} {instance_id}")
                self.assertEqual(out.getvalue(), '** no instance found **\n')
                # Clear output (console)
                out.truncate(0)
                out.seek(0)
                # Create another instance
                HBNBCommand().onecmd(f"create {name}")
                self.assertNotEqual('', out.getvalue())
                instance_id = out.getvalue().rstrip('\n')
                # Clear output (console)
                out.truncate(0)
                out.seek(0)
                # Execute Classname.destroy(instance_id)
                HBNBCommand().onecmd(f"{name}.destroy({instance_id})")
                self.assertEqual('', out.getvalue())
                HBNBCommand().onecmd(f"show {name} {instance_id}")
                self.assertEqual(out.getvalue(), '** no instance found **\n')

    def test_all(self):
        """Test the all cmd"""
        for name in self.class_names:
            with patch('sys.stdout', new=StringIO()) as out:
                # Create instance
                HBNBCommand().onecmd(f"create {name}")
                self.assertNotEqual(out.getvalue(), '')
                instance_id = out.getvalue().rstrip('\n')
                out.truncate(0)
                out.seek(0)
                # Check for classes
                HBNBCommand().onecmd(f"all {name}")
                self.assertIn(f"[\"[{name}] ({instance_id})", out.getvalue())
                out.truncate(0)
                out.seek(0)
                HBNBCommand().onecmd(f"{name}.all()")
                self.assertIn(f"[\"[{name}] ({instance_id})", out.getvalue())
        output = ''
        with patch('sys.stdout', new=StringIO()) as out:
            # Get output to assert all() without name
            HBNBCommand().onecmd("all")
            output = out.getvalue()
        for name in self.class_names:
            self.assertIn(name, output)

    def test_update(self):
        """Test the update cmd"""
        for name in self.class_names:
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd(f"create {name}")
                self.assertNotEqual(out.getvalue(), '')
                instance_id = out.getvalue().rstrip('\n')
                out.truncate(0)
                out.seek(0)
                # Execute and assert update with basic syntax
                HBNBCommand().onecmd(f"update {name} {instance_id} name Acme")
                self.assertEqual('', out.getvalue())
                HBNBCommand().onecmd(f"show {name} {instance_id}")
                output = out.getvalue()
                self.assertIn(instance_id, output)
                self.assertIn("'name': 'Acme'", output)
            with patch('sys.stdout', new=StringIO()) as out:
                # Execute and assert Classname.update with 1 arg
                HBNBCommand().onecmd(f"{name}.update({instance_id},\
                        name, Test)")
                self.assertEqual('', out.getvalue())
                HBNBCommand().onecmd(f"show {name} {instance_id}")
                output = out.getvalue()
                self.assertIn(instance_id, output)
                self.assertIn("'name': 'Test'", output)
            with patch('sys.stdout', new=StringIO()) as out:
                # Execute and assert Classname.update with dict
                param = "{'name': 'New'}"
                HBNBCommand().onecmd(f"{name}.update({instance_id}, {param})")
                self.assertEqual('', out.getvalue())
                HBNBCommand().onecmd(f"show {name} {instance_id}")
                output = out.getvalue()
                self.assertIn(instance_id, output)
                self.assertIn("'name': 'New'", output)

    def test_count(self):
        """Test the count cmd"""
        for name in self.class_names:
            with patch('sys.stdout', new=StringIO()) as out:
                # Create 2 instances
                HBNBCommand().onecmd(f"create {name}")
                self.assertNotEqual(out.getvalue(), '')
                # Clear output (console)
                out.truncate(0)
                out.seek(0)
                HBNBCommand().onecmd(f"create {name}")
                self.assertNotEqual(out.getvalue(), '')
                # Clear output (console)
                out.truncate(0)
                out.seek(0)
                HBNBCommand().onecmd(f"{name}.count()")
                self.assertNotEqual(out.getvalue(), '0\n')
                self.assertEqual(out.getvalue(), '2\n')
                # Clear output (console)
                out.truncate(0)
                out.seek(0)
