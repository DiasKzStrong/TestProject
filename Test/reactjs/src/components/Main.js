import React from 'react'
import "./css/Main.css"

export const Main = () => {
    return (
        <div className='main-container'>
            <div className='statistic-block'>
                <div className='statistic-item'>
                    <div className='statistics'>
                        <img src="../../../static/star.svg" />
                        <h3 style={{fontSize: "30px", fontWeight: 600}}>36332</h3>
                        <p style={{fontSize: "10px"}}>Тестов и квизов</p>
                    </div>
                    <div className='statistics'>
                        <img src='../../../static/people.svg'/>
                        <h3 style={{fontSize: "30px", fontWeight: 600}}>87583</h3>
                        <p style={{fontSize: "10px"}}>Членов сообщества</p>
                    </div>
                    <div className='statistics'>
                        <img src="../../../static/peoplenew.svg" />
                        <h3 style={{fontSize: "30px", fontWeight: 600}}>31878</h3>
                        <p style={{fontSize: "10px"}}>Посетителей</p>
                    </div>
                </div>
            </div>
            <div className='main-block'>
                <div className='main-item'>
                    <div className='main-information'>
                        <div className='main-text'>
                            <h1 style={{ color: "white" }}>Актуальные тесты</h1>
                            <p style={{ color: "#dfdfdf", fontSize: 16 }}>Самые высокооцененные тесты от наших авторов за неделю.</p>
                        </div>
                        <div className='main-all'>
                            <button className='button2'>Все тесты</button>
                        </div>
                    </div>
                </div>
                <div className='main-card-block'>
                    <div className='card-item'>
                        <div className='card-img-block'>
                            <img className='card-img' src="https://pikuco.ru/upload/test_stable/e54/e540241afd82d34d58a21f76f1d7da13.jpg" />
                        </div>
                        <div className='card-information'>
                            <h2>Лучший Мультфильм (2010-2015)</h2>
                            <p>Lorem*5</p>
                        </div>
                    </div>
                    <div className='card-item'>
                        <div className='card-img-block'>
                            <img className='card-img' src="https://pikuco.ru/upload/test_stable/232/23253fe82de4c6cb8b499924da833ae8.jpg" />
                        </div>
                        <div className='card-information'>
                            <h2>Викторина на знание стран | Часть 1</h2>
                            <p>Lorem*5</p>
                        </div>
                    </div>
                    <div className='card-item'>
                        <div className='card-img-block'>
                            <img className='card-img' src="https://pikuco.ru/upload/test_stable/347/347e4f6dc90425fecdbd3341e1bf5f89.jpg" />
                        </div>
                        <div className='card-information'>
                            <h2>Лучший игрок в истории футбола</h2>
                            <div className='card-description'>
                                <p>Здесь вы сможете выбрать лучшего по вашему мнению игрока за всю историю футбола</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}