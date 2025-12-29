# Copyright 2025 Iguazio
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
#

class VerifySchema:
    def __init__(self, name, context, schema: dict):
        self.name = name
        self.context = context
        self.schema = schema

    def do(self, event: dict):
        for key, value_type in self.schema.items():
            if key not in event:
                raise KeyError(f"Schema verification failed: key '{key}' not found in event: {event}")
            if not isinstance(event[key], value_type):
                raise TypeError(f"Schema verification failed: key '{key}' is not of type "
                                f"'{value_type.__name__}' in event: {event}")
        return event