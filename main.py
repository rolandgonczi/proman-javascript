from flask import Flask, render_template, url_for, session, redirect, request
from util import json_response

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


@app.route("/get-boards")
@json_response
def get_boards():
    """
    All the boards
    """
    return data_handler.get_all_boards()


@app.route("/new-board", methods=['GET', 'POST'])
@json_response
def add_board():
    if request.method == 'POST':
        board_title = request.form['title']
        data_handler.add_new_board(board_title)
        return render_template(url_for('index'), board_title=board_title)


@app.route("/delete-board/<int:board_id>")
@json_response
def delete_board(board_id: int):
    data_handler.delete_board(board_id)


@app.route("/get-cards/<int:board_id>")
@json_response
def get_cards_for_board(board_id: int):
    """
    All cards that belongs to a board
    :param board_id: id of the parent board
    """
    return data_handler.get_cards_for_board(board_id)


def main():
    app.run(debug=True)

    # Serving the favicon
    with app.app_context():
        app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()
