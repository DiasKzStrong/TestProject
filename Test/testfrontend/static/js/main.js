const ss = document.querySelector('#ss')
const s = document.querySelector('#s')
ss.addEventListener('click',()=>{
    const csrfToken = document.cookie.match(/csrftoken=([\w-]+)/)[1];
    fetch('api/reset-email/request/',{ 
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


s.addEventListener('click',()=>{
    const csrfToken = document.cookie.match(/csrftoken=([\w-]+)/)[1];
    fetch('http://127.0.0.1:8000/api/checking',{ 
        method: 'POST',
        headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(
        {
          "test_id": 3,
          "answers": [

            {
              'answer_id':1,
              'question_id':1
            },
            {
              'answer_id':3,
              'question_id':2
            }
          ]
        }
    )
})
.then(res => res.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
})



