// javascript_file.js
let persoane = []
let functii = []

document.addEventListener('DOMContentLoaded', function () {
    // Access the data passed from Django
    const dataFromDjango = jsonData;
    console.log(dataFromDjango);
    // Now you can use the data to run your functions
    for (const key in dataFromDjango) {
        if (dataFromDjango.hasOwnProperty(key)) {
            const value = dataFromDjango[key];
            persoane.push(key);
            functii.push(value);
            console.log(value);
        }
    }
     
    // let personNames = ["Matu Dragos Gabriel", "Filip Miriam-Valentina"]
    // let functions = ["billionaire", "trilionaire"]
    
});

function appearFunctions(value){
    document.querySelector("#function"+value).innerHTML = functii[value]
}

function appearPersonNames(value){
    document.querySelector("#function"+value).innerHTML = persoane[value]
}