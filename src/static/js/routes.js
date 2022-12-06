import Mustache from "./mustache.js";
import data from './result.json' assert {type: 'json'};
import main_data from './data.json' assert {type: 'json'};

function result_sort() {
    let j = []
    j.push(data);

    j.sort(function (a, b) {
        return a.value - b.value;
    })
// console.log(j)
    let result = []

    let articlesContainer = document.getElementById("router-view");
    for (let i = 0; i < j.length; i++) {
        let obj = j[i];
        for (let key in obj) {
            let value = obj[key];
            for (let x = 0; x < main_data.length; x++) {
                if (value['name'] === main_data[x]['summary']['name']) {
                    let name = main_data[x]['summary']['name'];
                    let desc = main_data[x]['summary']['description'];

                    const newArticle =
                        {
                            name: name,
                            description: desc
                        }

                    result.push(newArticle)

                    localStorage.myArticles = JSON.stringify(result);
                    articlesContainer.innerHTML += opinion2html(newArticle)
                }
            }
        }
    }
    window.scrollTo({top: 550, behavior: 'smooth'})
    console.log(result)
    return result;
}

function opinion2html(opinion) {
    return `
			<section class="articleSection">
			    <h2>${opinion.name}</h2>
                <p>${opinion.description}</p>
			</section>`;
}

export default [

    {
        //the part after '#' in the url (so-called fragment):
        hash: "welcome",
        ///id of the target html element:
        target: "router-view",
        //the function that returns content to be rendered to the target html element:
        getTemplate: (targetElm) =>
            document.getElementById(targetElm).innerHTML = document.getElementById("template-welcome").innerHTML,
    },

    {
        hash: "articles",
        target: "router-view",
        getTemplate: result_sort
    }
];

// function createHtml(targetElm) {
//     let opinionsFromStorage = result_sort();
//     console.log(opinionsFromStorage)
//     if (opinionsFromStorage) {
//         document.getElementById(targetElm).innerHTML = Mustache.render(
//             document.getElementById("template-articles").innerHTML,
//             opinionsFromStorage
//         );
//     }
// }