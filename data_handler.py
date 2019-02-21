import persistence
import connection
import security

"""USERS"""

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

"""END OF USERS"""

"""CARDS"""

@connection.connection_handler
def add_new_card(cursor, card_name, board_id, status_id):
    cursor.execute("""INSERT INTO cards (title, board_id, status_id)
                      VALUES (%(card_name)s, %(board_id)s, %(status_id)s)""", {'card_name': card_name, 'board_id': board_id, 'status_id': status_id})


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

@connection.connection_handler
def get_cards_by_board_id(cursor, board_id):
    cursor.execute("""SELECT * FROM cards
                    WHERE board_id= %(board_id)s;""",
    {'board_id': board_id})
    return cursor.fetchall()

"""END OF CARDS"""

"""DELETE"""

@connection.connection_handler
def delete_cards(cursor, _id):
    cursor.execute("""DELETE FROM cards
                              WHERE id = %(_id)s""", {'_id': _id})



#-----------------------------
#  BOARDS
#-----------------------------

@connection.connection_handler
def get_all_boards(cursor):
    cursor.execute("""
    SELECT * FROM boards;""")
    return cursor.fetchall()


@connection.connection_handler
def add_new_board(cursor, board_title):
    cursor.execute("""
                    INSERT into boards (title) VALUES (%(board_title)s);
                    """,
                   {'board_title': board_title})


@connection.connection_handler
def delete_board(cursor, board_id):
    cursor.execute("""
                    SELECT id FROM cards
                    WHERE board_id = %(id)s;
                    """,
                   {"id": board_id})
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


@connection.connection_handler
def delete(cursor, subject, _id):
    if subject == 'board':
        cursor.execute("""SELECT cards.id AS id
                          FROM boards
                          JOIN statuses ON board_columns.board_id = boards.id
                          JOIN cards ON cards.board_column_id = board_columns.id
                          WHERE boards.id = %(_id)s""", {'_id': _id})
        rows = cursor.fetchall()
        for row in rows:
            cursor.execute("""DELETE FROM cards
                              WHERE id = %(card_id)s""", {'card_id': int(row.get('id'))})
        cursor.execute("""DELETE FROM statuses
                          WHERE id = %(_id)s""", {'_id': _id})
        cursor.execute("""DELETE FROM boards
                          WHERE id = %(_id)s""", {'_id': _id})
    elif subject == 'column':
        cursor.execute("""DELETE FROM cards
                          WHERE status_id = %(_id)s""", {'_id': _id})
        cursor.execute("""DELETE FROM statuses
                          WHERE id = %(_id)s""", {'_id': _id})
    elif subject == 'card':
        cursor.execute("""DELETE FROM cards
                          WHERE id = %(_id)s""", {'_id': _id})


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
