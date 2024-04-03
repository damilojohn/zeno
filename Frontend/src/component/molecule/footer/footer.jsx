import React from 'react';
import logo from '../../../assets/Logo.png';
import x from '../../../assets/X - png 0.png';
import google from '../../../assets/Google svg.png';
import facebook from '../../../assets/Facebook svg.png';
import instagram from '../../../assets/Vector (2).png';

const Footer = () => {
  return (
    <>
      <footer>
        <div className="md:hidden lg:hidden w-full h-[31.25rem] border-solid border-[2px] border-black mt-[12.25rem] flex bg-zenno-3black text-zenno-white p-[2rem] 2xl-max:flex 2xl-max:justify-center 2xl-max:items-center">
          <div className="relative w-[24.5624rem] xl:w-full">
            <img
              src={logo}
              alt=""
              className="absolute left-[0.3125rem] bottom-[-1.72869rem] max-w-none 2xl-max:bottom-[-13.72869rem]"
            />
            {/* osition: absolute; left: 2.3125rem; bottom: 10.27131rem width: 24.5624rem; 0.3125rem*/}
          </div>
          <div className="flex gap-[10rem] pt-[3rem] sm:block">
            <div className="">
              <ul className="gap-[1.19rem] flex flex-col">
                <li className="text-zenno-1white font-semibold leading-normal text-[1.25rem]">
                  Zeeno
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Home
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  About us
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Contact
                </li>
                {/* flex items-end gap-[1.19rem] absolute left-[19.75rem] top-[4.6875rem]
                  flex-co */}
              </ul>
            </div>
            <div>
              <ul className="gap-[1.19rem] flex flex-col">
                <li className="text-zenno-1white font-semibold leading-normal text-[1.25rem]">
                  Support
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  FAQs
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Blogs
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Cookies Policy
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Privacy Policy
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Terms of use
                </li>
              </ul>
            </div>
            <div>
              <ul className="gap-[1.19rem] flex flex-col">
                <li className="text-zenno-1white font-semibold leading-normal text-[1.25rem]">
                  Discorver
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Journals
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Proceedings
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Books
                </li>
              </ul>
            </div>
            <div>
              <div className="gap-[1.19rem] flex flex-col">
                <p className="text-zenno-1white font-semibold leading-normal text-[1.25rem]">
                  Socials
                </p>
                <ul className="flex items-center gap-[1rem] ml-[-2rem]">
                  <li>
                    <img src={facebook} alt="" className="relative top-[0.2rem]" />
                  </li>
                  <li>
                    <img src={instagram} alt="" />
                  </li>
                  <li>
                    <img src={x} alt="" />
                  </li>
                  <li>
                    <img src={google} alt="" />
                  </li>
                </ul>
              </div>
              <div className="gap-[1.19rem] flex flex-col">
                <p className="text-zenno-1white font-semibold leading-normal text-[1.25rem]">
                  Contact
                </p>
                <ul className="gap-[1.19rem] flex flex-col">
                  <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                    Mail:Zeeno@gmail.com
                  </li>
                  <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                    Phone:+2348081738984
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </footer>
      {/* MOBILE */}

      <footer className="w-full h-[60.75rem] bg-zenno-3black mt-[4.18rem] 2xl:hidden sm:block md:block sm:w-full lg:block 2xl-max:hidden">
        <div className="p-[4rem]">
          <div className="logo">
            <img src={logo} alt="" />
          </div>
          <div className="flex pt-[3rem] justify-center md:gap-[5rem] lg:gap-[12rem]">
            <div className="gap-[4rem] flex flex-col pl-[2.25rem]">
              <ul className="gap-[1.19rem] flex flex-col">
                <li className="text-zenno-1white font-semibold leading-normal text-[1.25rem]">
                  Zeeno
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Home
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  About us
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Contact
                </li>
              </ul>

              <ul className="gap-[1.19rem] flex flex-col">
                <li className="text-zenno-1white font-semibold leading-normal text-[1.25rem]">
                  Discorver
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Journals
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Proceedings
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Books
                </li>
              </ul>
            </div>
            <div className="gap-[3.8rem] flex flex-col w-max">
              <ul className="gap-[1.19rem] flex flex-col pr-[1.81rem]">
                <li className="text-zenno-1white font-semibold leading-normal text-[1.25rem]">
                  Support
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  FAQs
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Blogs
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Cookies Policy
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Privacy Policy
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Terms of use
                </li>
              </ul>
              <div className="flex flex-col gap-[1rem]">
                <p className="text-zenno-1white font-semibold leading-normal text-[1.25rem]">
                  Socials
                </p>
                <ul className="flex items-center gap-[1rem] ml-[-1rem]">
                  <li>
                    <img src={facebook} alt="" className="relative top-[0.2rem]" />
                  </li>
                  <li>
                    <img src={instagram} alt="" />
                  </li>
                  <li>
                    <img src={x} alt="" />
                  </li>
                  <li>
                    <img src={google} alt="" />
                  </li>
                </ul>
              </div>
            </div>
          </div>
          <div className="flex justify-center items-center mt-[2.23rem]">
            {' '}
            <div className="gap-[1.19rem] flex flex-col justify-center items-baseline">
              <p className="text-zenno-1white font-semibold leading-normal text-[1.25rem]">
                Contact
              </p>
              <ul className="gap-[1.19rem] flex flex-col">
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Mail:Zeeno@gmail.com
                </li>
                <li className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                  Phone:+2348081738984
                </li>
              </ul>
            </div>
          </div>
          <div className="flex justify-center items-center text-center mt-[3.37rem]">
            <div>
              <p className="text-zenno-clear leading-normal font-normal text-[1.125rem]">
                Copyright Zeeno2023.
                <br />
                All Rights Reserved
              </p>
            </div>
          </div>
        </div>
      </footer>
    </>
  );
};

export default Footer;
