# Copyright 2019 Canonical Ldt.
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

from ros2cli.verb import VerbExtension
from ros2hellocli.api import get_hello_world, get_hello_world_leet


class WorldVerb(VerbExtension):
    """Prints Hello World on the terminal."""

    def add_arguments(self, parser, cli_name):
        parser.add_argument(
                  '--simple', '-s', action='store_true',
                  help="Display the message in a simple form.")

    def main(self, *, args):
        message = get_hello_world_leet() if not args.simple else get_hello_world()
        print(message)
