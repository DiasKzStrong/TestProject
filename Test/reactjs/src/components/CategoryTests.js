import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom';
import "./css/Tests.css"

export const CategoryTests = ({ category }) => {


    let { name } = useParams();
    let [categoryTests, setCategoryTests] = useState([]);

    useEffect(() => {
        const categoryToRender = category.find(item => item.name === name);
        if (categoryToRender) {
            setCategoryTests(categoryToRender.test);
        }
    }, [category, name]);

    

    return (
        <>
            <div className='categoryTest-container'>
                <div className='main-card-block'>
                    {categoryTests.length !== 0
                        ?
                        categoryTests.map((item, key) => {
                            let id = item.id
                            return (
                                <div key={key} className='card-item'>
                                    <div className='card-img-block'>
                                        <img className='card-img' src="https://pikuco.ru/upload/test_stable/e54/e540241afd82d34d58a21f76f1d7da13.jpg" />
                                    </div>
                                    <div className='card-information'>
                                        <Link className='navbar_link' to={`/category/${name}/${id}`}>
                                            <h2 style={{color: "white"}}>{item.title}</h2>
                                        </Link>
                                        <p>Lorem*5</p>
                                    </div>
                                </div>
                            )
                        })
                        :
                        null
                    }
                </div>
            </div>
        </>
    )
}