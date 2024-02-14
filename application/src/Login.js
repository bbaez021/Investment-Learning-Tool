import React from 'react'
import { Row, Container } from 'react-bootstrap'

const Login = () => {
  return (
    <div className='main'>
      <Container>
        <Row>
          <div className='email'>
            <div className='email'>
              <label htmlFor='exampleInputEmail1'>Email address</label>
              <input
                type='email'
                className='form-control'
                id='email'
                aria-describedby='emailHelp'
                placeholder='Enter email'

              />
            </div>
            <div className='password'>
              <label htmlFor='exampleInputPassword1'>Enter Password</label>
              <input
                type='password'
                className='form-control'
                id='password'
                placeholder='Password'
              />
            </div>
            <button type='submit' className='register-button'>
              Login
            </button>
            <button type='submit' className='register-button'>
              Forgot Password
            </button>
          </div>
        </Row>
      </Container>
    </div>
  )
}

export default Login
