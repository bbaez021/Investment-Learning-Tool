import React from 'react'
import { Container, Row } from 'react-bootstrap'
import './LandingPage.css'

import { useNavigate } from 'react-router-dom'

const LandingPage = () => {

  const navigate = useNavigate()
  const navigateLogin = () => {
    navigate('/login')
  }

  const navigateRegister = () => {
    navigate('/register')
  }

 
  return (
    <div className='main'>
      <Container>
        <Row>
          <div className='intro'>
            <div>
              <h1 className='title'>
                Welcome to Our Portfolio Management Application
              </h1>


              <button onClick={navigateLogin}>Login</button>
              <button onClick={navigateRegister}>Register</button>
              
              
              
            </div>
          </div>
          <div>
          </div>
        </Row>
      </Container>
    </div>
  )
}

export default LandingPage
