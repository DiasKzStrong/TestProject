import React, { useContext, useState } from 'react';
import { Link, Outlet } from 'react-router-dom';
import "./css/Header.css"
import { AuthContext } from './context';

export const Header = ({ loginUser }) => {
    const { isAuth, setIsAuth } = useContext(AuthContext);

    return (
        <div>
            <div className="navbar">
                <div className='logo-nav'>
                    <Link className="navbar_link" to={"/"}>
                        <img className='logo-img' src='../../../static/logoDB.png' />
                    </Link>
                </div>
                <ul className="item_block">
                    <li>
                        <Link className="navbar_link" to={"/"}>
                            <p className='nav-text'>Главная</p>
                        </Link>
                    </li>
                    <li>
                        <Link className="navbar_link" to={"/tests"}>
                            <p className='nav-text'>Тесты</p>
                        </Link>
                    </li>
                    <li>
                        <Link className="navbar_link" to={"/top"}>
                            <p className='nav-text'>Топы</p>
                        </Link>
                    </li>
                    <li>
                        <Link className="navbar_link" to={"/editor"}>
                            <p className='nav-text'>Создать</p>
                        </Link>
                    </li>
                </ul>
                <div className='account-nav' style={{ display: isAuth ? "none" : "block" }}>
                    <Link className="navbar_link" to={"/login"}>
                        <button className='button'> ВХОД</button>
                    </Link>
                </div>
                <div className='account-nav' style={{ display: isAuth ? "block" : "none" }}>
                    <Link className="navbar_link" to={"/personal"}>
                        <button className='button5'>
                            <img style={{ width: 20, borderRadius: "10px" }} src='../../../static/noavatar.svg' />
                            {loginUser.user.username}
                        </button>
                    </Link>
                </div>
            </div>
            <br />
            <br />
            <br />
            <br />
            <Outlet />
        </div >
    )
}


// const appDiv = document.getElementById('Header')
// render(<Header />,appDiv)