function search() {
    let query = document.getElementById('user-input').value;

    let show = document.getElementById('show').value;

    let color = document.getElementById('color').value;

    // fetch("http://127.0.0.1:5000/get/" + query).then(res => res.json()).then(response => {
    //     document.getElementById('display').innerHTML = JSON.stringify(response);
    // })\

    
    fetch("http://127.0.0.1:5000/get/" + show + ' ' + color).then(res => res.json()).then(response => {
        document.getElementById('display').innerHTML = JSON.stringify(response);
    })

    fetch("http://127.0.0.1:5000/get/" + show + ' ' + color).then(res => res.json()).then(response => {
        document.getElementById('display').innerHTML = JSON.stringify(response);
    })

    fetch("http://127.0.0.1:5000/get/" + show + ' ' + color).then(res => res.json()).then(response => {
        document.getElementById('display').innerHTML = JSON.stringify(response);
    })
}