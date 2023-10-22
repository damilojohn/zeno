import React from 'react';
import '../modal/modal.css'

const BookModal = ({ book, onClose, isModalOpen }) => {
    console.log('Received Book:', book);
    console.log("isModalOpen: ", isModalOpen);
    if (!isModalOpen) return null;

    return (
        <div className={`modal ${isModalOpen ? 'active' : ''}`}>
            <div className="modal-content">
                <span className="close" onClick={onClose}>
                    &times;
                </span>
                <h2>{book.title}</h2>
                <p>Author(s): {book.authors}</p>
                <p>Category: {book.categories}</p>
                <p>Average Rating: {book.average_rating}</p>
                <p>Description: {book.description}</p>
                <p>Published Year: {book.published_year}</p>
                <img src={book.thumbnail} alt={book.title} />
            </div>
        </div>
    );
};

export default BookModal;
