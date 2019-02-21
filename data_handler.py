import persistence
import connection
import security

"""USERS"""

@connection.connection_handler
def sign_up(cursor, username, password):
    cursor.execute("""
        INSERT INTO users (username, password)
        VALUES (%(username)s, %(password)s)
    """, {"username": username, "password": security.hash_password(password)})


@connection.connection_handler
def sign_in(cursor, username, password):
    cursor.execute("""
        SELECT id, username, password from users
        WHERE username = %(username)s
    """, {"username": username, "password": password})
    return cursor.fetchone()

"""END OF USERS"""

"""CARDS"""

@connection.connection_handler
def add_new_card(cursor, card_name, status_id, position):
    cursor.execute("""INSERT INTO cards (title, status_id, position)
                      VALUES (%(card_name)s, %(status_id)s, %(position)s)""", {'card_name': card_name, 'status_id': status_id, 'position': position})


@connection.connection_handler
def update_card_board_column_id(cursor, card_id, status_id):
    cursor.execute("""UPDATE cards
                      SET status_id = %(status_id)s
                      WHERE id = %(card_id)s""", {'new_board_column_id': status_id, 'card_id': card_id})


@connection.connection_handler
def update_card_positions(cursor, ids_and_positions):
    for position in ids_and_positions:
        cursor.execute("""UPDATE cards
                          SET position = %(position)s
                          WHERE id = %(card_id)s""",
                          {'position': int(position), 'card_id': int(ids_and_positions.get(position))})

"""END OF CARDS"""

"""DELETE"""

@connection.connection_handler
def delete_cards(cursor, _id):
    cursor.execute("""DELETE FROM cards
                              WHERE id = %(_id)s""", {'_id': _id})



def get_card_status(status_id):
    """
    Find the first status matching the given id
    :param status_id:
    :return: str
    """
    statuses = persistence.get_statuses()
    return next((status['title'] for status in statuses if status['id'] == str(status_id)), 'Unknown')


def get_boards():
    """
    Gather all boards
    :return:
    """
    return persistence.get_boards(force=True)


def get_cards_for_board(board_id):
    persistence.clear_cache()
    all_cards = persistence.get_cards()
    matching_cards = []
    for card in all_cards:
        if card['board_id'] == str(board_id):
            card['status_id'] = get_card_status(card['status_id'])  # Set textual status for the card
            matching_cards.append(card)
    return matching_cards
