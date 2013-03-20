# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2013 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <http://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.test import TestCase
from trans.machine.dummy import DummyTranslation
from trans.machine.glosbe import GlosbeTranslation
from trans.machine.mymemory import MyMemoryTranslation
from trans.machine.opentran import OpenTranTranslation
from trans.machine.apertium import ApertiumTranslation

class MachineTranslationTest(TestCase):
    '''
    Testing of machine translation core.
    '''
    def test_support(self):
        machine_translation = DummyTranslation()
        self.assertTrue(machine_translation.is_supported('cs'))
        self.assertFalse(machine_translation.is_supported('de'))

    def test_translate(self):
        machine_translation = DummyTranslation()
        self.assertEqual(
            machine_translation.translate('cs', 'Hello'),
            []
        )
        self.assertEqual(
            machine_translation.translate('cs', 'Hello, world!'),
            []
        )

    def test_glosbe(self):
        machine = GlosbeTranslation()
        self.assertGreater(len(machine.translate('cs', 'world')), 0)

    def test_mymemory(self):
        machine = MyMemoryTranslation()
        self.assertGreater(len(machine.translate('cs', 'world')), 0)

    def test_opentran(self):
        machine = OpenTranTranslation()
        self.assertGreater(len(machine.translate('cs', 'world')), 0)

    def test_apertium(self):
        machine = ApertiumTranslation()
        self.assertGreater(len(machine.translate('es', 'world')), 0)
