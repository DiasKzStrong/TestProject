import React, { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import "./css/StartTest.css"

export const StartTest = ({ category }) => {

    let { name, id } = useParams();
    let [categoryTests, setCategoryTests] = useState([]);

    console.log(name, id);

    useEffect(() => {
        const categoryToRender = category.find(item => item.name === name);
        if (categoryToRender) {
            setCategoryTests(categoryToRender.test);
        }
    }, [category, name]);

    return (
        <div className='startTest-container'>
            <div className='startTest-block'>
                <div className='startTest-header'>
                    <Link className='navbar_link' to={`/category/${name}`}>
                        <div style={{ display: "flex", alignItems: "center", gap: 5 }}>
                            <img src='../../../static/back.svg' />
                            <span style={{ color: "#c2c2c2" }}>Назад</span>
                        </div>
                    </Link>
                </div>
                <div className='start-card-block'>
                    {categoryTests.length !== 0
                        ?
                        categoryTests.map((item, key) => {
                            if (id == item.id) {
                                return (
                                    <div className='start-card-item'>
                                        <div className='start-card-img-block'>
                                            <img className='start-card-img' src="https://pikuco.ru/upload/test_stable/e54/e540241afd82d34d58a21f76f1d7da13.jpg" />
                                        </div>
                                        <div className='start-card-information'>
                                            <h2>{item.title}</h2>
                                            <p>Lorem*5</p>
                                        </div>
                                        <div className='start-btn'>
                                            <button className='button4'>Поехали!</button>
                                        </div>
                                    </div>
                                )
                            }
                        })
                        :
                        null
                    }
                </div>
            </div>
        </div>
    )
}