const url: string = 'http://localhost:5000/' ;
fetch(url, {
    method: 'PUT',
    body: "",
    headers: {
        "Content-Type": "application/json"
    },
}).then((value) => {
    console.log(value)
})