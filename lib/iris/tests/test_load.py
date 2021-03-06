# (C) British Crown Copyright 2010 - 2012, Met Office
#
# This file is part of Iris.
#
# Iris is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Iris is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Iris.  If not, see <http://www.gnu.org/licenses/>.
"""
Test the main loading API.

"""
# import iris tests first so that some things can be initialised before importing anything else
import iris.tests as tests

import iris


@iris.tests.skip_data
class TestLoad(tests.IrisTest):
    def test_normal(self):
        paths = (
            tests.get_data_path(['PP', 'aPPglob1', 'global.pp']),
        )
        cubes = iris.load(paths)
        self.assertEqual(len(cubes), 1)

    def test_bogus(self):
        paths = (
            tests.get_data_path(['PP', 'aPPglob1', 'global.pp']),
        )
        cubes = iris.load(paths, 'wibble')
        self.assertEqual(len(cubes), 0)

    def test_real_and_bogus(self):
        paths = (
            tests.get_data_path(['PP', 'aPPglob1', 'global.pp']),
        )
        cubes = iris.load(paths, ('air_temperature', 'wibble'))
        self.assertEqual(len(cubes), 1)

    def test_duplicate(self):
        paths = (
            tests.get_data_path(['PP', 'aPPglob1', 'global.pp']),
            tests.get_data_path(['PP', 'aPPglob1', 'gl?bal.pp'])
        )
        cubes = iris.load(paths)
        self.assertEqual(len(cubes), 2)


@iris.tests.skip_data
class TestLoadCube(tests.IrisTest):
    def test_normal(self):
        paths = (
            tests.get_data_path(['PP', 'aPPglob1', 'global.pp']),
        )
        cube = iris.load_cube(paths)

    def test_not_enough(self):
        paths = (
            tests.get_data_path(['PP', 'aPPglob1', 'global.pp']),
        )
        with self.assertRaises(iris.exceptions.ConstraintMismatchError):
            iris.load_cube(paths, 'wibble')

    def test_too_many(self):
        paths = (
            tests.get_data_path(['PP', 'aPPglob1', 'global.pp']),
            tests.get_data_path(['PP', 'aPPglob1', 'gl?bal.pp'])
        )
        with self.assertRaises(iris.exceptions.ConstraintMismatchError):
            iris.load_cube(paths)


@iris.tests.skip_data
class TestLoadCubes(tests.IrisTest):
    def test_normal(self):
        paths = (
            tests.get_data_path(['PP', 'aPPglob1', 'global.pp']),
        )
        cubes = iris.load_cubes(paths)
        self.assertEqual(len(cubes), 1)

    def test_not_enough(self):
        paths = (
            tests.get_data_path(['PP', 'aPPglob1', 'global.pp']),
        )
        with self.assertRaises(iris.exceptions.ConstraintMismatchError):
            iris.load_cubes(paths, 'wibble')

    def test_not_enough_multi(self):
        paths = (
            tests.get_data_path(['PP', 'aPPglob1', 'global.pp']),
        )
        with self.assertRaises(iris.exceptions.ConstraintMismatchError):
            iris.load_cubes(paths, ('air_temperature', 'wibble'))

    def test_too_many(self):
        paths = (
            tests.get_data_path(['PP', 'aPPglob1', 'global.pp']),
            tests.get_data_path(['PP', 'aPPglob1', 'gl?bal.pp'])
        )
        with self.assertRaises(iris.exceptions.ConstraintMismatchError):
            iris.load_cube(paths)


if __name__ == "__main__":
    tests.main()
