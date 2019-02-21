// It uses data_handler.js to visualize elements
import {data_handler} from "./data_handler.js";


const createTable = function(title, id) {
    const template = document.querySelector('#board-template');
    const clone = document.importNode(template.content, true);
    clone.querySelector('#headingOne').textContent = title;
    clone.querySelector('#headingOne').setAttribute('aria-controls', id)
    clone.querySelector('#headingOne').setAttribute('id', id);
    clone.querySelector('#collapseOne').setAttribute('aria-labelledby', id);
    clone.querySelector('#collapseOne').setAttribute('id', id)
    return clone

};

const createCard = function (title, board_id, status_id) {
    const cardTemplate = document.querySelector('#card-template');
    const clone = document.importNode(cardTemplate.content, true);
    clone.querySelector('#card-title').textContent = title;

    return clone
};

export let dom = { createBoard : function (board) {
    const createElement = createTable(board.title, board.id);
    document.querySelector('#container').appendChild(createElement);

    },
    showCards: function (cards) {
    const showCard = createCard(cards.title, cards.board_id, cards.status_id)
    document.getElementById('')

    }
}


