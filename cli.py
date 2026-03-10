#!/usr/bin/env python3
"""SHEIN CLI入口"""
import sys
from shein import main
import asyncio

if __name__ == "__main__":
    asyncio.run(main())
