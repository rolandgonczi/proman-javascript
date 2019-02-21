// It uses data_handler.js to visualize elements
import {data_handler} from "./data_handler.js";


const createTable = function(title) {
    const template = document.querySelector('#board-template');
    const clone = document.importNode(template.content, true);
    clone.querySelector('#headingOne').textContent = title;

    return clone

};

const createCard = function (title) {
    const cardTemplate = document.querySelector('#card-template');
    const clone = document.importNode(cardTemplate.content, true);

    clone.querySelector('#card-title').textContent = title;
    return clone
};

export function createBoard(board) {
    const createElement = createTable(board.title);
    document.querySelector('#container').appendChild(createElement);

}


