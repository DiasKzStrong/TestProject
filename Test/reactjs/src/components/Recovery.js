import React from 'react'
import './css/Login.css'
import { Link } from 'react-router-dom'

export const Recovery = () => {
    return (
        <div className='login-container'>
            <div className='login-welcome-block'>
                <div className='welcome-wrapper'>
                    <h2 className='welcome-text'>ПОТЕРЯЛИСЬ ?</h2>
                    <p>Заполните форму справа, получите письмо на ваш почтовый адрес и сделуйте инструкции описанной в нем.</p>
                </div>
            </div>
            <div className='login-form-block'>
                <div className='form'>
                    <Link className="navbar_link" to={"/recovery"}>
                        <p className='login-active-text'>Восстановление</p>
                    </Link>
                    <Link className="navbar_link" to={"/login"}>
                        <p className='login-text'>Вход</p>
                    </Link>
                </div>
                <div className='form-wrapper'>
                    <div style={{ width: "55%", color: "white", marginBottom: "-25px" }}>
                        <p>Ваш логин или e-mail адрес</p>
                    </div>
                    <input className='input' placeholder='Логин' name='username' id='u' type="text" />
                    <div style={{ width: "55%", textAlign: "justify", margin: "-25px" }}>
                        <p style={{ fontSize: 13, color: "gray" }}>Контрольная строка для смены пароля, а также ваши регистрационные данные, будут высланы вам на email.</p>
                    </div>
                    <Link className="navbar_link" to={"/personal"}>
                        <button className='button3' id="ss" type='submit'>Выслать</button>
                    </Link>
                </div>
            </div>
        </div>
    )
}