#!/usr/bin/env python3

"""
Reference:
Source: https://github.com/aianta/cgi-lab
Owner: Alex (TA)
Date Accessed: Sept 27th, 2022
"""

import os
import json

env = {}

# fetch the environment variables
for env_key, env_value in os.environ.items():
    env[env_key] = env_value

print("Content-Type: application/json") # HTML is following
print()                                 # blank line, end of headers

# print env dictionary in json format
print(json.dumps(env))