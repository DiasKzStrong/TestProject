import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import "./css/Login.css"

export const Register = () => {

    let [userArray, setUserArray] = useState([])

    useEffect(() => {
        const apiUrl = 'http://127.0.0.1:8000/api/users';
        axios.get(apiUrl).then((resp) => {
            const allPersons = resp.data;
            setUserArray(allPersons);
        });
    }, [setUserArray]);

    console.log(userArray);

    const [emailValue, setEmailValue] = useState("")
    const [passwordValue, setPasswordValue] = useState("")
    const [loginValue, setLoginValue] = useState("")

    const [emailDirty, setEmailDirty] = useState(false)
    const [passwordDirty, setPasswordDirty] = useState(false)
    const [loginDirty, setLoginDirty] = useState(false)
    const [emailError, setEmailError] = useState('Email не может быть пустым!')
    const [passwordError, setPasswordError] = useState("Пароль не может быть пустым!")
    const [loginError, setLoginError] = useState("Логин не может быть пустым!")
    const [formValid, setFormValid] = useState(false)

    const emailHandler = (e) => {
        setEmailValue(e.target.value)
        const re = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
        if (!re.test(String(e.target.value).toLowerCase())) {
            setEmailError('Некорректный email!')
        } else {
            setEmailError('')
        }
    }

    const passwordHandler = (e) => {
        setPasswordValue(e.target.value)
        if (e.target.value.length < 3 || e.target.value.length > 12) {
            setPasswordError('Пароль должен быть длинее 3 и  меньше 12!')
            if (!e.target.value) {
                setPasswordError('Пароль не может быть пустым!')
            }
        } else {
            setPasswordError('')
        }
    }

    const loginHandler = (e) => {
        setLoginValue(e.target.value)
        if (e.target.value.length < 2) {
            setLoginError('Логин должен быть длинее 2!')
            if (!e.target.value) {
                setLoginError('Логин не может быть пустым!')
            }
        } else {
            setLoginError('')
        }


        userArray.map(item => {
            if (e.target.value == item.username) {
                setLoginError("Такой пользователь уже существует!");
            } else {
                setLoginError("");
            }
            console.log(userArray);
        })
    }

    const registerClick = (e) => {
        const formData = new FormData();
        formData.append('email', emailValue);
        formData.append('username', loginValue);
        formData.append('password', passwordValue);

        fetch('http://127.0.0.1:8000/api/register', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => console.log(data.username[0]))
            .catch(error => console.error(error));

        alert("Вы успешно зарегистрировались!")
    }


    const blurHandler = (e) => {
        switch (e.target.name) {
            case "email":
                setEmailDirty(true);
                break;
            case 'password':
                setPasswordDirty(true);
                break;
            case 'username':
                setLoginDirty(true);
                break;
        }
    }

    useEffect(() => {
        if (emailError || passwordError || loginError) {
            setFormValid(false)
        } else {
            setFormValid(true)
        }
    }, [emailError, passwordError, loginError])


    return (
        <div className='login-container'>
            <div className='login-welcome-block'>
                <div className='welcome-wrapper'>
                    <h2 className='welcome-text'>ДОБРО ПОЖАЛОВАТЬ !</h2>
                </div>
            </div>
            <div className='login-form-block'>
                <div className='form'>
                    <Link className="navbar_link" to={"/login"}>
                        <p className='login-text'>Вход</p>
                    </Link>
                    <Link className="navbar_link" to={"/register"}>
                        <p className='login-active-text'>Регистрация</p>
                    </Link>
                </div>
                <div className='form-wrapper'>
                    <input className='input' value={emailValue} onChange={(e) => emailHandler(e)} onBlur={e => blurHandler(e)} placeholder='Email' name='email' id='e' type="text" />
                    {(emailDirty && emailError) && <div className="error_text">{emailError}</div>}
                    <input className='input' value={loginValue} onChange={(e) => loginHandler(e)} onBlur={e => blurHandler(e)} placeholder='Логин' name='username' id='u' type="text" />
                    {(loginDirty && loginError) && <div className="error_text">{loginError}</div>}
                    <input className='input' value={passwordValue} onChange={(e) => passwordHandler(e)} onBlur={e => blurHandler(e)} placeholder='Пароль' name='password' id='p' type="password" />
                    {(passwordDirty && passwordError) && <div className="error_text">{passwordError}</div>}
                    <Link className="navbar_link" to={"/login"}>
                        <button className='button3' disabled={!formValid} id="s" onClick={registerClick} type='submit'>ЗАРЕГИСТРИРОВАТЬСЯ</button>
                    </Link>
                </div>
            </div>
        </div>
    )
}