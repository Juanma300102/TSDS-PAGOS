import { Outlet } from "react-router-dom"

export default () => {
    return(
        <>
        <div>
            <p>Hola este es mi layout</p>
            <Outlet/>
        </div>
        </>
    )
}