import { createBrowserRouter } from "react-router-dom";
import Landing from '../pages/landing'
import UserLayout from "../layouts/userLayout";
import Login from "../pages/login";
import UserHome from "../pages/user/home"
import ErrorPage from "./error-page";
import MyProfile from "../pages/user/profile"

export default createBrowserRouter([
    {
        path: "/",
        element: <Landing/>,
        errorElement: <ErrorPage/>,
    },
    {
        path: "/login",
        element: <Login/>,
    },
    {
        path: "/h",
        element: <UserLayout/>,
        errorElement: <ErrorPage/>,
        children: [
            {
                path: "",
                element: <UserHome/> 
            },
            {
                path: 'my-profile',
                element: <MyProfile/>
            }
        ]
    }
])