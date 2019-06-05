from trello import TrelloApi


class TrelloHelper:

    def __init__(self, tokens):
        self.trello = TrelloApi(tokens["api_key"], "none")
        self.trello.set_token(tokens["token"])

    def get_board(self, id):
        board = self.trello.boards.get(id)
        return board

    def get_lists(self, board_id):
        lists = self.trello.boards.get_list(board_id)
        return lists

    def get_cards(self, list_id):
        cards = self.trello.lists.get_card(list_id)
        return cards

    def delete_cards(self, card_id):
        self.trello.cards.delete(card_id)
