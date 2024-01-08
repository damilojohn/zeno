import Header from '../../component/organism/header/header.jsx';
import React, {Suspense} from 'react';
import {useState, useEffect} from 'react';
import axios from 'axios';

import Loader from '../../loader/loader';
import BookModal from '../../modal/modal';
import Navbar from '../../component/molecule/navbar/navbar';
import zenno3 from '../../assets/Isometric Stickers - Books 1 (3).png';
import zenno2 from '../../assets/Isometric Stickers - Books 1 (2).png';
import zenno from '../../assets/zeno. (1).png';
import icon from '../../assets/Frame.svg';
import logo from '../../assets/Logo.png';
import x from '../../assets/X - png 0.png';
import google from '../../assets/Google svg.png';
import facebook from '../../assets/Facebook svg.png';
import instagram from '../../assets/Vector (2).png';
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
// import { faSearch } from '@fortawesome/free-solid-svg-icons';

const Home = () => {
  const [userInput, setUserInput] = useState('');
  const [loading, setLoading] = useState(false);

  const [data, setData] = useState(null);
  const [selectedBook, setSelectedBook] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const handleInputChange = e => {
    e.preventDefault();
    setUserInput(e.target.value);
  };

  const fetchData = async () => {
    setLoading(true);
    try {
      const postData = {
        query: userInput,
      };
      const resp = await axios.post(
        'https://hfex3k70e0.execute-api.us-east-1.amazonaws.com/prod',
        postData
      );
      setLoading(false);

      setData(resp.data);
      console.log(resp.data);
    } catch (error) {
      setLoading(false);

      console.log(error);
    }
  };
  const handleClick = e => {
    e.preventDefault();
    fetchData();
  };
  const handleClickKeyPress = e => {
    if (e.key === 'Enter') {
      e.preventDefault();
      fetchData();
    }
  };
  // const handleBookClick = (books) => {
  //     setSelectedBooks(books);
  //     setIsModalOpen(true);
  // };
  // const closeBookModal = () => {
  //     // setSelectedBooks(null);
  //     setIsModalOpen(false);
  // };
  const handleBookClick = book => {
    console.log('Selected Book:', book);
    setSelectedBook(book);
    setIsModalOpen(true);
  };

  const closeBookModal = () => {
    setSelectedBook(null);
    setIsModalOpen(false);
  };
  return (
    <React.Fragment>
      <div className="main-container">
        <Navbar />
        {/* <Preload loading={loading} /> */}
        {loading && <Loader loading={loading} />}
        <Header />
        {/* <div className='text-header'>
                    Discover books that <br />
                    match your imagination.
                </div> */}
        <div className="form-main">
          <form className="form-container" action="#">
            <input
              type="text"
              id="searchInput"
              name="searchText"
              value={userInput}
              onChange={handleInputChange}
              placeholder="search for books based on your description"
              onKeyDown={handleClickKeyPress}
              className="w-[42.3125rem] pt-[0.75rem] pb-[1.19rem] pr-[2.5rem] pl-[2.5rem] outline-none h-[3rem] "
            />
            <button
              type="button"
              onClick={handleClick}
              className="absolute right-[10px] top-[4px] bg-zenno-orange pt-[0.88rem] pb-[0.81rem] justify-center w-[12.625rem] flex items-center rounded-r-[1.375rem] h-[3rem] mt-[-4px] mr-[-11px]"
            >
              <div className="text-zenno-white flex item-center justify-center gap-[0.5rem] text-[1.25rem] font-bold not-italic leading-[1.65rem] tracking-[-0.0025rem]">
                {' '}
                {/* padding: 0.875rem 1.75rem 0.8125rem 1.25rem; */}
                <div className="h-[1.1875rem] flex items-center justify-center gap-[0.5rem]  pt-[0.88rem] pb-[0.81rem] pl-[1.25rem] pr-[1.75rem]">
                  {' '}
                  {loading ? 'Loading...' : 'Search book  '}
                  <img src={icon} alt="" />
                </div>
              </div>
            </button>
          </form>
        </div>
        <div className="flex items-center justify-center text-[1.125rem] text-center not-italic font-bold leading-[1.68705rem] text-zenno-2black mr-[13rem] ml-[13rem]">
          <p>
            {/* Unleash the power of machine learning and sematic search with <b>zeno</b>{' '}
            .Find books <br />
            that match your unique intrests and explore the limitless word of knowledge.{' '} */}
            Unleash the power of machine learning and semantic search with{' '}
            <b className="italic font-normal">Zeeno</b>. Find books that <br /> match your
            unique interests and explore the limitless word of book recommendations
          </p>
        </div>
        {/* <div className='about'>
                    <div className='left-about'>
                        <p>Zenno allows you to find books based on description provided by you.Using machine learning and sematic search, you could think of the process as talking to a liberian.</p>

                    </div>
                    <div className='right-about'>
                        <p>Named after zenolotus,the first libarian of the library of Alenardines.</p>
                    </div>
                </div> */}

        <Suspense fallback={<p>loading....</p>}>
          <div className="main-container">
            {data &&
              data.books.map(book => (
                <div className="display-container" key={book.isbn10}>
                  <div className="title">
                    <p> {book.title} </p>
                  </div>
                  <div className="thumbnail">
                    <img src={book.thumbnail} alt=""></img>
                  </div>
                  <div className="author">
                    {' '}
                    <p> {book.authors} </p>
                  </div>
                  <button onClick={() => handleBookClick(book)}>View Details</button>
                </div>
              ))}
            {/* <BookModal books={selectedBooks} onClose={closeBookModal} /> */}
            {/* {isModalOpen && <BookModal books={selectedBooks} onClose={closeBookModal} />} */}
            {selectedBook && (
              <BookModal
                book={selectedBook}
                onClose={closeBookModal}
                isModalOpen={isModalOpen}
              />
            )}
            {/* {isModalOpen && <BookModal book={selectedBook} onClose={closeBookModal} />} */}
          </div>
        </Suspense>
        <div className="flex items-center justify-center ">
          <div className="w-[58.625rem] h-[15.25rem] bg-zenno-orange rounded-[1.5rem] flex justify-between relative top-[85px]">
            <div className="text-zenno-1white text-[1.875rem] not-italic font-bold leading-[2.0625rem] p-[4rem] mt-[-0.875rem] ">
              You remember <br />
              that book <br />
              right?
              <p className="text-[0.9375rem] font-bold not-italic leading-[1.03125rem] text-zenno-clear mt-space250">
                Explore with{' '}
                <span className="text-zenno-1white font-bold text-[1rem] leading-[1.03125rem]">
                  Zeeno
                </span>
                .
              </p>
            </div>

            <div className="right-details">
              <img src={zenno2} alt="book-image" />
            </div>
          </div>
        </div>

        <footer>
          <div className="w-auto h-[31.25rem] border-solid border-[2px] border-black mt-[12.25rem] flex bg-zenno-3black text-zenno-white p-[2rem]">
            <div className="relative w-[24.5624rem]">
              <img
                src={logo}
                alt=""
                className="absolute left-[6.3125rem] bottom-[5.27131rem]"
              />
              {/* osition: absolute; left: 2.3125rem; bottom: 10.27131rem width: 24.5624rem;*/}
            </div>
            <div className="flex gap-[11rem] pt-[3rem]">
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
                      <img src={facebook} alt="" />
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
                  <ul>
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
        {/* <div className="logo-z">
          <img src={zenno} alt="zenno-image"></img>
        </div> */}
      </div>
      {/* <div className='mobile-container'>
                <Navbar />
                {loading && <Loader loading={loading} />}
                <div className='text-header'>
                    Discover books that <br />
                    match your imagination.By simply
                    describing the kind of books you want.
                </div>
                <form className='search' action='#'>
                    <input
                        type="text"
                        id="searchInput"
                        name="searchText"
                        value={userInput}
                        onChange={handleInputChange}
                        placeholder='search for books based on your description'
                        onKeyDown={handleClickKeyPress}
                        className='input'
                    />
                    <button type="button" onClick={handleClick} > {loading ? 'Loading...' : 'Search book  '}
                    </button>


                </form>
                <Suspense fallback={<p>loading....</p>}>

                    <div className='main-container'>
                        {
                            data && data.books.map((book) => (
                                <div className='display-container' key={book.isbn10} >
                                    <div className='title'>
                                        <p> {book.title} </p>
                                    </div>
                                    <div className='thumbnail'>
                                        <img src={book.thumbnail} alt=''></img>
                                    </div>
                                    <div className='author'>  <p> {book.authors} </p></div>
                                    <button onClick={() => handleBookClick(book)}>View Details</button>
                                </div>

                            ))
                        }
                     
                        {selectedBook && <BookModal book={selectedBook} onClose={closeBookModal} isModalOpen={isModalOpen} />}
                       

                    </div>
                </Suspense>
                <div className='about'>
                    <p>Unleash the power of machine learning and semantic search with <b>zeno</b> .Find books
                        that match your unique interests and explore the limitless world of knowledge. </p>
                </div>
                <div className='mobile-details'>
                    <div className='mobile-top-details'>
                        You remember <br />
                        that book <br />
                        right?
                        <p>search with zeno.</p>
                    </div>

                    <img src={zenno3} alt="mobile-view" />


                </div>
            </div> */}
    </React.Fragment>
  );
};

export default Home;
