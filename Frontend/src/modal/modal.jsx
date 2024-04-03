import React from 'react';
import '../modal/modal.css';
import Book from '../assets/Isometric Stickers - Books 1.png';

const BookModal = ({book, onClose, isModalOpen}) => {
  console.log('Received Book:', book);
  console.log('isModalOpen: ', isModalOpen);
  if (!isModalOpen) return null;

  return (
    <div className={`modal ${isModalOpen ? 'active' : ''}`}>
      <div className="modal-content md:w-[23.3125rem] lg:w-[23.3125rem] xl:w-[57.3125rem]">
        <span className="close" onClick={onClose}>
          &times;
        </span>
        <h2 className="flex text-zenno-4black text-[2.687rem] font-bold leading-[4.031rem] text-justify justify-center items-center">
          {book.title}
        </h2>
        <p className="text-justify text-[1.5rem] font-normal leading-[2.25rem] text-zenno-3black mb-[4.38rem]">
          Author(s): {book.authors}
        </p>
        <p className="text-justify text-[1.5rem] font-normal leading-[2.25rem] text-zenno-3black mb-[4.38rem]">
          Category: {book.categories}
        </p>
        <p className="text-justify text-[1.5rem] font-normal leading-[2.25rem] text-zenno-3black mb-[4.38rem]">
          Average Rating: {book.average_rating}
        </p>
        <p className="text-justify text-[1.5rem] font-normal leading-[2.25rem] text-zenno-3black mb-[4.38rem]">
          Description: {book.description}
        </p>
        <p className="text-justify text-[1.5rem] font-normal leading-[2.25rem] text-zenno-3black mb-[4.38rem]">
          Published Year: {book.published_year}
        </p>
        <div className="flex justify-center items-center">
          <img
            src={book.thumbnail}
            alt={book.title}
            className="w-[18.75rem] h-[29.72rem]"
          />
        </div>
        {/* <div className="book">
          <img src={Book} alt="" className='image' />
        </div> */}
      </div>
    </div>
  );
};

export default BookModal;
