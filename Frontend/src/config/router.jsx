import About from '../pages/aboutMe/aboutMe';
import Home from '../pages/home/home';
import {createBrowserRouter, RouterProvider} from 'react-router-dom';
const router = createBrowserRouter([
  {
    path: '/',
    element: <Home />,
  },

  {
    path: '/aboutUs',
    element: <About />,
  },
]);
const RouterComponent = () => <RouterProvider router={router} />;
export default RouterComponent;
