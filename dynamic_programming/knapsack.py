# Copyright (C)  Authors and contributors All Rights Reserved.
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
# ==============================================================================
from collections import namedtuple
import numpy as np

Item = namedtuple("Item", "weight profit")


def knapsack01(items, knapsack_capacity):
    no_items = len(items)

    cols_len = knapsack_capacity + 1
    table = np.zeros((no_items + 1, cols_len), dtype=int)

    for row, item in enumerate(items):
        for col in range(1, cols_len):
            if item.weight > col:
                table[row + 1][col] = table[row][col]

            if (col - item.weight) >= 0:
                current_total_profit = item.profit + table[row][col - item.weight]
                table[row + 1][col] = max(current_total_profit, table[row][col])

    selected_items = []
    current_col = cols_len - 1
    current_row = no_items

    while current_row > 0 and current_col > 0:
        if table[current_row][current_col] == table[current_row - 1][current_col]:
            current_row = current_row - 1

        else:
            selected_items.append(items[current_row - 1])
            current_col = current_col - items[current_row - 1].weight
            current_row = current_row - 1

    return selected_items, table[no_items][cols_len - 1]

