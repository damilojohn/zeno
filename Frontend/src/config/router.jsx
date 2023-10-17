import BookDetails from "../pages/bookDetails/bookDetails";
import Home from "../pages/home/home";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
const router = createBrowserRouter([
    {
        path: '/',
        element: <Home />
    },
    {
        path: '/bookDetails/:index',
        element: <BookDetails />
    }
])
const RouterComponent = () => (
    <RouterProvider router={router} />
)
export default RouterComponent