function addEntry() {
    let steps = document.getElementById('steps').value
    let date = document.getElementById('date').value
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'steps': steps,
                             'date': date})
    }).then(response => {
        if (response.redirected) {
            window.location.href = response.url;
        }
    })
}

function clearEntries() {
    fetch('/clear', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
    }).then(response => {
        if (response.redirected) {
            window.location.href = response.url;
        }
    })
}
