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

import ros2hellocli.api
from ros2hellocli.verb import VerbExtension


class WorldVerb(VerbExtension):
    """Prints Hello World on the terminal."""

    def main(self, *, args):
        hello_world = ros2hellocli.api.get_hello_world()
        print(hello_world)
