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
def lis(str_):
    """
    Given a string A, find a longest (not necessarily contiguous) subsequence of A that strictly increases (
    lexicographically). see:
    https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/mit6_006s20_lec16/
    """
    a = len(str_)
    x = [1] * a

    for i in reversed(range(a)):
        for j in range(i, a):
            if str_[j] > str_[i]:
                x[i] = max(x[i], 1 + x[j])

    return max(x)
