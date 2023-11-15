const initialQuestion = "Is this gift for you or somebody else?"; 

let questions = [
"How would you describe yourself in three words?",
"What are your hobbies or interests?",
"Do you have any favorite books, movies, or TV shows?",
"What kind of music do you enjoy listening to?",
"Have you traveled anywhere recently? Any favorite destinations?",
"Do you have pets? If so, what pet do you have?",
"What's your favorite type of food?",
"Are you a morning person or a night owl?",
"What's a skill you've always wanted to learn?",
"If you could have dinner with any historical figure, who would it be?",
"Do you have a favorite quote or mantra that inspires you?"]; 

const priceQuestion = "What is the price range of your project?"; 

let qnum = 0; 

function updateQuiz(num) {
    document.getElementById('quiz').innerHTML += `
    <div>
        <h1>${questions[num]}</h1>
        <button onclick="click()">CLICK ME</button>
    </div>
`;
}


function click() {
    console.log("hi"); 
    qnum = qnum + 1;
    updateQuiz(qnum); 
}



function loaded() {
    updateQuiz(qnum); 
}

if (qnum == questions.length) {
    window.location = 'wish.end.html';
}

