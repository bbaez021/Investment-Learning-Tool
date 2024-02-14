import React from 'react';
import { Container, Row } from 'react-bootstrap'

const Register = () => {
  return (
    <div className='main'>
      <Container>
        <Row>
          <div className='email'>
            <form>
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
                <label htmlFor='exampleInputPassword1'>Password</label>
                <input
                  type='password'
                  className='form-control'
                  id='password'
                  placeholder='Password'
                />
              </div>
              <div className='password-confirmation'>
                <label htmlFor='exampleInputPassword1'>Confirm Password</label>
                <input
                  type='password'
                  className='form-control'
                  id='confirmPassword'
                  placeholder='Confirm Password'
                />
              </div>
              <button type='submit' className='register-button'>
                Register
              </button>
            </form>
          </div>
        </Row>
      </Container>
    </div>
  )
}

export default Register
