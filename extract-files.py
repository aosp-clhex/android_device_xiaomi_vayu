#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

namespace_imports = [
		'device/xiaomi/vayu',
		'hardware/qcom-caf/common/libqti-perfd-client',
		'hardware/qcom-caf/sm8150',
		'hardware/qcom-caf/wlan',
		'hardware/xiaomi',
		'vendor/qcom/opensource/commonsys-intf/display',
		'vendor/qcom/opensource/commonsys/display',
		'vendor/qcom/opensource/dataservices',
		'vendor/qcom/opensource/display',
]

blob_fixups: blob_fixups_user_type = {
    'vendor/lib64/camera/components/com.qti.node.watermark.so': blob_fixup()
        .add_needed('libpiex_shim.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'vayu',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()