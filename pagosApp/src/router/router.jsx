import { createBrowserRouter } from "react-router-dom";
import Login from "../pages/login/login";
import Home from "../pages/home/home";
import Conceptos from "../pages/gestion/conceptos/main";

export default createBrowserRouter([
  {
    path: "/",
    element: <Login />,
  },
  {
    path: "h/",
    element: <Home />,
    children: [
      {
        path: "gestion/",
        element: <Home />,
        children: [
          {
            path: "conceptos/",
            element: <Conceptos />,
          },
        ],
      },
    ],
  },
]);
