// import React from 'react'


// const BookDetails = () => {
//   const [bookDetails, setBookDetails] = useState(null)
//   const { id } = useParams()
//   console.log(id)
//   // const fetchBook = async () => {
//   //   try {
//   //     const details = await axios.post(`https://hfex3k70e0.execute-api.us-east-1.amazonaws.com/prod/${isbn10}`, postData)
//   //     setBookDetails(details.bookDetails)
//   //   }
//   //   catch (error) {
//   //     console.log(error)
//   //   }
//   // }
//   // useEffect(() => { fetchBook() }, [])
//   return (
//     <div className='container-details'>

//     </div>

//   )
// }

// export default BookDetails
// BookDetails.jsx
// import React from 'react';
// import { useParams, useLocation } from 'react-router-dom';

// const BookDetails = ({ data }) => {
//   const { bookIndex } = useParams();
//   const selectedBook = data.books[bookIndex];

//   return (
//     <div>
//       <h2>{selectedBook.title}</h2>
//       <p>{selectedBook.authors}</p>
//       {/* Add other book details here */}
//     </div>
//   );
// };

// export default BookDetails;

// import React from 'react';
// import { useParams } from 'react-router-dom';

// const BookDetails = ({ data }) => {
//   const { index } = useParams();
//   console.log(index)

//   // Convert the index to a number if needed
//   const bookIndex = parseInt(index, 10);

//   // Check if data is available and if the index is valid
//   if (isNaN(bookIndex) || bookIndex < 1 || bookIndex >= data.books.length) {
//     return <div>Invalid book index or data not available</div>;
//   }

//   const selectedBook = data.books[bookIndex - 1];

//   return (
//     <div>
//       <h2>{selectedBook.title}</h2>
//       <p>{selectedBook.authors}</p>
//       {/* Add other book details here */}
//     </div>
//   );
// };

// export default BookDetails;

// import React from 'react';
// import { useParams } from 'react-router-dom';
// const BookDetails = ({ data }) => {
//   const { index } = useParams();
//   const bookIndex = parseInt(index, 10);

//   if (!data || !data.books || isNaN(bookIndex) || bookIndex < 0 || bookIndex >= data.books.length) {
//     return <div>Invalid book index or data not available.</div>;
//   }

//   const selectedBook = data.books[bookIndex];

//   if (!selectedBook || !selectedBook.title) {
//     return <div>Book details not available.</div>;
//   }

//   return (
//     <div>
//       <h2>{selectedBook.title}</h2>
//       <p>{selectedBook.authors}</p>
//       {/* Add other book details here */}
//     </div>
//   );
// };

// export default BookDetails;
// import React from 'react';
// import { useParams } from 'react-router-dom';

// const BookDetails = ({ data }) => {
//   const { index } = useParams();
//   const bookIndex = parseInt(index, 10);

//   // if (!data || !data.books || isNaN(bookIndex) || bookIndex < 0 || bookIndex >= data.books.length) {
//   //   return <div>Invalid book index or data not available.</div>;
//   // }

//   const selectedBook = data.books[bookIndex];

//   return (
//     <div>
//       <h2>{selectedBook.title}</h2>
//       <p>Authors: {selectedBook.authors}</p>
//       <p>Categories: {selectedBook.categories}</p>
//       <p>Average Rating: {selectedBook.average_rating}</p>
//       <p>Description: {selectedBook.description}</p>
//       <p>Published Year: {selectedBook.published_year}</p>
//       <img src={selectedBook.thumbnail} alt={selectedBook.title} />
//       {/* You can display other book details here */}
//     </div>
//   );
// };

// export default BookDetails;
import React from 'react';
import { useParams } from 'react-router-dom';

const BookDetails = ({ data }) => {
  const { index } = useParams();
  const bookIndex = parseInt(index, 10);
  console.log('Data:', data);
  console.log('Index:', index);

  if (!data || !data.books || isNaN(bookIndex) || bookIndex < 0 || bookIndex >= data.books.length) {
    console.log('Invalid data or index');
    return <div>Invalid book index or data not available.</div>;
  }

  const selectedBook = data.books[bookIndex];

  return (
    <div>
      <h2>{selectedBook.title}</h2>
      <p>Authors: {selectedBook.authors}</p>
      <p>Categories: {selectedBook.categories}</p>
      <p>Average Rating: {selectedBook.average_rating}</p>
      <p>Description: {selectedBook.description}</p>
      <p>Published Year: {selectedBook.published_year}</p>
      <img src={selectedBook.thumbnail} alt={selectedBook.title} />
    </div>
  );
};

export default BookDetails;

