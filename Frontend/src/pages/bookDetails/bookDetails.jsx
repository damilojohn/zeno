import React, { useState } from 'react'
import { useEffect } from 'react'
import axios from 'axios'
import { useParams } from 'react-router-dom'

const BookDetails = () => {
  const [bookDetails, setBookDetails] = useState(null)
  const { isbn10 } = useParams()
  console.log(isbn10)
  const fetchBook = async () => {
    try {
      const details = await axios.post(`https://hfex3k70e0.execute-api.us-east-1.amazonaws.com/prod/${isbn10}`, postData)
      setBookDetails(details.bookDetails)
    }
    catch (error) {
      console.log(error)
    }
  }
  useEffect(() => { fetchBook() }, [])
  return (
    <div className='container-details'>

    </div>
  )
}

export default BookDetails
