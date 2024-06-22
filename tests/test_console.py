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
        storage._FileStorage__file_path = 'file.json'
        try:
            os.remove('test_file.json')
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

    def test_create_with_kv_str_args(self):
        """Test that create new object with string kv pair works"""
        with patch('sys.stdout', new=StringIO()) as out:
            # Test create state
            HBNBCommand().onecmd('create State name="Kode"')
            obj_id = out.getvalue().rstrip('\n')
            self.assertIsNotNone(obj_id)
            state = storage._FileStorage__objects.get(f'State.{obj_id}')
            self.assertEqual(state.name, 'Kode')
            out.truncate(0)
            out.seek(0)
            # Test create User
            udata = 'email="d@m.co" password="passw" first_name="Djimra"\
                    last_name="NGARLEITA"'
            HBNBCommand().onecmd(f'create User {udata}')
            u_id = out.getvalue().rstrip('\n')
            self.assertIsNotNone(u_id)
            user = storage._FileStorage__objects.get(f'User.{u_id}')
            self.assertEqual(user.first_name, 'Djimra')
            self.assertEqual(user.last_name, 'NGARLEITA')
            self.assertEqual(user.password, 'passw')
            self.assertEqual(user.email, 'd@m.co')
            out.truncate(0)
            out.seek(0)
            # Test create City
            cdata = 'name="Mane" state_id="S10"'
            HBNBCommand().onecmd(f'create City {cdata}')
            c_id = out.getvalue().rstrip('\n')
            self.assertIsNotNone(c_id)
            city = storage._FileStorage__objects.get(f'City.{c_id}')
            self.assertEqual(city.name, 'Mane')
            self.assertEqual(city.state_id, 'S10')
            out.truncate(0)
            out.seek(0)
            # Test create Amenity
            HBNBCommand().onecmd('create Amenity name="Private_Airport"')
            obj_id = out.getvalue().rstrip('\n')
            self.assertIsNotNone(obj_id)
            amenity = storage._FileStorage__objects.get(f'Amenity.{obj_id}')
            self.assertEqual(amenity.name, 'Private Airport')
            out.truncate(0)
            out.seek(0)
            # Test create Review
            HBNBCommand().onecmd('create Review place_id="P10" user_id="U10"\
                    text="Cool_place"')
            obj_id = out.getvalue().rstrip('\n')
            self.assertIsNotNone(obj_id)
            review = storage._FileStorage__objects.get(f'Review.{obj_id}')
            self.assertEqual(review.place_id, 'P10')
            self.assertEqual(review.user_id, 'U10')
            self.assertEqual(review.text, 'Cool place')
            out.truncate(0)
            out.seek(0)
            # Test create Place
            place_d = 'city_id="C10" user_id="U10" name="DMTower" number_rooms=7\
                    description="My_house" number_bathrooms=8 max_guest=10\
                    price_by_night=1000 latitude=0.12 longitude=12.7'
            HBNBCommand().onecmd(f'create Place {place_d}')
            obj_id = out.getvalue().rstrip('\n')
            self.assertIsNotNone(obj_id)
            place = storage._FileStorage__objects.get(f'Place.{obj_id}')
            self.assertEqual(place.city_id, 'C10')
            self.assertEqual(place.user_id, 'U10')
            self.assertEqual(place.description, 'My house')
            out.truncate(0)
            out.seek(0)

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
