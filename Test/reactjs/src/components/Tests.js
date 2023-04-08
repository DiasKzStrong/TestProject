import React from 'react'
import { Link } from 'react-router-dom'
import "./css/Tests.css"

export const Tests = ({ category }) => {
  return (
    <div className='test-page-container'>
      <div className='categories-block'>
        <h2>Тесты</h2>
        <div className='categories'>
          <div className='category-wrapper'>
            {
              category.length !== 0
                ?
                category.map((item, key) => {
                  return (
                    <div key={key} className='category random'>
                      <div className='category-name'>
                        <Link style={{ color: "white" }} className="navbar_link" to={"/category/" + `${item.name}`}>
                          <p>{item.name}</p>
                        </Link>
                      </div>
                    </div>
                  )
                })
                :
                null
            }
            {/* <div className='category random'>
              <div className='category-name'>
                <p>СЛУЧАЙНЫЙ ТЕСТ</p>
              </div>
            </div>
            <div className='category animation'>
              <div className='category-name'>
                <p>АНИМАЦИЯ</p>
              </div>
            </div>
            <div className='category games'>
              <div className='category-name'>
                <p>ИГРЫ</p>
              </div>
            </div> */}
            <div className='category imige'>
              <div className='category-name'>
                <p>ИМИДЖ</p>
              </div>
            </div>
            <div className='category isskustvo'>
              <div className='category-name'>
                <p>ИСКУССТВО</p>
              </div>
            </div>
            <div className='category cinema'>
              <div className='category-name'>
                <p>КИНЕМАТОГРАФ</p>
              </div>
            </div>
            <div className='category klubnichka'>
              <div className='category-name'>
                <p>КЛУБНИЧКА</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className='sort-block'>
        <div className='sort-rating'>
          <ul className='sort-wrapper'>
            <li className='sort-item'>
              <p>Интересные</p>
            </li>
            <li className='sort-item'>
              <p>Новые</p>
            </li>
            <li className='sort-item'>
              <p>Лучшие</p>
            </li>
          </ul>
        </div>

        <div className='sort-alphabet'>
          <ul className='sort-wrapper'>
            <li className='sort-item' style={{padding: "10px 25px"}}>
              <img width={25} src='../../../static/sort-abc.svg' />
            </li>
            <li className='sort-item' style={{padding: "10px 25px"}}>
              <img width={25} src='../../../static/sort-cba.svg' />
            </li>
          </ul>
        </div>

        <div className='sort-category'>
          <select className='sort-select'>
          <option className='sort-options'>Все типы тестов</option>
            <option className='sort-options'>IT</option>
            <option className='sort-options'>Entertaiment</option>
            <option className='sort-options'>Games</option>
          </select>
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
    </div >
  )
}