import React from 'react'
import { Home } from '../home/home'

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
      <Home />
      </div>

  )
}

export default BookDetails
