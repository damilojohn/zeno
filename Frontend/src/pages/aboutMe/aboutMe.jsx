import Navbar from '../../component/molecule/navbar/navbar';
import React from 'react';

const About = () => {
  return (
    <>
      <Navbar />
      <div className="h-[27.5rem] flex justify-center flex-col items-center px-[23.94rem] py-[4.69rem] bg-zenno-aboutw gap-[0.625rem]">
        <div className="flex flex-col items-center gap-[2.75rem]">
          <h1 className="text-[2.25rem] font-bold leading-[3.36rem] text-zenno-aboutb">
            About Us
          </h1>
          <div>
            <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-justify w-[31.125rem]">
              Zeeno, named after the first librarian of the library of Alexandria,
              Zenodotus of Ephesus, Zeno is a book recommendation service that gives users
              the ability to take direct control of their journey in exploring the amazing
              world of books. Using machine learning and semantic search.{' '}
            </p>{' '}
            <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-justify w-[31.125rem] mt-[2rem]">
              Zeno helps you find books about descriptions provided by you, with Zeno, the
              limits of your search knowledge are only bounded by your imagination.
            </p>
          </div>
        </div>
      </div>
    </>
  );
};

export default About;
