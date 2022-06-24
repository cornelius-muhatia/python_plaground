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
# ==============================================================================


def bowl(v):
    """
    recursive solution (top down)
    Refer to: <a href="https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/mit6_006s20_lec15/">MIT Algorithms 2020</a>
    """
    memo = {}

    def bowl_fn(i):
        if i >= len(v):
            return 0  # base cases

        if i not in memo:  # check memo
            if (i + 2) >= len(v):
                memo[i] = max(
                    bowl_fn(i + 1),  # relation: skip pin i
                    v[i] + bowl_fn(i + 1)  # OR bowl pin i separately
                )

            else:
                memo[i] = max(
                    bowl_fn(i + 1),  # relation: skip pin i
                    v[i] + bowl_fn(i + 1),  # OR bowl pin i separately
                    v[i] * v[i + 1] + bowl_fn(i + 2)  # OR bowl pins i and i+1 together
                )

        return memo[i]

    return bowl_fn(0)
