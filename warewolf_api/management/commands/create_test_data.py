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
# Copyright 2019 SerialLab Corp.  All rights reserved.


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
# Copyright 2018 SerialLab Corp.  All rights reserved.
import os

from django.core.management.base import BaseCommand
from django.utils.translation import gettext as _

from quartet_output.parsing import BusinessEPCISParser


class Command(BaseCommand):
    help = _(
        'Creates test data that works along with the robot tests.'
    )

    def handle(self, *args, **options):
        print('***************************************************')
        try:
            self._parse_test_data()
        except Exception as e:
            print('there was a problem parsing the test data...this is '
                  'usually due to the fact that it may have already been '
                  'added.')
            print(e)

    def _parse_test_data(self, test_file='../../tests/data/epcis.xml',
                         recursive_decommission=False):
        curpath = os.path.dirname(__file__)
        parser = BusinessEPCISParser(
            os.path.join(curpath, test_file),
            recursive_decommission=recursive_decommission
        )
        message_id = parser.parse()
        print(parser.event_cache)
        return message_id, parser
