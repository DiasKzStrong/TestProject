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
    const csrfToken = document.cookie.match(/csrftoken=([\w-]+)/)[1];
    fetch('api/reset-password/request/',{ 
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken

        },
        body: JSON.stringify(
        {
        'email':'dias.ziyada12345@gmail.com'
        }
    )
})
.then((res) => {
    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }
  })
  .then((data) => console.log(data))
  .catch((error) => console.error(error));
})