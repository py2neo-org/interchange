#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright Nigel Small
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from unittest import TestCase

from interchange.time import Clock, Duration


class ClockTimeTestCase(TestCase):

    def test_zero_(self):
        clock = Clock()
        self.assertEqual(clock.seconds, 0)
        self.assertEqual(clock.nanoseconds, 0)

    def test_only_seconds(self):
        clock = Clock(123456)
        self.assertEqual(clock.seconds, 123456)
        self.assertEqual(clock.nanoseconds, 0)

    def test_float(self):
        clock = Clock(123456.789)
        self.assertEqual(clock.seconds, 123456)
        self.assertEqual(clock.nanoseconds, 789000000)

    def test_only_nanoseconds(self):
        clock = Clock(0, 123456789)
        self.assertEqual(clock.seconds, 0)
        self.assertEqual(clock.nanoseconds, 123456789)

    def test_nanoseconds_overflow(self):
        clock = Clock(0, 2123456789)
        self.assertEqual(clock.seconds, 2)
        self.assertEqual(clock.nanoseconds, 123456789)

    def test_positive_nanoseconds(self):
        clock = Clock(1, 1)
        self.assertEqual(clock.seconds, 1)
        self.assertEqual(clock.nanoseconds, 1)

    def test_negative_nanoseconds(self):
        clock = Clock(1, -1)
        self.assertEqual(clock.seconds, 0)
        self.assertEqual(clock.nanoseconds, 999999999)

    def test_add_float(self):
        clock = Clock(123456.789) + 0.1
        self.assertEqual(clock.seconds, 123456)
        self.assertEqual(clock.nanoseconds, 889000000)

    def test_add_duration(self):
        clock = Clock(123456.789) + Duration(seconds=1)
        self.assertEqual(clock.seconds, 123457)
        self.assertEqual(clock.nanoseconds, 789000000)

    def test_add_duration_with_months(self):
        with self.assertRaises(ValueError):
            _ = Clock(123456.789) + Duration(months=1)

    def test_add_object(self):
        with self.assertRaises(TypeError):
            _ = Clock(123456.789) + object()

    def test_sub_float(self):
        clock = Clock(123456.789) - 0.1
        self.assertEqual(clock.seconds, 123456)
        self.assertEqual(clock.nanoseconds, 689000000)

    def test_sub_duration(self):
        clock = Clock(123456.789) - Duration(seconds=1)
        self.assertEqual(clock.seconds, 123455)
        self.assertEqual(clock.nanoseconds, 789000000)

    def test_sub_duration_with_months(self):
        with self.assertRaises(ValueError):
            _ = Clock(123456.789) - Duration(months=1)

    def test_sub_object(self):
        with self.assertRaises(TypeError):
            _ = Clock(123456.789) - object()

    def test_repr(self):
        clock = Clock(123456.789)
        self.assertTrue(repr(clock).startswith("Clock"))
