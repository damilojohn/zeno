import React from 'react';
// import './navbar.css'
// import image from '/src/assets/zeno..png'
import image from '/src/assets/Vector.png';
import image1 from '/src/assets/Vector (1).png';
// import image2 from '/src/assets/menu.svg';
import hamburger from '../../../assets/menu.svg';

const Navbar = () => {
  return (
    <>
      <div className="md:hidden 2xl:flex  bg-zenno-white justify-between px-[3.12rem] py-[2.31rem] w-auto shadow-lg items-baseline">
        <div className="text-zenno-black w-84">
          <img src={image} alt="zeeno" className="image-style-1" />
        </div>
        <div className="center ">
          <ul className="flex gap-space400">
            <li className="text-zenno-black text-center text-base hover:underline w-51 h-17">
              Home
            </li>
            <li className="text-zenno-black text-center text-base hover:underline w-75 h-17">
              About Us
            </li>
            <li className="text-zenno-black text-center text-base hover:underline  h-17">
              Contact
            </li>
          </ul>
        </div>
        <div className="search">
          <img src={image1} alt="" className="flex w-18 h-18 item-center" />
        </div>
      </div>
      {/* MOBILE */}
      <div className="2xl:hidden md:flex  bg-zenno-white justify-between py-[2.31rem] w-auto items-baseline mr-[0.81rem] ml-[0.81rem]">
        <div className="text-zenno-black w-84">
          <img src={image} alt="zeeno" className="image-style-1" />
        </div>

        <div className="hambuger">
          <img src={hamburger} alt="" className="flex w-18 h-18 item-center" />
        </div>
      </div>
    </>
  );
};

export default Navbar;
