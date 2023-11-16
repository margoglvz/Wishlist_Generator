const initialQuestion = "Is this gift for you or somebody else?"; 
let pronoun = ""; 
let pronoun2 = ""; 
let pronoun3 = ""; 

function myself() {
    pronoun = "you";
    pronoun2 = "your";
    pronoun3 = "your";

    questions = [
        `How would ${pronoun} describe ${pronoun2}self in three words?`,
        `What are ${pronoun3} hobbies or interests?`,
        `Do ${pronoun} have any favorite books, movies, or TV shows?`,
        `What kind of music do ${pronoun} enjoy listening to?`,
        `Have ${pronoun} traveled anywhere recently? Any favorite destinations?`,
        `Do ${pronoun} have pets? If so, what pet do ${pronoun} have?`,
        `What's ${pronoun3} favorite type of food?`,
        `Are ${pronoun} a morning person or a night owl?`,
        `What's a skill ${pronoun}'ve always wanted to learn?`,
        `If ${pronoun} could have dinner with any historical figure, who would it be?`,
        `Do ${pronoun} have a favorite quote or mantra that inspires ${pronoun}?`];
    
    set(); 
}

function someoneElse() {
    pronoun = "they";
    pronoun2 = "them";
    pronoun3 = "their"; 
    
    questions = [
        `How would ${pronoun} describe ${pronoun2}self in three words?`,
        `What are ${pronoun3} hobbies or interests?`,
        `Do ${pronoun} have any favorite books, movies, or TV shows?`,
        `What kind of music do ${pronoun} enjoy listening to?`,
        `Have ${pronoun} traveled anywhere recently? Any favorite destinations?`,
        `Do ${pronoun} have pets? If so, what pet do ${pronoun} have?`,
        `What's ${pronoun3} favorite type of food?`,
        `Are ${pronoun} a morning person or a night owl?`,
        `What's a skill ${pronoun}'ve always wanted to learn?`,
        `If ${pronoun} could have dinner with any historical figure, who would it be?`,
        `Do ${pronoun} have a favorite quote or mantra that inspires ${pronoun}?`];
    
    set(); 
}

let answers = [

]

let questions = [];

const priceQuestion = "What is the price range of your project?"; 

let qnum = 0; 

function askFirst() {
    document.getElementById('quiz').innerHTML += `
    <div>
        <h1>${initialQuestion}</h1>
        <button onclick="myself()">Myself</button>
        <button onclick="someoneElse()">Someone else</button>
    </div>
`;

}

function updateQuiz(num) {
    document.getElementById('quiz').innerHTML = ""; 

    document.getElementById('quiz').innerHTML += `
    <div>
        <h1>${questions[num]}</h1>
    </div>
`
    if (num == 7) {
        document.getElementById('quiz').innerHTML += `
    <div>
        <button onclick="set()">Morning Person</button>
        <button onclick="set()">Night Owl</button>
    </div>
`;
    } else {
        document.getElementById('quiz').innerHTML += `
    <div>
        <input id="ans${num}" type="text"></input>
        <button onclick="set()">Submit</button>
    </div>
`;

    }
}


function set() {
    if (qnum == 0 | qnum == 7) {
        answers.push("");
    } else {
        answers.push(document.getElementById(`ans${qnum}`).value); 
    }
    qnum = qnum + 1;
    if (qnum < questions.length) {
        updateQuiz(qnum); 
    } else {
        loadEnd(); 
    }
    
}

function loaded() {
    askFirst(); 
}

function loadEnd() {
    localStorage.setItem("answers", answers); 
    window.location = 'wish_end.html';
}

