import React from 'react'
import './navbar.css'
// import image from '/src/assets/zeno..png'
import image from '/src/assets/Vector.png'
import image1 from '/src/assets/Vector (1).png'

const Navbar = () => {
  return (
    <div className='navbar'>
      {/* <ul>
        <li>About Us</li>
       
        <img src={image} alt="logo" />
        <li>Use Cases</li>
      </ul> */}
      {/* /////// old prototype  */}
     
     <div className='navbar-left'><img src={image} alt="zeeno" /></div>
     <div className='center '>
      <ul>
        <li>Home</li>
        <li>About Us</li>
        <li>Contact</li>
      </ul>
     </div>
     <div className='navbar-right'><img src={image1} alt="" /></div>




    </div>
  )
}

export default Navbar
