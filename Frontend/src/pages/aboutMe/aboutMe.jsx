import Navbar from '../../component/molecule/navbar/navbar';
import React from 'react';
import library from '../../assets/library.png';
import book from '../../assets/book.png';
import rock from '../../assets/rock.png';
import background from '../../assets/Group 175.png';
import mobilebg from '../../assets/Group 1756.png';
import Footer from '../../component/molecule/footer/footer';
import {Link} from 'react-router-dom';
import {motion} from 'framer-motion';

const About = () => {
  // const history = useHistory();
  // const handleClick = () => {
  //   history.push('/');
  //   window.scrollTo(0, 0);
  // };

  return (
    <>
      <motion.div
        initial={{opacity: 0, y: -50}}
        animate={{opacity: 1, y: 0}}
        transition={{duration: 2}}
        className="md:hidden sm:hidden lg:hidden xl:block 2xl:block 2xl-max:block"
      >
        <Navbar />
        <div className="h-[27.5rem] flex justify-center flex-col items-center px-[23.94rem] py-[4.69rem] bg-zenno-aboutw gap-[0.625rem]">
          <div className="flex flex-col items-center gap-[2.75rem]">
            <h1 className="text-[2.25rem] font-bold leading-[3.36rem] text-zenno-aboutb pt-[4.69rem]">
              About Us
            </h1>
            <div className="h-[21rem]">
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-justify w-[31.125rem]">
                Zeeno, named after the first librarian of the library of Alexandria,
                Zenodotus of Ephesus, Zeno is a book recommendation service that gives
                users the ability to take direct control of their journey in exploring the
                amazing world of books. Using machine learning and semantic search.{' '}
              </p>{' '}
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-justify w-[31.125rem] mt-[2rem]">
                Zeno helps you find books about descriptions provided by you, with Zeno,
                the limits of your search knowledge are only bounded by your imagination.
              </p>
            </div>
          </div>
        </div>
        {/* ////////////////////// ///////*/}
        <div className="h-[23.56rem] gap-[5.625rem] flex items-center justify-center px-[5.06rem] mt-[4.5rem]">
          <div className="h-[21rem] gap-[2.75rem] flex justify-center flex-col items-center">
            {' '}
            <h1 className="text-[2.25rem] font-bold leading-[3.36rem] text-zenno-aboutb">
              Our Story
            </h1>
            <div>
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-justify w-[31.125rem]">
                It all started with a group of bookworms who wanted to create a place for
                where fellow readers could find their next literary obsession. We wanted
                to make book recommendations personal and exciting, so we developed
                cutting-edge technology that analyzes your preference and suggests books
                tailored just for you.{' '}
              </p>{' '}
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-justify w-[31.125rem] mt-[2rem]">
                Our vibrant community of book lovers adds an extra layer of magic to
                Zeeno. Together, we’re on a mission to bring the joy of reading to
                everyone and create a world where books come to life. Join us in this
                incredible journey and let’s dive into a world of captivating stories.
              </p>
            </div>
          </div>
          <div>
            <img src={library} alt="" />{' '}
          </div>
        </div>
        {/* ////////////////////// ///////*/}
        <div className="h-[23.56rem] gap-[5.625rem] flex items-center justify-center px-[5.06rem] mt-[6.8rem]">
          <div>
            <img src={book} alt="" />{' '}
          </div>
          <div className="h-[21rem] gap-[2.75rem] flex justify-center flex-col items-center">
            {' '}
            <h1 className="text-[2.25rem] font-bold leading-[3.36rem] text-zenno-aboutb">
              Our Vision
            </h1>
            <div>
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-justify w-[31.125rem]">
                Our vision is to ignite a love for reading in every individual. We believe
                that books have the power to transport us to new worlds, inspire our
                imagination and broaden our perspectives.{' '}
              </p>{' '}
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-justify w-[31.125rem] mt-[2rem]">
                Our goal is to create a platform where book lovers can discover their next
                adventure with ease. Through personalized recommendations and a vibrant
                community, we aim to foster a deep connection between readers and books.
              </p>
            </div>
          </div>
        </div>
        {/* ////////////////////// ///////*/}
        <div className="h-[23.56rem] gap-[5.625rem] flex items-center justify-center px-[5.06rem] mt-[6.8rem]">
          <div className="h-[21rem] gap-[2.75rem] flex justify-center flex-col items-center">
            {' '}
            <h1 className="text-[2.25rem] font-bold leading-[3.36rem] text-zenno-aboutb">
              Our Mission
            </h1>
            <div>
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-justify w-[31.125rem]">
                Our mission is to make book recommendations a delightful adventure for
                book lovers like you! W e believe everyone deserves to discover the
                perfect book that sparks their imagination and leaves them wanting more.{' '}
              </p>{' '}
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-justify w-[31.125rem] mt-[2rem]">
                Our dedicated team works tirelessly to curate a diverse collection of
                books and use innovative technology to match them with your unique taste
                and interests. We’re here to empower you tto explore new genres, discover
                hidden gems and connect with fellow readers who share your passion.
              </p>
            </div>
          </div>
          <div>
            <img src={rock} alt="" />{' '}
          </div>
        </div>
        {/* ////////////////////// ///////*/}
        <div className="h-[23.56rem] gap-[5.625rem] flex items-center justify-center px-[5.06rem] mt-[6.8rem]">
          <div>
            <img src={book} alt="" />{' '}
          </div>
          <div className="h-[21rem] gap-[2.75rem] flex justify-center flex-col items-center">
            {' '}
            <h1 className="text-[2.25rem] font-bold leading-[3.36rem] text-zenno-aboutb">
              Our Process
            </h1>
            <div>
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-justify w-[31.125rem]">
                We believe in putting you in the driver’s seat when it comes to exploring
                the incredible world of books. With our cutting edge machine learning and
                semantic search technology, we analyze your reading preference, interests
                and even your mood to provide personalized book recommendations.{' '}
              </p>{' '}
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-justify w-[31.125rem] mt-[2rem]">
                You have the ability to take direct control of your journey, discovering
                new genres, authors and hidden gems that truly resonate with you. It’s all
                about giving you the power to curate your own reading adventure.
              </p>
            </div>
          </div>
        </div>
        {/* ////////////////////// ///////*/}
        <div className="flex justify-center items-center">
          <h1 className="text-[2.25rem] font-bold leading-[3.36rem] text-zenno-aboutb mt-[6.94rem]">
            Meet Our Team
          </h1>
        </div>
        <div className="grid grid-cols-2 auto-rows-auto justify-items-center gap-x-[1.25rem] gap-y-[3.3rem] mt-[6.94rem] p-[1rem]">
          <div className="h-[11.43rem] flex flex-col items-center gap-[0.75rem]">
            <h1 className="text-zenno-aboutb3 text-[1.75rem] leading-[2.625rem] font-bold text-justify">
              Damilola Oduguwa{' '}
            </h1>
            <p className="text-zenno-4black text-[1.43rem] leading-[2.156rem] font-semibold text-justify">
              Machine Learning Engineer
            </p>
            <h3 className="text-zenno-aboutb3 text-[1.43rem] leading-[2.156rem] font-normal text-justify">
              Portfolio link:
            </h3>
            <a
              href="http://damilojohn.github.io/"
              target="_blank"
              rel="noopener noreferrer"
              className="text-zenno-aboutl"
            >
              http://damilojohn.github.io/
            </a>
          </div>
          <div className="h-[11.43rem] flex flex-col items-center gap-[0.75rem]">
            <h1 className="text-zenno-aboutb3 text-[1.75rem] leading-[2.625rem] font-bold text-justify">
              Daud Abolade{' '}
            </h1>
            <p className="text-zenno-4black text-[1.43rem] leading-[2.156rem] font-semibold text-justify">
              NLP Dataset Collector
            </p>
            <h3 className="text-zenno-aboutb3 text-[1.43rem] leading-[2.156rem] font-normal text-justify">
              Portfolio link:
            </h3>
            <a
              href="https://www.linkedin.com/in/daud-abolade-9b20781b6"
              target="_blank"
              rel="noopener noreferrer"
              className="text-zenno-aboutl"
            >
              https://www.linkedin.com/in/daud-abolade-9b20781b6
            </a>
          </div>
          <div className="h-[11.43rem] flex flex-col items-center gap-[0.75rem]">
            <h1 className="text-zenno-aboutb3 text-[1.75rem] leading-[2.625rem] font-bold text-justify">
              Oluwasegun Adebowale{' '}
            </h1>
            <p className="text-zenno-4black text-[1.43rem] leading-[2.156rem] font-semibold text-justify">
              UI/UX Designer
            </p>
            <h3 className="text-zenno-aboutb3 text-[1.43rem] leading-[2.156rem] font-normal text-justify">
              Portfolio link:
            </h3>
            <a
              href="https://linktr.ee/oluwasegun_"
              target="_blank"
              rel="noopener noreferrer"
              className="text-zenno-aboutl"
            >
              https://linktr.ee/oluwasegun_
            </a>
          </div>
          <div className="h-[11.43rem] flex flex-col items-center gap-[0.75rem]">
            <h1 className="text-zenno-aboutb3 text-[1.75rem] leading-[2.625rem] font-bold text-justify">
              Damilola Makinde{' '}
            </h1>
            <p className="text-zenno-4black text-[1.43rem] leading-[2.156rem] font-semibold text-justify">
              Software Developer
            </p>
            <h3 className="text-zenno-aboutb3 text-[1.43rem] leading-[2.156rem] font-normal text-justify">
              Portfolio link:
            </h3>
            <a
              href="https://github.com/mankinde23"
              target="_blank"
              rel="noopener noreferrer"
              className="text-zenno-aboutl"
            >
              https://github.com/mankinde23
            </a>
          </div>
        </div>
        {/* ////////////////////// ///////*/}
        <div className="h-[46.187rem] flex justify-center items-center">
          <img src={background} alt="" className="top-0 left-0 object-cover absolute" />
          <div className="absolute top-0 left-0 h-[46.187rem] w-[49.625rem]" />
          <div className="absolute top-0 flex flex-col justify-center items-center">
            <div className="h-[622px]">
              {' '}
              <h1 className="text-zenno-1white text-[2.25rem] text-center font-normal">
                What can you find on Zeeno?
              </h1>
              <p className="w-[30.43rem] h-[24.43rem] text-[1.25rem] font-medium text-justify mt-[2rem] text-zenno-1white">
                Zeeno is the ultimate destination for book enthusiasts seeking their next
                literary adventure. With curated search ideas, diverse genres and
                captivating stories, it’s a one-stop for all your book recommendation
                needs. Zeeno is your gateway to a world of immerse reading experiences,
                creating a sophisticated and comprehensive book recommendation website
                that caters to the diverse taste of readers. Aims to connect readers with
                their next great book, and our goal is to create a platform that inspires,
                engages and enriches the reading journey of every user.
              </p>
              <div className="flex justify-center mt-[3rem]">
                {' '}
                <button className="bg-zenno-1white rounded-[0.625rem] flex justify-center w-[20.125rem] h-[3.8125rem] px-[2.125rem] py-[1.125rem]">
                  {' '}
                  <p className="text-zenno-black text-[1.1rem] font-normal">
                    <Link to="/#top"> Start researching with Zeeno</Link>
                  </p>
                </button>
              </div>
            </div>
          </div>
        </div>
        {/* ////////////////////// ///////*/}
        <div className="flex justify-center items-center">
          <div className="flex flex-col items-center gap-[4.125rem] w-[44.62rem] h-[16.06rem] mb-[8.5rem]">
            <div className="flex justify-center mt-[6rem]">
              <h1 className="text-zenno-aboutb4 text-[2.25rem] font-bold leading-[3.36rem]">
                Why Use Zeeno?
              </h1>
            </div>
            <div className="w-[43.62rem]">
              {' '}
              <p className="text-zenno-black text-[1.25rem] font-medium leading-[1.87rem]">
                We make accessing research simple. Our powerful online library features
                millions of{' '}
                <span className="text-zenno-black text-[1.25rem] font-bold leading-[1.87rem]">
                  articles, journals, e-books
                </span>{' '}
                and more, all on a seamless platform.
              </p>{' '}
              <p className="text-zenno-black text-[1.25rem] font-medium leading-[1.87rem] mt-[2rem]">
                You can use comprehensive search ideas to narrow down your research and
                and content with ease.
              </p>
            </div>
          </div>
        </div>
        {/* ////////////////////// ///////*/}
        <Footer />
      </motion.div>

      {/* MOBILE */}
      {/* //////////////////////////////////////// */}
      <div className="2xl:hidden sm:block md:block sm:w-full lg:block 2xl-max:hidden">
        <Navbar />

        <div className="h-auto flex justify-center flex-col items-center mx-[1.5rem] mb-[8rem] bg-zenno-aboutw gap-[0.625rem]">
          <div className="flex flex-col items-center gap-[2.75rem]">
            <h1 className="text-[1.25rem] font-bold leading-[3.36rem] text-zenno-aboutb pt-[4.69rem]">
              About Us
            </h1>
            <div className="h-[17.25rem] w-auto">
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-center">
                Zeeno, named after the first librarian of the library of Alexandria,
                Zenodotus of Ephesus, Zeno is a book recommendation service that gives
                users the ability to take direct control of their journey in exploring the
                amazing world of books. Using machine learning and semantic search.{' '}
              </p>{' '}
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-center mt-[2rem]">
                Zeno helps you find books about descriptions provided by you, with Zeno,
                the limits of your search knowledge are only bounded by your imagination.
              </p>
            </div>
          </div>
        </div>
        {/* ////////////////////// ///////*/}
        <div className="h-[40.1rem] items-center justify-center mx-[4.5rem] lg:h-[48.1rem]">
          <div className="h-[21rem] gap-[2.75rem] flex justify-center flex-col items-center ">
            {' '}
            <h1 className="text-[1.25rem] font-bold leading-[3.36rem] text-zenno-aboutb">
              Our Story
            </h1>
            <div className="h-[23rem] w-auto">
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-center ">
                It all started with a group of bookworms who wanted to create a place for
                where fellow readers could find their next literary obsession. We wanted
                to make book recommendations personal and exciting, so we developed
                cutting-edge technology that analyzes your preference and suggests books
                tailored just for you.{' '}
              </p>{' '}
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-center mt-[2rem]">
                Our vibrant community of book lovers adds an extra layer of magic to
                Zeeno. Together, we’re on a mission to bring the joy of reading to
                everyone and create a world where books come to life. Join us in this
                incredible journey and let’s dive into a world of captivating stories.
              </p>
              <div className="mt-[2.75rem] lg:flex lg:justify-center w-auto">
                <img src={library} alt="" className="w-auto" />{' '}
              </div>
            </div>
          </div>
        </div>
        {/* ////////////////////// ///////*/}
        <div className="h-[40.1rem] items-center justify-center mx-[4.5rem] lg:h-[48.1rem] mt-[7rem]">
          <div className="h-auto gap-[2.75rem] flex justify-center flex-col items-center">
            {' '}
            <h1 className="text-[1.25rem] font-bold leading-[3.36rem] text-zenno-aboutb">
              Our Vision
            </h1>
            <div className="h-[23rem] w-auto">
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-center ">
                Our vision is to ignite a love for reading in every individual. We believe
                that books have the power to transport us to new worlds, inspire our
                imagination and broaden our perspectives.{' '}
              </p>{' '}
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-center  mt-[2rem]">
                Our goal is to create a platform where book lovers can discover their next
                adventure with ease. Through personalized recommendations and a vibrant
                community, we aim to foster a deep connection between readers and books.
              </p>
              <div className="mt-[2.75rem] lg:flex lg:justify-center">
                <img src={book} alt="" />{' '}
              </div>
            </div>
          </div>
        </div>
        {/* ////////////////////// ///////*/}
        <div className="h-[40.1rem] items-center justify-center mx-[4.5rem]  lg:h-[48.1rem]">
          <div className="h-auto gap-[2.75rem] flex justify-center flex-col items-center ">
            {' '}
            <h1 className="text-[1.25rem] font-bold leading-[3.36rem] text-zenno-aboutb">
              Our Mission
            </h1>
            <div className="h-[23rem] w-auto">
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-center ">
                Our mission is to make book recommendations a delightful adventure for
                book lovers like you! W e believe everyone deserves to discover the
                perfect book that sparks their imagination and leaves them wanting more.{' '}
              </p>{' '}
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-center  mt-[2rem]">
                Our dedicated team works tirelessly to curate a diverse collection of
                books and use innovative technology to match them with your unique taste
                and interests. We’re here to empower you tto explore new genres, discover
                hidden gems and connect with fellow readers who share your passion.
              </p>
              <div className="mt-[2.75rem] lg:flex lg:justify-center">
                <img src={rock} alt="" />{' '}
              </div>
            </div>
          </div>
        </div>
        {/* ////////////////////// ///////*/}
        <div className="h-[40.1rem] items-center justify-center mx-[4.5rem]  lg:h-[48.1rem] mt-[7rem]">
          <div className="h-auto gap-[2.75rem] flex justify-center flex-col items-center">
            {' '}
            <h1 className="text-[1.25rem] font-bold leading-[3.36rem] text-zenno-aboutb">
              Our Process
            </h1>
            <div>
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-center">
                We believe in putting you in the driver’s seat when it comes to exploring
                the incredible world of books. With our cutting edge machine learning and
                semantic search technology, we analyze your reading preference, interests
                and even your mood to provide personalized book recommendations.{' '}
              </p>{' '}
              <p className="text-zenno-aboutb2 font-medium text-[0.93rem] leading-[1.40rem] text-center mt-[2rem]">
                You have the ability to take direct control of your journey, discovering
                new genres, authors and hidden gems that truly resonate with you. It’s all
                about giving you the power to curate your own reading adventure.
              </p>
              <div className="mt-[2.75rem] lg:flex lg:justify-center lg:mt-[3.75rem]">
                <img src={book} alt="" />{' '}
              </div>
            </div>
          </div>
        </div>
        {/* ////////////////////// ///////*/}
        <div className="flex justify-center items-center">
          <h1 className="text-[1.25rem] font-bold leading-[3.36rem] text-zenno-aboutb mt-[6.94rem]">
            Meet Our Team
          </h1>
        </div>
        <div className="flex flex-col justify-items-center gap-x-[1.25rem] gap-y-[3.3rem] mt-[6.94rem] p-[1rem]">
          <div className="h-[11.43rem] flex flex-col items-center gap-[0.75rem]">
            <h1 className="text-zenno-aboutb3 text-[1.75rem] leading-[2.625rem] font-bold text-justify">
              Damilola Oduguwa{' '}
            </h1>
            <p className="text-zenno-4black text-[1.43rem] leading-[2.156rem] font-semibold text-justify">
              Machine Learning Engineer
            </p>
            <h3 className="text-zenno-aboutb3 text-[1.43rem] leading-[2.156rem] font-normal text-justify">
              Portfolio link:
            </h3>
            <a
              href="http://damilojohn.github.io/"
              target="_blank"
              rel="noopener noreferrer"
              className="text-zenno-aboutl"
            >
              http://damilojohn.github.io/
            </a>
          </div>
          <div className="h-[11.43rem] flex flex-col items-center gap-[0.75rem]">
            <h1 className="text-zenno-aboutb3 text-[1.75rem] leading-[2.625rem] font-bold text-justify">
              Daud Abolade{' '}
            </h1>
            <p className="text-zenno-4black text-[1.43rem] leading-[2.156rem] font-semibold text-justify">
              NLP Dataset Collector
            </p>
            <h3 className="text-zenno-aboutb3 text-[1.43rem] leading-[2.156rem] font-normal text-justify">
              Portfolio link:
            </h3>
            <a
              href="https://www.linkedin.com/in/daud-abolade-9b20781b6"
              target="_blank"
              rel="noopener noreferrer"
              className="text-zenno-aboutl text-center"
            >
              https://www.linkedin.com/in/daud-abolade-9b20781b6
            </a>
          </div>
          <div className="h-[11.43rem] flex flex-col items-center gap-[0.75rem]">
            <h1 className="text-zenno-aboutb3 text-[1.75rem] leading-[2.625rem] font-bold text-center">
              Oluwasegun Adebowale{' '}
            </h1>
            <p className="text-zenno-4black text-[1.43rem] leading-[2.156rem] font-semibold text-justify">
              UI/UX Designer
            </p>
            <h3 className="text-zenno-aboutb3 text-[1.43rem] leading-[2.156rem] font-normal text-justify">
              Portfolio link:
            </h3>
            <a
              href="https://linktr.ee/oluwasegun_"
              target="_blank"
              rel="noopener noreferrer"
              className="text-zenno-aboutl"
            >
              https://linktr.ee/oluwasegun_
            </a>
          </div>
          <div className="h-[11.43rem] flex flex-col items-center gap-[0.75rem]">
            <h1 className="text-zenno-aboutb3 text-[1.75rem] leading-[2.625rem] font-bold text-justify">
              Damilola Makinde{' '}
            </h1>
            <p className="text-zenno-4black text-[1.43rem] leading-[2.156rem] font-semibold text-justify">
              Software Developer
            </p>
            <h3 className="text-zenno-aboutb3 text-[1.43rem] leading-[2.156rem] font-normal text-justify">
              Portfolio link:
            </h3>
            <a
              href="https://github.com/mankinde23"
              target="_blank"
              rel="noopener noreferrer"
              className="text-zenno-aboutl"
            >
              https://github.com/mankinde23
            </a>
          </div>
        </div>
        {/* ////////////////////// ///////*/}
        <div className="h-[46.187rem] flex justify-center items-center">
          <img src={mobilebg} alt="" className="top-0 left-0 object-cover absolute" />
          <div className="absolute top-0 left-0 h-[46.187rem]" />
          <div className="absolute top-0 flex flex-col justify-center items-center">
            <div className="h-[622px]">
              {' '}
              <h1 className="text-zenno-1white text-[1.5rem] text-center font-normal">
                What can you find on Zeeno?
              </h1>
              <p className="w-auto h-[24.43rem] text-[1rem] font-medium text-justify mt-[2rem] text-zenno-1white mx-[2rem]">
                Zeeno is the ultimate destination for book enthusiasts seeking their next
                literary adventure. With curated search ideas, diverse genres and
                captivating stories, it’s a one-stop for all your book recommendation
                needs. Zeeno is your gateway to a world of immerse reading experiences,
                creating a sophisticated and comprehensive book recommendation website
                that caters to the diverse taste of readers. Aims to connect readers with
                their next great book, and our goal is to create a platform that inspires,
                engages and enriches the reading journey of every user.
              </p>
              <div className="flex justify-center mt-[3rem]">
                {' '}
                <button className="bg-zenno-1white rounded-[0.625rem] flex justify-center w-[20.125rem] h-[3.8125rem] px-[2.125rem] py-[1.125rem]">
                  {' '}
                  <p className="text-zenno-black text-[1.1rem] font-normal">
                    <Link to="/#top"> Start researching with Zeeno</Link>
                  </p>
                </button>
              </div>
            </div>
          </div>
        </div>
        {/* ////////////////////// ///////*/}
        <div className="flex justify-center items-center">
          <div className="flex flex-col items-center gap-[4.125rem] w-[20.37rem] h-[27.31rem] mb-[8.5rem]">
            <div className="flex justify-center mt-[6rem]">
              <h1 className="text-zenno-aboutb4 text-[1.25rem] font-bold leading-[3.36rem]">
                Why Use Zeeno?
              </h1>
            </div>
            <div className=" w-auto">
              {' '}
              <p className="text-zenno-black text-[1.25rem] font-medium leading-[1.87rem] text-center">
                We make accessing research simple. Our powerful online library features
                millions of{' '}
                <span className="text-zenno-black text-[1.25rem] font-bold leading-[1.87rem]">
                  articles, journals, e-books
                </span>{' '}
                and more, all on a seamless platform.
              </p>{' '}
              <p className="text-zenno-black text-[1.25rem] font-medium leading-[1.87rem] mt-[2rem] text-center">
                You can use comprehensive search ideas to narrow down your research and
                and content with ease.
              </p>
            </div>
          </div>
        </div>
        {/* ////////////////////// ///////*/}
        <Footer />
      </div>
    </>
  );
};

export default About;
