import { Link } from 'react-router-dom';
import "./css/Profile.css"
import { useContext } from 'react';
import { AuthContext } from './context';

export const Profile = ({ loginUser, setLoginUser }) => {

  const { isAuth, setIsAuth } = useContext(AuthContext);

  const logOut = () => {
    // loginUser.splice(0, 1)
    setLoginUser(loginUser)
    localStorage.setItem("loginUser", JSON.stringify(loginUser));
    setIsAuth(false)
    localStorage.removeItem('auth')
  }

  console.log(loginUser);


  return (
    <div className='profile-container'>
      <div className='profile-block'>
        <div className='profile-functions'>
          <h1 style={{ color: "#fff" }}>Личный кабинет</h1>
          <div>
            <Link className="navbar_link" to={"/edit"}>
              <img src='../../../static/settings.svg' />
            </Link>
          </div>
          <div>
            <Link className="navbar_link" to={"/login"}>
              <img width={25} onClick={logOut} src='../../../static/logout.svg' />
            </Link>
          </div>
        </div>
        <div className='profile-wrapper'>
          <div className='user-login-block'>
            <img className='avatar' src='../../../static/noavatar.svg' />
            <h2 style={{ color: "white" }}>{loginUser.user.username}</h2>
          </div>
          <div className='user-statistics'>
            <div className='user-statistic-block'>
              <div className='user-statistic-item'>
                <div className='user-statistic-img'>
                  <img width={80} src='../../../static/profile-rating.svg' />
                </div>
                <div className='user-statistic-text'>
                  <h1 style={{ fontSize: "30px" }}>1</h1>
                  <p>Рейтинг</p>
                </div>
              </div>

              <div className='user-statistic-item'>
                <div className='user-statistic-img'>
                  <img width={80} src='../../../static/profile-passed.svg' />
                </div>
                <div className='user-statistic-text'>
                  <h1 style={{ fontSize: "30px" }}>1</h1>
                  <p>Тест пройден</p>
                </div>
              </div>

              <div className='user-statistic-item'>
                <div className='user-statistic-img'>
                  <img width={80} src='../../../static/profile-comments.svg' />
                </div>
                <div className='user-statistic-text'>
                  <h1 style={{ fontSize: "30px" }}>1</h1>
                  <p>Комментариев</p>
                </div>
              </div>

              <div className='user-statistic-item'>
                <div className='user-statistic-img'>
                  <img width={80} src='../../../static/profile-mark-good.svg' />
                </div>
                <div className='user-statistic-text'>
                  <h1 style={{ fontSize: "30px" }}>1</h1>
                  <p>Лайк</p>
                </div>
              </div>

              <div className='user-statistic-item'>
                <div className='user-statistic-img'>
                  <img width={80} src='../../../static/profile-average.svg' />
                </div>
                <div className='user-statistic-text'>
                  <h1 style={{ fontSize: "30px" }}>1</h1>
                  <p>Средний балл</p>
                </div>
              </div>

              <div className='user-statistic-item'>
                <div className='user-statistic-img'>
                  <img width={80} src='../../../static/profile-added.svg' />
                </div>
                <div className='user-statistic-text'>
                  <h1 style={{ fontSize: "30px" }}>1</h1>
                  <p>Рейтинг</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  )
}