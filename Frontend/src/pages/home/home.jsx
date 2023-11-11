import Header from '../../component/organism/header/header.jsx'
import React, { Suspense } from 'react'
import { useState, useEffect } from 'react'
import axios from 'axios'
import '../home/home.css'
import Loader from '../../loader/loader'
import BookModal from '../../modal/modal'
import Navbar from '../../component/molecule/navbar/navbar'

const Home = () => {
    const [userInput, setUserInput] = useState('')
    const [loading, setLoading] = useState(false)

    const [data, setData] = useState(null)
    const [selectedBook, setSelectedBook] = useState(null)
    const [isModalOpen, setIsModalOpen] = useState(false)
    const handleInputChange = (e) => {
        e.preventDefault()
        setUserInput(e.target.value);
    };

    const fetchData = async () => {
        setLoading(true)
        try {
            const postData = {
                query: userInput
            };
            const resp = await axios.post('https://hfex3k70e0.execute-api.us-east-1.amazonaws.com/prod', postData)
            setLoading(false)

            setData(resp.data)
            console.log(resp.data)
        }
        catch (error) {
            setLoading(false)

            console.log(error)
        }

    }
    const handleClick = (e) => {
        e.preventDefault();
        fetchData()
    }
    const handleClickKeyPress = (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            fetchData()

        }
    }
    // const handleBookClick = (books) => {
    //     setSelectedBooks(books);
    //     setIsModalOpen(true);
    // };
    // const closeBookModal = () => {
    //     // setSelectedBooks(null);
    //     setIsModalOpen(false);
    // };
    const handleBookClick = (book) => {
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
            <div className='container'>
                <Navbar />
                {/* <Preload loading={loading} /> */}
                {loading && <Loader loading={loading} />}
                <Header />
                <div className='about'>
                    <div className='left-about'>
                        <p>Zenno allows you to find books based on description provided by you.Using machine learning and sematic search, you could think of the process as talking to a liberian.</p>

                    </div>
                    <div className='right-about'>
                        <p>Named after zenolotus,the first libarian of the library of Alenardines.</p>
                    </div>
                </div>

                <form className='search' action='#'>
                    <input
                        type="text"
                        id="searchInput"
                        name="searchText"
                        value={userInput}
                        onChange={handleInputChange}
                        placeholder='For example:Book about roman emperrors and their romantic interest '
                        onKeyDown={handleClickKeyPress}
                        className='input'
                    />
                    <button type="button" onClick={handleClick} > {loading ? 'Loading...' : 'Search'} </button>

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
                        {/* <BookModal books={selectedBooks} onClose={closeBookModal} /> */}
                        {/* {isModalOpen && <BookModal books={selectedBooks} onClose={closeBookModal} />} */}
                        {selectedBook && <BookModal book={selectedBook} onClose={closeBookModal} isModalOpen={isModalOpen} />}
                        {/* {isModalOpen && <BookModal book={selectedBook} onClose={closeBookModal} />} */}



                    </div>
                </Suspense>
                <footer>
                    <div className='credit'>
                        <h2>Credits</h2>
                        <ul>
                            <li>
                                <a href="https://github.com/damilojohn" target="_blank" rel="noopener noreferrer" >Damilola John </a> - Machine Learning Engineer
                            </li>
                            <li>
                                <a href="https://github.com/mankinde23" target="_blank" rel="noopener noreferrer" >Makinde Damilola </a> - Frontend Engineer
                            </li>
                        </ul>
                    </div>
                </footer>
            </div>
        </React.Fragment>
    )
}

export default Home
