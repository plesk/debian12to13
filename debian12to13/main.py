#!/usr/bin/python3
# Copyright 1999-2026. WebPros International GmbH. All rights reserved.

import sys

import pleskdistup.main
import pleskdistup.registry

import debian12to13.upgrader

if __name__ == "__main__":
    pleskdistup.registry.register_upgrader(debian12to13.upgrader.Debian12to13Factory())
    sys.exit(pleskdistup.main.main())
