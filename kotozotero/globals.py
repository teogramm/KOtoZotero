import os

def check_if_envvars_are_set():
    try:
        os.environ["ZOT_KEY"]
        os.environ["ZOT_LIB_ID"]
    except KeyError:
        print("Please set the ZOT_KEY and ZOT_LIB_ID environment variables.")
        exit(1)


api_key = os.environ["ZOT_KEY"]
user_id = os.environ["ZOT_LIB_ID"]
