import React from 'react';
import img from '/src/assets/Isometric Stickers - Books 1.png';
// import './header.css'

const Header = () => {
  return (
    <>
      <div className="md:hidden 2xl:flex items-center justify-center">
        <h1 className="text-zenno-black flex items-center justify-center text-6xl font-bold  w-[47.375rem]  h-[8.3125rem] text-center text-[3.75rem]  leading-[4.00875rem] mt-space1000">
          Discover books that <br />
          match your imagination.
        </h1>
      </div>
      {/* mobile */}
      <div className="2xl:hidden md:flex items-center justify-center">
        <h1 className="text-zenno-black flex items-center justify-center font-bold  w-[47.375rem]  h-[8.3125rem] text-center text-[1.8125rem]  leading-[1.93756rem] mt-[3.87rem] mr-[0.81rem] ml-[0.81rem]">
          Discover books that <br />
          match your imagination.
        </h1>
      </div>
    </>
  );
};

export default Header;
