from flask import Flask, render_template, url_for, session, redirect, request
from util import json_response
import json

import data_handler
import security

app = Flask(__name__)

app.secret_key = b'r[_Drea+%!"edCElf>>,'


@app.route("/")
def index():
    """
    This is a one-pager which shows all the boards and cards
    """
    return render_template('index.html')

"""USER HANDLING"""

@app.route('/signup', methods=['POST'])
def route_sign_up():
    data_handler.sign_up(request.form['username'], request.form['password'])
    return redirect(url_for('index'))


@app.route('/signin', methods=['POST'])
def route_sign_in():
    user_details = data_handler.sign_in(request.form['username'], request.form['password'])
    if user_details is not None and security.verify_password(request.form['password'], user_details['password']):
        session['user_id'] = user_details['id']
        session['username'] = user_details['username']
    return redirect(url_for('index'))


@app.route('/logout', methods=['GET'])
def route_logout():
    session.clear()
    return redirect(url_for('index'))

"""END OF USER HANDLING"""


"""CARD HANDLING"""

@app.route('/card', methods=['POST'])
def add_new_card():
    card_name = request.json.get('cardName')
    board_column_id = request.json.get('boardColumnId')
    position = request.json.get('position')
    data_handler.add_new_card(card_name, board_column_id, position)
    return json.dumps({'attempt': 'successful'})


@app.route('/update-card-column-id', methods=['POST'])
def update_card_board_column_id():
    new_board_column_id = request.json.get('newBoardColumnId')
    card_id = request.json.get('cardId')
    data_handler.update_card_board_column_id(card_id, new_board_column_id)
    return json.dumps({'attempt': 'successful'})


@app.route('/update-card-positions', methods=['POST'])
def update_card_positions():
    data_handler.update_card_positions(request.json)
    return json.dumps({'attempt': 'successful'})

"""END OF CARD HANDLING"""


@app.route("/get-boards")
@json_response
def get_boards():
    """
    All the boards
    """
    title = data_handler.get_all_boards()
    return title


@app.route("/new-board", methods=['GET', 'POST'])
def add_board():
    if request.method == 'POST':
        board_title = request.form['title']
        data_handler.add_new_board(board_title)
        return redirect(url_for('index'))


@app.route("/delete-board/<int:board_id>")
@json_response
def delete_board(board_id: int):
    data_handler.delete_board(board_id)


@app.route('/delete', methods=['POST'])
def delete():
    data_handler.delete(request.json.get('subject'), request.json.get('id'))
    return json.dumps({'attempt': 'successful'})


@app.route("/get-cards/<int:board_id>")
@json_response
def get_cards_for_board(board_id: int):
    """
    All cards that belongs to a board
    :param board_id: id of the parent board
    """

    return data_handler.get_cards_by_board_id(board_id)


def main():
    app.run(debug=True)

    # Serving the favicon
    with app.app_context():
        app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()




