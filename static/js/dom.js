// It uses data_handler.js to visualize elements
import {data_handler} from "./data_handler.js";


const createTable = function(title, id) {
    const template = document.querySelector('#board-template');
    const clone = document.importNode(template.content, true);
    clone.querySelector('#heading-1').textContent = title;
    clone.querySelector('.new-card').setAttribute('data-board-id', id);
    clone.querySelector('.btn-danger').setAttribute('data-id',  id);
    clone.querySelector('#heading-1').setAttribute('data-target', '#collapse-' +id)
    clone.querySelector('#heading-1').setAttribute('aria-controls', 'collapse-' + id);
    clone.querySelector('#heading-1').setAttribute('id', 'heading-' + id)
    clone.querySelector('#collapse-1').setAttribute('aria-labelledby', 'heading-' + id);
    clone.querySelector('#collapse-1').setAttribute('id', 'collapse-' + id);

    return clone

};

const createCard = function (title, board_id, status_id) {
    const cardTemplate = document.querySelector('#card-template');
    const clone = document.importNode(cardTemplate.content, true);
    clone.querySelector('#card-title').textContent = title;
    return clone
};

export let dom = {
    createBoard: function (board) {
        const createElement = createTable(board.title, board.id);
        document.querySelector('#container').appendChild(createElement);
    },
    showCard: function (cards) {
        const showElement = createCard(cards.title, cards.board_id, cards.status_id);
        let table = document.getElementById('collapse-' + cards.board_id);
        let status = table.querySelector('#status'+cards.status_id)
        status.appendChild(showElement)
    },
    createNewCard: function () {
        let newCardButtons = document.querySelectorAll('.new-card')
        for(let newButton of newCardButtons){
            newButton.addEventListener('click', function () {
                let board_id = this.dataset.boardId
                let modal_board_id = document.getElementById('new-cards')
                modal_board_id.setAttribute('value', board_id)

            })

        }

    },

}


