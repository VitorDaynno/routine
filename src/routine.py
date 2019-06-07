from .trelloHelper import TrelloHelper
from .fileHelper import FileHelper
from datetime import datetime


class Routine:

    def __init__(self, board_id, tokens):
        self.trello = TrelloHelper(tokens)
        self.board_id = board_id
        self.file = FileHelper()

    def process(self):
        self.file.open("historic.csv", "a")
        lists = self.trello.get_lists(self.board_id)
        for list in lists:
            self.process_day(list)
        self.file.close()

    def process_day(self, list):
        total = 0
        concluded = 0
        cards = self.trello.get_cards(list["id"])
        for card in cards:
            if card["dueComplete"]:
                concluded = concluded + 1
            total = total + 1
            self.trello.delete_cards(card["id"])
        total = 100 if total == 0 else total
        percentage = ((100 * concluded)/total)
        self.file.write(list["name"] + "," + str(percentage))

    def import_routine(self, file):
        self.file.open(file, "r")
        lines = self.file.get_lines()
        for line in lines:
            card = line.split(",")
            self.import_day(card)
        self.file.close()

    def import_day(self, card):
        lists = self.trello.get_lists(self.board_id)
        for list in lists:
            if card[0].lower() == list["name"].lower():
                self.trello.create_card(card[1], list["id"], None, None, None)
