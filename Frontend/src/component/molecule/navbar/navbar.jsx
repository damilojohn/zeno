import React from 'react';
// import './navbar.css'
// import image from '/src/assets/zeno..png'
import image from '/src/assets/Vector.png';
import image1 from '/src/assets/Vector (1).png';
// import image2 from '/src/assets/menu.svg';
import hamburger from '../../../assets/menu.svg';
import exit from '../../../assets/menu (1).svg';
import line from '../../../assets/Line 7.png';
import {Link} from 'react-router-dom';
import {useState} from 'react';

const Navbar = () => {
  const [menuOpen, setMenuOpen] = useState(false);
  const handleMenu = () => {
    setMenuOpen(!menuOpen);
  };
  const handleCloseMenu = () => {
    setMenuOpen(false);
  };
  return (
    <>
      <div className="md:hidden lg:hidden 2xl:flex  bg-zenno-white justify-between px-[3.12rem] py-[2.31rem] w-auto shadow-lg items-baseline">
        <div className="text-zenno-black w-84">
          <img src={image} alt="zeeno" className="image-style-1" />
        </div>
        <div className="center ">
          <ul className="flex gap-space400">
            <li className="text-zenno-black text-center text-base hover:underline w-51 h-17">
              Home
            </li>
            <li className="text-zenno-black text-center text-base hover:underline w-75 h-17">
              <Link to="/aboutUs">About Us</Link>
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
      {/* <div className="2xl:hidden lg:flex md:flex  bg-zenno-white justify-between py-[2.31rem] w-auto items-baseline mr-[0.81rem] ml-[0.81rem]">
        <div className="text-zenno-black w-84">
          <img src={image} alt="zeeno" className="image-style-1" />
        </div>

        <div onClick={handleMenu} className="fixed">
          {!menuOpen ? (
            <img src={exit} className="flex h-[18px] item-center mt-space0 mb-[8px]" />
          ) : (
            <img src={hamburger} className="flex w-[18px] h-[18px] item-center" />
          )}
        </div>

        <nav
          className={
            !menuOpen
              ? 'w-[13rem] fixed h-full border-r bg-zenno-1white top-space0 right-space0 z-50 border-r-gray-900'
              : 'fixed left-[-100%]'
          }
        >
          <div>
            {' '}
            <img src={exit} className="flex w-[18px] h-[18px] item-center" />
          </div>
          <ul className="flex flex-col items-center justify-center h-full uppercase p-[4px]">
            <li className="p-[4px] border-b border-gray-600">Home</li>
            <li className="p-[4px] border-b border-gray-600">About Us</li>
            <li className="p-[4px] border-b border-gray-600">Contact</li>
          </ul>
        </nav> 
      </div> */}
      <div className="2xl:hidden lg:flex md:flex bg-zenno-white justify-between py-[2.31rem] w-auto items-baseline mr-[0.81rem] ml-[0.81rem]">
        <div className="text-zenno-black w-84">
          <img src={image} alt="zeeno" className="image-style-1" />
        </div>

        <div onClick={handleMenu} className="">
          {menuOpen ? (
            <img
              src={exit}
              className="flex h-[18px] w-[18px] item-center mt-space0 transition-all duration-700 ease-in-out"
            />
          ) : (
            <img
              src={hamburger}
              className="flex w-[18px] h-[18px] item-center transition-all duration-700 ease-in-out"
            />
          )}
        </div>

        {menuOpen && (
          <div className="w-[13rem] fixed h-full border-[0.6rem] bg-zenno-1white mt-space0 top-space0 right-space0 z-50 border-zenno-1white transition-all ease-in-out duration-700">
            <div className="flex justify-end p-[4px] relative top-[1.7rem]">
              <img
                src={exit}
                className="flex w-[18px] h-[18px] item-center border-zenno-3black border-b-2"
                onClick={handleCloseMenu}
              />
            </div>

            <ul className="flex flex-col items-center justify-center h-full uppercase p-[4px] md:pb-[8rem] sm:pb-[33rem]">
              <li className="p-[4px]">
                {' '}
                <img src={line} alt="" className="flex flex-col" />
              </li>
              <li className="p-[4px] border-b border-gray-600">Home</li>
              <li className="p-[4px] border-b border-gray-600">About Us</li>
              <li className="p-[4px] border-b border-gray-600">Contact</li>
            </ul>
          </div>
        )}
      </div>
    </>
  );
};

export default Navbar;
{
  /* <button className="" onClick={() => setMenuOpen(!menuOpen)}>
  {menuOpen ? (
    <img
      src={exit}
      onClick={() => setMenuOpen(false)}
      className="flex h-[18px] item-center mt-space0 mb-[8px]"
    />
        <div onClick={handleMenu} className="ease-in-out duration-500">

  ) : (
    <img
      src={hamburger}
      onClick={() => setMenuOpen(true)}
      className="flex w-[18px] h-[18px] item-center"
    />
  )}
</button>;
  <div className="fixed h-full bg-black/50 backdrop-blur-sm z-50 w-full">
fixed h-full bg-black/50 backdrop-blur-sm top-space0 right-space0 z-50 -translate-x-full

"text-black bg-zenno-1white absolute top-space0 right-space0 h-screen w-[13rem] p-[8px] gap-[8rem] flex items-center flex-col*/
}
