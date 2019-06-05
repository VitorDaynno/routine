import sys
import os
from src.routine import Routine

if __name__ == "__main__":
    board_id = os.environ["BOARD_ID"]
    api_key = os.environ["TRELLO_API_KEY"]
    token = os.environ["TRELLO_TOKEN"]
    tokens = {"api_key": api_key, "token": token}
    routine = Routine(board_id, tokens)
    if len(sys.argv) > 1:
        action = sys.argv[1]
        if action == "process":
            routine.process()
