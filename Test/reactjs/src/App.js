import axios from "axios";
import { useEffect, useState } from "react";
import { HashRouter, Route, Routes } from "react-router-dom";
import { CategoryTests } from "./components/CategoryTests";
import { Header } from "./components/Header";
import { Login } from "./components/Login";
import { Main } from "./components/Main";
import { Profile } from "./components/Profile";
import { Register } from "./components/Register";
import { StartTest } from "./components/StartTest";
import { Tests } from "./components/Tests";
import { AuthContext } from "./components/context";
import { Recovery } from "./components/Recovery";
import { EditProfile } from "./components/EditProfile";

function App() {

  const [isAuth, setIsAuth] = useState(false)

  useEffect(() => {
    if (localStorage.getItem('auth')) {
      setIsAuth(true)
    }
  }, [])

  const [loginUser, setLoginUser] = useState(
    JSON.parse(localStorage.getItem('loginUser'))
  )

  useEffect(() => {
    localStorage.setItem('loginUser', JSON.stringify(loginUser))
  }, [loginUser])

  let [category, setCategory] = useState([]);

  useEffect(() => {
    const apiUrl = 'http://127.0.0.1:8000/api/category';
    axios.get(apiUrl).then((resp) => {
      const allPersons = resp.data;
      setCategory(allPersons);
    });
  }, [setCategory]);

  console.log(category);

  return (
    <AuthContext.Provider value={{
      isAuth,
      setIsAuth
    }}>
      <HashRouter>
        <Header loginUser={loginUser} />
        <Routes>
          <Route path='/' element={<Main />} />
          <Route path='/login' element={<Login loginUser={loginUser} setLoginUser={setLoginUser} />} />
          <Route path='/register' element={<Register />} />
          <Route path='/recovery' element={<Recovery />} />
          <Route path='/tests' element={<Tests category={category} />} />
          <Route path='/category/:name' element={<CategoryTests category={category} />} />
          <Route path='/category/:name/:id' element={<StartTest category={category} />} />
          <Route path='/personal' element={<Profile loginUser={loginUser} setLoginUser={setLoginUser} />} />
          <Route path='/edit' element={<EditProfile loginUser={loginUser} setLoginUser={setLoginUser} />} />
          <Route path="*" element={<Main/>}/>
          <Route path="/password/reset/:urlbase64/:tokens" element={<Register/>}/>
        </Routes>
      </HashRouter>
    </AuthContext.Provider>
  );
}

export default App;
