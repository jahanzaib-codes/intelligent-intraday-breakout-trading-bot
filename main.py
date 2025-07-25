#!/usr/bin/env python3
"""
Intelligent Intraday Breakout Trading Bot
Main entry point
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.main_bot import main

if __name__ == "__main__":
    main() 