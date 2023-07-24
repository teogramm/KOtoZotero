import os
import sys


def check_if_envvars_are_set():
    if not all(k in os.environ for k in ("ZOT_KEY", "ZOT_LIB_ID")):
        print("Please set the ZOT_KEY and ZOT_LIB_ID environment variables.", file=sys.stderr)
        exit(1)


check_if_envvars_are_set()
api_key = os.environ["ZOT_KEY"]
user_id = os.environ["ZOT_LIB_ID"]
