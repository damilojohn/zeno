import React from 'react'
// import './navbar.css'
// import image from '/src/assets/zeno..png'
import image from '/src/assets/Vector.png'
import image1 from '/src/assets/Vector (1).png'

const Navbar = () => {
  return (
    // <div className='navbar'>
    //   {/* <ul>
    //     <li>About Us</li>

    //     <img src={image} alt="logo" />
    //     <li>Use Cases</li>
    //   </ul> */}
    //   {/* /////// old prototype  */}

    //  <div className='navbar-left'><img src={image} alt="zeeno" /></div>
    //  <div className='center '>
    //   <ul>
    //     <li>Home</li>
    //     <li>About Us</li>
    //     <li>Contact</li>
    //   </ul>
    //  </div>
    //  <div className='navbar-right'><img src={image1} alt="" /></div>




    // </div>
    <div className="flex  bg-zenno-white justify-between px-10 py-5 w-auto shadow-md">
      <div className='navbar-left'><img src={image} alt="zeeno" /></div>
      <div className='center '>
      
        <ul className="flex space-x-4">
          <li className="text-blue-500 hover:underline">Home</li>
          <li className="text-blue-500 hover:underline">About Us</li>
          <li className="text-blue-500 hover:underline">Contact</li>
        </ul>
      </div>
      <div className='search' >
        <img src={image1} alt="" />
      </div>


    </div>
  )
}

export default Navbar
