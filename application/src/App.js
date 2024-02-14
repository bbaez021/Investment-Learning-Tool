import './App.css'
import React from 'react'
import Footer from './components/Footer/Footer'
import Header from './components/Header/Header'
import LandingPage from './screens/LandingPage/LandingPage'
import Login from './Login'
import Register from './Register'

import { Routes, Route } from 'react-router-dom'
import ProfileScreen from './screens/ProfileScreen/ProfileScreen'

const App = () => (
  <>
    <Header />
    <main>

      <Routes>
        <Route exact path='/' element={<LandingPage />} />
        <Route exact path='/login' element={<Login />} />
        <Route path='/register' element={<Register />} />
        <Route path='/profile' element={<ProfileScreen />} />
      </Routes>
    </main>

    <Footer />
  </>
)

export default App