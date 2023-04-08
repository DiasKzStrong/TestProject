import axios from 'axios'
import React, { useContext, useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import "./css/Login.css"
import { AuthContext } from './context'

export const Login = ({ loginUser, setLoginUser }) => {

    const { isAuth, setIsAuth } = useContext(AuthContext);


    // let [loginUser, setLoginUser] = useState([])

    const [login, setLogin] = useState("")
    const [password, setPassword] = useState("")
    const [loginDirty, setLoginDirty] = useState(false)
    const [passwordDirty, setPasswordDirty] = useState(false)
    const [loginError, setLoginError] = useState('Логин не может быть пустым!')
    const [passwordError, setPasswordError] = useState("Пароль не может быть пустым!")
    const [formValid, setFormValid] = useState(false)

    const loginHandler = (e) => {
        setLogin(e.target.value)
        if (e.target.value.length < 3 || e.target.value.length > 12) {
            setLoginError('Логин должен быть длинее 3 и  меньше 12!')
            if (!e.target.value) {
                setLoginError('Логин не может быть пустым!')
            }
        } else {
            setLoginError('')
        }
    }

    const passwordHandler = (e) => {
        setPassword(e.target.value);
        if (e.target.value.length < 3 || e.target.value.length > 12) {
            setPasswordError('Пароль должен быть длинее 3 и  меньше 12!')
            if (!e.target.value) {
                setPasswordError('Пароль не может быть пустым!')
            }
        } else {
            setPasswordError('')
        }
    }


    const blurHandler = (e) => {
        switch (e.target.name) {
            case "username":
                setLoginDirty(true);
                break;
            case 'password':
                setPasswordDirty(true);
                break;
        }
    }


    useEffect(() => {
        if (loginError || passwordError) {
            setFormValid(false)
        } else {
            setFormValid(true)
        }
    }, [loginError, passwordError])

    const enterClick = (event) => {
        const formData = new FormData();
        formData.append('username', login);
        formData.append('password', password);


        fetch('http://127.0.0.1:8000/api/login', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                // loginUser.splice(0, 1)
                setLoginUser(data)
                localStorage.setItem("loginUser", JSON.stringify(data));
                setIsAuth(true)
                localStorage.setItem('auth', 'true')

                console.log(isAuth);
            })
            .catch(error => console.error(error));
    }

    return (
        <div className='login-container'>
            <div className='login-welcome-block'>
                <div className='welcome-wrapper'>
                    <h2 className='welcome-text'>С ВОЗВРАЩЕНИЕМ !</h2>
                    <p>Для авторизации воспользуйтесь формой входа, а если у вас еще нет аккаунта воспользуйтесь ссылкой "Регистрация" над формой.</p>
                </div>
            </div>
            <div className='login-form-block'>
                <div className='form'>
                    <Link className="navbar_link" to={"/login"}>
                        <p className='login-active-text'>Вход</p>
                    </Link>
                    <Link className="navbar_link" to={"/register"}>
                        <p className='login-text'>Регистрация</p>
                    </Link>
                </div>
                <div className='form-wrapper'>
                    {(loginDirty && loginError) && <div className="error_text">{loginError}</div>}
                    <input className='input' onChange={e => loginHandler(e)} value={login} onBlur={e => blurHandler(e)} placeholder='Логин' name='username' id='u' type="text" />
                    {(passwordDirty && passwordError) && <div className="error_text">{passwordError}</div>}
                    <input className='input' onChange={e => passwordHandler(e)} value={password} onBlur={e => blurHandler(e)} placeholder='Пароль' name='password' id='p' type="password" />
                    <div style={{width: "100%", textAlign: "end", margin: "-25px"}}>
                        <Link className='navbar_link' to={"/recovery"}>
                            <p style={{ fontSize: 13, color: "gray"}}>Забыли пароль?</p>
                        </Link>
                    </div>
                    <Link className="navbar_link" to={"/personal"}>
                        <button className='button3' disabled={!formValid} onClick={enterClick} id="ss" type='submit'>Войти</button>
                    </Link>
                </div>
            </div>
        </div>
    )
}