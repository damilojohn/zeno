// import React, { useState } from 'react'
// import { useEffect } from 'react'
// import axios from 'axios'
// import { useParams } from 'react-router-dom'

// const BookDetails = () => {
//   // const [bookDetails, setBookDetails] = useState(null)
//   const { isbn10 } = useParams()
//   console.log(isbn10)
//   // const fetchBook = async () => {
//   //   try {
//   //     const response = await axios.get(`https://hfex3k70e0.execute-api.us-east-1.amazonaws.com/prod/${isbn10}`, {
//   //       headers: {
//   //         'Authorization': 'APPID',
//   //       }
//   //     })
//   //     // setBookDetails(details.bookDetails)
//   //     // console.log(bookDetails)
//   //     setBookDetails(response.data)
//   //     console.log(response.data)
//   //   }
//   //   catch (error) {
//   //     console.log(error)
//   //   }
//   // }
//   // useEffect(() => { fetchBook() }, [isbn10])
//   return (
//     <div className='container-details'>
//       {/* {bookDetails ?
//         <div className='display-container'>
//           <div className='title'>
//             <p> {bookDetails.title} </p>
//           </div>
//           <div className='thumbnail'>
//             <img src={bookDetails.thumbnail} alt='' />
//           </div>
//           <div className='author'>
//             <p> {bookDetails.authors} </p>
//           </div>
//         </div>
//         : null} */}
//       <div className='display-container' key={item.isbn10} >
//         <div className='title'>
//           <p> {item.title} </p>
//         </div>
//         <div className='thumbnail'>
//           <img src={item.thumbnail} alt=''></img>
//         </div>

//         <div className='author'>  <p> {item.authors} </p></div>

//       </div>


//       <Link to="/">Back to Search</Link>
//     </div>


//   )
// }

// export default BookDetails




// import React, { useState, useEffect } from 'react';
// import axios from 'axios';
// import { useParams } from 'react-router-dom';
// import { useDataContext } from '../../datacontext';

// const BookDetails = () => {
//   // const [bookDetails, setBookDetails] = useState(null);
//   // const { isbn10 } = useParams();

//   const { state } = useDataContext();
//   const { bookDetails } = state;

//   // useEffect(() => {
//   //   const fetchBook = async () => {
//   //     try {
//   //       const response = await axios.post(
//   //         'https://hfex3k70e0.execute-api.us-east-1.amazonaws.com/prod/book-details',
//   //         { isbn: isbn10 },
//   //         {
//   //           headers: {
//   //             'Authorization': 'APPID',
//   //           },
//   //         }
//   //       );

//   //       setBookDetails(response.data);
//   //     } catch (error) {
//   //       console.log(error);
//   //     }
//   //   };

//   //   fetchBook();
//   // }, [isbn10]);

//   return (
//     <div className='container-details'>
//       {bookDetails ? (
//         <div className='display-container' key={bookDetails.isbn10}>
//           <div className='title'>
//             <p>{bookDetails.title}</p>
//           </div>
//           <div className='thumbnail'>
//             <img src={bookDetails.thumbnail} alt='' />
//           </div>
//           <div className='author'>
//             <p>{bookDetails.authors}</p>
//           </div>
//         </div>
//       ) : (
//         <p>Loading...</p>
//       )}
//     </div>
//   );
// };

// export default BookDetails;


// import React, { useEffect, useState } from 'react';
// import axios from 'axios';
// import { useParams } from 'react-router-dom';

// const BookDetails = () => {
//   const { isbn10 } = useParams();
//   const [bookDetails, setBookDetails] = useState(null);

//   useEffect(() => {
//     const fetchBookDetails = async () => {
//       try {
//         const postData = {
//           query: bookDetails
//         };
//         const response = await axios.post(
//           `https://hfex3k70e0.execute-api.us-east-1.amazonaws.com/prod/${isbn10}`,
//           // { isbn: isbn }
//           postData
//         );
//         setBookDetails(response.data);
//       } catch (error) {
//         console.error('Error fetching book details:', error);
//       }
//     };

//     fetchBookDetails();
//   }, [isbn10]);

//   return (
//     <div className="container">
//       {bookDetails ? (
//         <div className="book-details">
//           <h2>{bookDetails.title}</h2>
//           <div className="author">Author: {bookDetails.author}</div>
//           <div className="description">{bookDetails.description}</div>
//           {/* Add more book details here */}
//         </div>
//       ) : (
//         <p>Loading...</p>
//       )}
//     </div>
//   );
// };

// export default BookDetails;

