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
def lcs(str1, str2):
    """
    Given two strings A and B, find a longest (not necessarily contiguous) subsequence of A that is also a
    subsequence of B. For more details see: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020
    /resources/mit6_006s20_lec16/
    """
    a, b = len(str1), len(str2)
    x = [[0] * (b + 1) for _ in range(a + 1)]

    for i in reversed(range(a)):
        for j in reversed(range(b)):
            if str1[i] == str2[j]:
                x[i][j] = x[i + 1][j + 1] + 1
            else:
                x[i][j] = max(x[i + 1][j], x[i][j + 1])

    return x[0][0]
