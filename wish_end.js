let inputs = localStorage.getItem("answers")

function loaded() {

    let parsedAnswers = JSON.parse(inputs);

    for (let j = 0; j < parsedAnswers.length; j++) {
        fetch("http://127.0.0.1:5000/get/" + parsedAnswers[j]).then(res => res.json()).then(response => {
            // document.getElementById('display').innerHTML = JSON.stringify(response);

            console.log(response);

            for (let i = 0; i < response.itemSummaries.length; i++) {
                let item = response.itemSummaries[i];

                document.getElementById("display").innerHTML += `
            <div>
                <a href="${item.itemWebUrl}" target="_blank"><h1>${response.itemSummaries[i].title}</h1></a>
                <img src="${response.itemSummaries[i].image.imageUrl}" />
            </div>
            `;
            }


        });
    }




}


