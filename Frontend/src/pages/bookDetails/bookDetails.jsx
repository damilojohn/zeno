import React from 'react'


const BookDetails = () => {
  const [bookDetails, setBookDetails] = useState(null)
  const { id } = useParams()
  console.log(id)
  // const fetchBook = async () => {
  //   try {
  //     const details = await axios.post(`https://hfex3k70e0.execute-api.us-east-1.amazonaws.com/prod/${isbn10}`, postData)
  //     setBookDetails(details.bookDetails)
  //   }
  //   catch (error) {
  //     console.log(error)
  //   }
  // }
  // useEffect(() => { fetchBook() }, [])
  return (
    <div className='container-details'>

    </div>

  )
}

export default BookDetails
