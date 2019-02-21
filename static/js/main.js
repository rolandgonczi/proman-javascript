// import { dom } from "./dom.js";
//
// // This function is to initialize the application
// function init() {
//     // init data
//     dom.init();
//     // loads the boards to the screen
//     dom.loadBoards();
//
// }
//
// init();

function init() {
    deleteButton()
}


function deleteButton()
{
    const deleteButtons = document.querySelectorAll(".btn-danger");
    for(let deleteButton of deleteButtons) {
        console.log(deleteButton);
        deleteButton.addEventListener('click', function(event) {
            const board = event.target;
            const url = '/delete';
            console.log(url);
            const subject = {subject: event.target.dataset.target, id: event.target.dataset.id};
            console.log(subject);
            fetch(url,
                {
                    method: 'POST',
                    headers:
                        {
                            "Content-Type": "application/json; charset=utf-8",
                        },
                    body: JSON.stringify(subject)
                })
                .then((response) => response.json())
                .then((response) => {
                    if (response.attempt === 'successful') {
                        reloadPageBoard()
                    }
                });
            });
        };
}

init();