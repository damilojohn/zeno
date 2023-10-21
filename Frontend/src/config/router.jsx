// import BookDetails from "../pages/bookDetails/bookDetails";
import Home from "../pages/home/home";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
const router = createBrowserRouter([
    {
        path: '/',
        element: <Home />
    },
    // {
    //     path: '/bookDetails/:isbn10',
    //     element: <BookDetails />
    // }
])
const RouterComponent = () => (
    <RouterProvider router={router} />
)
export default RouterComponent