import React, {useEffect, useState} from 'react';
const words = [
  'Science',
  'Art',
  'Geography',
  'Medicine',
  'Biology',
  'Fiction',
  'Non-fiction',
  'History',
  'Romance',
  'Finance',
  'Horror',
  'Philosophy',
  'Business',
  'Sales',
];
const delay = 2000;
const gapWidth = 20;
const wordWidth = 200;

const Slideshow = () => {
  const [position, setPosition] = useState(0);

  useEffect(() => {
    const totalWidth = words.length * wordWidth + (words.length - 1) * gapWidth;
    const scrollSpeed = 200;
    const intervalId = setInterval(() => {
      setPosition(prevPosition =>
        prevPosition <= -totalWidth ? 0 : prevPosition - scrollSpeed
      );
    }, delay);

    return () => {
      clearInterval(intervalId);
    };
  }, [delay]);
  return (
    <div className="slideShow">
      <div className="slideshowSlider" style={{transform: `translateX(${position}px)`}}>
        {words.map((word, index) => (
          <div className="slide" key={index} style={{width: `${wordWidth}px`}}>
            {word}
          </div>
        ))}
        {words.map((word, index) => (
          <div
            className="slide"
            key={index + words.length}
            style={{width: `${wordWidth}px`}}
          >
            {word}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Slideshow;
// import React from 'react';
// import Slider from 'react-slick';
// import 'slick-carousel/slick/slick.css';
// import 'slick-carousel/slick/slick-theme.css';

// const words = [
//   'Science',
//   'Art',
//   'Geography',
//   'Medicine',
//   'Biology',
//   'Fiction',
//   'Non-fiction',
//   'History',
//   'Romance',
//   'Finance',
//   'Horror',
//   'Philosophy',
//   'Business',
//   'Sales',
// ];
// const delay = 2000;

// const sliderSettings = {
//   autoplay: true,
//   autoplaySpeed: delay,
//   speed: 200,
//   slidesToShow: 1,
//   slidesToScroll: 1,
//   infinite: true,
//   pauseOnHover: true,
// };

// const Slideshow = () => {
//   return (
//     <Slider {...sliderSettings}>
//       {words.map((word, index) => (
//         <div className="slide" key={index}>
//           {word}
//         </div>
//       ))}
//       {words.map((word, index) => (
//         <div className="slide" key={index + words.length}>
//           {word}
//         </div>
//       ))}
//     </Slider>
//   );
// };

// export default Slideshow;
