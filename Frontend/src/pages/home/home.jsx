import Header from '../../component/molecule/header/header'
import React, { Suspense } from 'react'
import { useState, useEffect } from 'react'
import axios from 'axios'
import '../home/home.css'
import Loader from '../../loader/loader'
import { useHistory } from 'react-router-dom'

const Home = () => {
    const [userInput, setUserInput] = useState('')
    const [loading, setLoading] = useState(false)

    const [data, setData] = useState(null)
    // const history = useHistory()
    // const linkToNewPage = () => {
    //     history.push()

    // }
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
    return (
        <React.Fragment>
            <div className='container'>
                <Header />
                {/* <Preload loading={loading} /> */}
                {loading && <Loader loading={loading} />}

                <form className='search' action='#'>
                    <input
                        type="text"
                        value={userInput}
                        onChange={handleInputChange}
                        placeholder='enter a text describing what you feel '
                        className='input'
                    />
                    <button type="button" onClick={handleClick} > {loading ? 'Loading...' : 'Search'} </button>

                </form>
                {/* {loading ? <p>loading ...</p> : */}
                <Suspense fallback={<p>loading....</p>}>

                    <div className='main-container'>
                        {
                            data && data.books[0].map((item) => (
                                <div className='display-container' key={item.isbn10}>
                                    <div className='title'>
                                        <p> {item.title} </p>
                                    </div>
                                    <div className='thumbnail'>
                                        <img src={item.thumbnail} alt=''></img>
                                    </div>

                                    <div className='author'>  <p> {item.authors} </p></div>
                                </div>

                            ))
                        }

                    </div>
                </Suspense>
                {/* } */}
                <footer>
                    <div className='credit'>
                        <h2>Credits</h2>
                        <ul>
                            <li>
                                <a href="https://github.com/damilojohn" target="_blank" rel="noopener noreferrer" >Damilola John </a> - Machine Learning Engineer
                            </li>
                            <li>
                                <a href="https://github.com/mankinde23" target="_blank" rel="noopener noreferrer" >Makinde Damilola </a> - Software Developer
                            </li>
                        </ul>
                    </div>
                </footer>
            </div>
        </React.Fragment>
    )
}

export default Home
