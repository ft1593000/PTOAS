# Copyright (c) 2026 Huawei Technologies Co., Ltd.
# This program is free software, you can redistribute it and/or modify it under the terms and conditions of
# CANN Open Software License Agreement Version 2.0 (the "License").
# Please refer to the License for details. You may not use this file except in compliance with the License.
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR PURPOSE.
# See LICENSE in the root of the software repository for the full text of the License.

"""Run supported reduction boundary goldens through the VPTO case runner.

Reuse the DSL ST kernels and reference calculations so both test entrypoints
check identical semantics: original identities, modulo sums, grouped stores,
broadcasts and untouched output canaries. Small vectors include singleton
groups; integer inputs are 16/32-bit and floating inputs are f16/f32.
"""

import sys
from pathlib import Path

DSL_ST_DIR = Path(__file__).resolve().parents[3] / "dsl-st"
sys.path.insert(0, str(DSL_ST_DIR))

from common import auto_main
from vmi_compact_group_reduce import CASES as COMPACT_CASES
from vmi_group_reduce_boundaries import CASES as BOUNDARY_CASES

CASES = BOUNDARY_CASES + COMPACT_CASES

auto_main(globals())
