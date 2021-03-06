#
# This file is licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import smv
from stage1.modules import RM

RML = smv.SmvModuleLink(RM)

class M(smv.smvdataset.SmvModule):
    def requiresDS(self):
        return [RML]

    def run(self, i):
        # [100, "100", 100.0]
        res = i[RML]
        df = self.smvApp.createDF("res: String", "\"{}\"".format(res))
        return df
