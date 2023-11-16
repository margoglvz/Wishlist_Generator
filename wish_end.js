let inputs = localStorage.getItem("answers")

console.log(inputs); 
let i = 0;
while (i < 11) {
    loaded(i); 
}

function loaded(index) {
    console.log("hi"); 
    console.log(inputs[index]); 
    /*document.getElementById("display").innerHTML += `
    <div id="display">
        <h1>yo</h1>
    </div>
    `;*/
    
    
    }
    

