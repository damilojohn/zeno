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
import searchIcon from '../../assets/Search book.svg';
import Slideshow from '../../component/slider/slider.jsx';
import Footer from '../../component/molecule/footer/footer.jsx';
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
// import { faSearch } from '@fortawesome/free-solid-svg-icons';
import {motion} from 'framer-motion';

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
      <motion.div
        initial={{opacity: 0, y: -50}}
        animate={{opacity: 1, y: 0}}
        transition={{duration: 3}}
        className="md:hidden sm:hidden lg:hidden xl:block"
      >
        <Navbar />
        {/* <Preload loading={loading} /> */}
        {loading && <Loader loading={loading} />}
        <Header />
        {/* <div className='text-header'>
                    Discover books that <br />
                    match your imagination.
                </div> */}
        <div className="form-main" id="top">
          <form className="form-container" action="#">
            <input
              type="text"
              id="searchInput"
              name="searchText"
              value={userInput}
              onChange={handleInputChange}
              placeholder="search for books based on your description"
              onKeyDown={handleClickKeyPress}
              className="w-[42.3125rem] outline-none h-[3rem] "
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
        <div className="flex items-center justify-center text-[1.125rem] text-center not-italic font-bold leading-[1.68705rem] text-zenno-2black mr-[13rem] ml-[13rem] mt-[4.18rem]">
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
          <div className="grid grid-cols-3 auto-rows-auto gap-x-[3.2rem] gap-y-[3.3rem] mx-[3rem] my-[4rem] justify-items-center sm:block">
            {data &&
              data.books.map(book => (
                <div
                  className="shadow-lg bg-zenno-1white w-[22.25rem] h-[29.5625rem] grid justify-center items-baseline col-span-1 last:col-span-3"
                  key={book.isbn10}
                >
                  <div className="text-[1rem] font-bold leading-[1.5rem] text-center w-[10rem]">
                    <p> {book.title} </p>
                  </div>
                  <div className="thumbnail">
                    <img src={book.thumbnail} alt="Description of the image" className="mx-auto my-auto"></img>
                  </div>
                  <div className="text-[0.9375rem] font-semibold text-zenno-3black leading-[1.40625rem] text-center w-[10rem]">
                    {' '}
                    <p> {book.authors} </p>
                  </div>
                  <button
                    onClick={() => handleBookClick(book)}
                    className="w-[10.375rem] pt-[1.625rem] pb-[1.6875rem] pr-[1.75rem] pl-[1.75rem] bg-zenno-orange rounded-[0.3125rem] h-[2.875rem] flex justify-center items-center text-zenno-1white text-[1.125rem] font-normal leading-[1.69rem]"
                  >
                    View Details
                  </button>
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
        <Slideshow />
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

        <Footer />
      </motion.div>
      {/*      ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// */}

      <div className="2xl:hidden sm:block md:block sm:w-full lg:block">
        <Navbar />

        {loading && <Loader loading={loading} />}
        <Header />

        <div className="flex justify-center items-center mt-[3.18rem]">
          <form
            className="flex justify-center items-center w-[21.625rem] relative rounded-[1.25rem] bg-zenno-mwhite h-4 border-2 border-solid border-zenno-3black shadow-custom"
            action="#"
          >
            <input
              type="text"
              id="searchInput"
              name="searchText"
              value={userInput}
              onChange={handleInputChange}
              placeholder="search for books based on your description"
              onKeyDown={handleClickKeyPress}
              className="w-[19.125rem] pt-[1.06rem] pb-[1.25rem] pr-[0.94rem] outline-none h-[0.4375rem] font-bold leading-[0.6445rem] text-[0.6rem] sm:w-[18.125rem]"
            />
            <button
              type="button"
              onClick={handleClick}
              className="absolute right-[11px] top-[4px] bg-zenno-orange pt-[1rem] pb-[1.06rem] justify-center w-[7.5rem] flex items-center rounded-r-[1.375rem] h-[2.3rem] mt-[-4px] mr-[-11px]"
            >
              <div className="text-zenno-white flex item-center justify-center gap-[0.5rem] text-[1.25rem] font-bold not-italic leading-[1.65rem] tracking-[-0.0025rem]">
                {' '}
                {/* padding: 0.875rem 1.75rem 0.8125rem 1.25rem; */}
                <div className="h-[1.1875rem] flex items-center justify-center gap-[0.5rem]  pt-[0.88rem] pb-[0.81rem] pl-[1.25rem] pr-[1.75rem]">
                  {' '}
                  {loading ? 'Loading...' : <img src={searchIcon} />}
                  <img src={icon} alt="" />
                </div>
              </div>
            </button>
          </form>
        </div>
        <div className="flex items-center justify-center text-[0.8125rem] text-center not-italic font-bold leading-[1.21388rem] text-zenno-2black mr-[1.94rem] ml-[1.94rem] mt-[3.18rem]">
          <p>
            Unleash the power of machine learning and semantic search with{' '}
            <b className="italic font-normal">Zeeno</b>.Find books that match your unique
            interests and explore the limitless word of book recommendations
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
          <div className="grid grid-cols-3 auto-rows-auto gap-x-[3.2rem] gap-y-[3.3rem] mx-[2rem] my-[1rem] justify-items-center sm:block lg:flex lg:justify-center lg:items-center lg:flex-col">
            {data &&
              data.books.map(book => (
                <div
                  className="shadow-lg bg-zenno-1white w-[22.25rem] h-[29.5625rem] grid justify-center items-baseline col-span-1 last:col-span-3 mt-[4.38rem] md:w-full"
                  key={book.isbn10}
                >
                  <div className="text-[1rem] font-bold leading-[1.5rem] text-center w-[10rem]">
                    <p> {book.title} </p>
                  </div>
                  <div className="thumbnail">
                    <img src={book.thumbnail} alt="" className="mx-auto my-auto"></img>
                  </div>
                  <div className="text-[0.9375rem] font-semibold text-zenno-3black leading-[1.40625rem] text-center w-[10rem]">
                    {' '}
                    <p> {book.authors} </p>
                  </div>
                  <button
                    onClick={() => handleBookClick(book)}
                    className="w-[10.375rem] pt-[1.625rem] pb-[1.6875rem] pr-[1.75rem] pl-[1.75rem] bg-zenno-orange rounded-[0.3125rem] h-[2.875rem] flex justify-center items-center text-zenno-1white text-[1.125rem] font-normal leading-[1.69rem]"
                  >
                    View Details
                  </button>
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
        <Slideshow />
        <div className="flex items-center justify-center mt-[3.18rem]">
          <div className="w-[20.3125rem] h-[34.9375rem] bg-zenno-orange rounded-[1.5rem]">
            <div className="text-zenno-1white text-[1.5rem] not-italic font-bold leading-[1.65rem] mt-[2.68rem] mr-[4.31rem] ml-[4.31rem] w-[11.6875rem]">
              <p className="text-center">
                You remember <br /> that book <br /> right?
              </p>

              <p className="text-[0.9375rem] font-bold not-italic leading-[1.03125rem] text-zenno-clear mt-space250 flex justify-center">
                Explore with{' '}
                <span className="text-zenno-1white font-bold text-[1rem] leading-[1.03125rem]">
                  Zeeno
                </span>
                .
              </p>
            </div>

            <div className="relative">
              <img src={zenno3} alt="book-image" className="absolute top-[4.9rem]" />
            </div>
          </div>
        </div>

        <Footer />
      </div>
    </React.Fragment>
  );
};

export default Home;
