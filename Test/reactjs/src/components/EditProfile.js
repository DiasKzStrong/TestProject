import React, { useState } from 'react'
import "./css/EditProfile.css"
import { Link } from 'react-router-dom'

export const EditProfile = ({loginUser, setLoginUser}) => {

    const [login, setLogin] = useState("")

    const loginHandler = (e) => {
        setLogin(e.target.value)
    }

    return (
        <div>
            <div className='edit-header'>
                <h1>Редактирование профиля</h1>
                <div>
                    <Link className='navbar_link' to={"/personal"}>
                        <p style={{color: "#fff", fontSize: 15}}>К ПРОФИЛЮ</p>
                    </Link>
                </div>
            </div>
            <div className='edit-container'>
                <div className='user-login-block'>
                    <img className='avatar' src='../../../static/noavatar.svg' />
                    <h2 style={{ color: "white" }}>{loginUser.user.username}</h2>
                </div>
                <div className='edit-block'>
                    <div className='edit-item'>
                        <label>
                            <p style={{ fontSize: 20, color: "#fff" }}>Логин</p>
                        </label>
                        <input className='input2' onChange={e => loginHandler(e)} value={loginUser.user.username} type="text" name="username" />
                    </div>
                    <div className='edit-item'>
                        <label>
                            <p style={{ fontSize: 20, color: "#fff" }}>Почта</p>
                        </label>
                        <input className='input2' value={loginUser.user.email} type="text" name="username" />
                    </div>
                    <button className='button'>СОХРАНИТЬ ИЗМЕНЕНИЯ</button>
                </div>
                <div>
                    <button className='button2'>ИЗМЕНИТЬ ПАРОЛЬ</button>
                </div>
            </div>
        </div>
    )
}