/*
 * This file is licensed under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.tresamigos.smv

class SmvForceRunTest extends SmvTestUtil {
  object X extends SmvModule("X") {
    def requiresDS() = Seq()
    def run(i: runParams) = dfFrom("k:String","")
  }

  test("Test forcing module to run skips the DataFrame cache") {
    val rdd1 = X.rdd()
    val rdd2 = X.rdd(true)
    assert(rdd1 !== rdd2)
  }
}
