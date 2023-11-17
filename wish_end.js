let inputs = localStorage.getItem("answers")

function loaded() {
    document.getElementById("display").innerHTML = `
    <div id="display">
        <h1>${inputs}</h1>
    </div>
    `;
    
    
    }
    

