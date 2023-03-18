const submit = document.querySelector('#s')
submit.addEventListener('click', () => {
    const formData = new FormData();
    formData.append('username', document.querySelector('#u').value);
    formData.append('password', document.querySelector('#p').value);

    fetch('api/login', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
});


const ss = document.querySelector('#ss')

ss.addEventListener('click',()=>{

    fetch('api/users')
    .then(res => res.json())
    .then(data => console.log(data))


})