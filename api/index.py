import sys
import os

# Root directory path-a Python path-la add pannuroam
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Vercel entry point
app = app
