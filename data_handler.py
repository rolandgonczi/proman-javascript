import persistence
import connection
import security


#-----------------------------
#  USER
#-----------------------------

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


#-----------------------------
#  BOARDS
#-----------------------------

@connection.connection_handler
def get_all_boards(cursor):
    cursor.execute("""
    SELECT title FROM boards;""")
    return cursor.fetchall()


@connection.connection_handler
def add_new_board(cursor, board_title):
    cursor.execute("""
                    INSERT into boards (title) VALUES %(board_title)s;
                    """,
                   {'board_title': board_title})
    return cursor.fetchone()


@connection.connection_handler
def delete_board(cursor, board_id):
    cursor.execute("""
                    SELECT id FROM cards
                    WHERE board_id = %(id)s;
                    """,
                   {'id': board_id})
    card_ids = cursor.fetchall()
    for card_id in card_ids:
        cursor.execute("""
                        DELETE FROM cards WHERE id = %(card_id)s;
                        """,
                       {'card_id': card_id}) #  here we can call DELETE cards function written by Roland
    cursor.execute("""
                    DELETE FROM boards WHERE id = %(board_id)s;
                    """,
                   {'board_id': board_id})


#-----------------------------
#  ORIGINAL SKELETON CODE
#-----------------------------


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
