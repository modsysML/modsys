# Copyright: (c) 2022, Adrian Brown <adrbrownx@gmail.com>
# Copyright: (c) 2023, ModsysML Project
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from modsys.client import Modsys


def evaluate():
    sdk = Modsys()
    sdk.use("google_perspective:analyze", google_perspective_api_key="#API-KEY")
    return sdk.evaluate(
        [
            {
                "item": "This is hate speech",
                "__expected": {"TOXICITY": {"value": "0.78"}},
                "__trend": "lower",
            },
            {
                "item": "You suck at this game.",
                "__expected": {"TOXICITY": {"value": "0.50"}},
                "__trend": "higher",
            },
        ]
    )


if __name__ == "__main__":
    evaluate()
