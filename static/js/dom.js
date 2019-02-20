// It uses data_handler.js to visualize elements
import { dataHandler } from "./data_handler.js";

export let dom = {
    _appendToElement: function (elementToExtend, textToAppend, prepend = false) {
        // function to append new DOM elements (represented by a string) to an existing DOM element
        let fakeDiv = document.createElement('div');
        fakeDiv.innerHTML = textToAppend.trim();

        for (let childNode of fakeDiv.childNodes) {
            if (prepend) {
                elementToExtend.prependChild(childNode);
            } else {
                elementToExtend.appendChild(childNode);
            }
        }

        return elementToExtend.lastChild;
    },
    init: function () {
        // This function should run once, when the page is loaded.
    },
    loadBoards: function () {
        // retrieves boards and makes showBoards called
        dataHandler.getBoards(function(boards){
            dom.showBoards(boards);
        });
    },
    showBoards: function (boards) {
        // shows boards appending them to #boards div
        // it adds necessary event listeners also

        let boardList = '';

        for(let board of boards){
            boardList += `
                <li>${board.title}</li>
            `;
        }

        const outerHtml = `
            <ul class="board-container">
                ${boardList}
            </ul>
        `;

        this._appendToElement(document.querySelector('#boards'), outerHtml);
    },
    loadCards: function (boardId) {
        // retrieves cards and makes showCards called
    },
    showCards: function (cards) {
        // shows the cards of a board
        // it adds necessary event listeners also
    },
    // here comes more features
};

const createTable = function(title) {
    const template = document.querySelector('#board-template');
    const clone = document.importNode(template.content, true)
    const datSet = document.querySelector('#headingOne');


    clone.querySelector('#headingOne').textContent = title;

    return clone

};

const createCard = function (title) {
    const cardTemplate = document.querySelector('#card-template')
    const clone = document.importNode(cardTemplate.content, true)

    clone.querySelector('#card-title').textContent = title;
    return clone
}
function getTitle () {
    let title = prompt("Please enter your board name", "Harry Potter");
    if (title != null) {
        return title;
        }
    return null
}
function getCard(){
    let toDo = getTitle()
    const firstCard = createCard(toDo)
    document.querySelector('.new-card').appendChild(firstCard);
}

function createBoard() {
    let title = getTitle();
    const createElement = createTable(title);
    document.querySelector('#container').appendChild(createElement);

}

document.getElementById('new-board').addEventListener('click', createBoard);
document.getElementById('new-card').addEventListener('click', getCard);

// const firstCard = createCard('How you doing')
// document.querySelector('.new-card').appendChild(firstCard);