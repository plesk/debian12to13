# Copyright 2023-2024. WebPros International GmbH. All rights reserved.
# vim:ft=python:

include_defs('//product.defs.py')


python_binary(
    name = 'debian12to13.pex',
    platform = 'py3',
    # libgcc_s.so.1 is preloaded to workaround crash due to "libgcc_s.so.1 must
    # be installed for pthread_cancel to work" instead of clean exit after
    # dist-upgrade, see https://bugs.python.org/issue44434
    build_args = ['--python-shebang', '/usr/bin/env -S LD_PRELOAD=libgcc_s.so.1 python3'],
    main_module = 'debian12to13.main',
    deps = [
        'dist-upgrader//pleskdistup:lib',
        '//debian12to13:lib',
    ],
)

genrule(
    name = 'debian12to13',
    srcs = [':debian12to13.pex'],
    out = 'debian12to13',
    cmd = 'cp $(location :debian12to13.pex) $OUT && chmod +x $OUT',
)
