import React, { useState } from 'react'
import Toggle from '../Toggle'
import Container from 'react-bootstrap/Container'
import Nav from 'react-bootstrap/Nav'
import Navbar from 'react-bootstrap/Navbar'
import NavDropdown from 'react-bootstrap/NavDropdown'

const Header = () => {
  
  const [toggled, setToggled] = useState(false)
  return (
    <Navbar bg='light' expand='lg'>
      <Container>
        <Toggle onChange={(event) => setToggled(event.target.checked)} />
        <p> Safe Mode is {toggled ? "On": "Off"}</p>
        <Navbar.Brand href='/'>Group 23 Stock Portfolio</Navbar.Brand>
        <Navbar.Toggle aria-controls='basic-navbar-nav' />
        <Navbar.Collapse id='basic-navbar-nav'>
          <Nav className='me-auto'>
            <Nav.Link href='#home'>Portfolio</Nav.Link>
            <NavDropdown title='My Profile' id='basic-nav-dropdown'>
              <NavDropdown.Item href='/profile'>
                Profile Settings
              </NavDropdown.Item>
              <NavDropdown.Item href='#action/3.2'>Logout</NavDropdown.Item>
              <NavDropdown.Divider />
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
        
      </Container>
    </Navbar>

  )
}

export default Header
