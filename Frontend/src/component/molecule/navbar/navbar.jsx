import React from 'react'
import './navbar.css'
import image from '/src/assets/zeno..png'

const Navbar = () => {
  return (
    <div className='navbar'>
      <ul>
        <li>About Us</li>
        {/* <li className='logo'>zeno</li> */}
        <img src={image} alt="logo" />
        <li>Use Cases</li>
      </ul>

    </div>
  )
}

export default Navbar
