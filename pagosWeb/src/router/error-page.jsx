import { useRouteError } from "react-router-dom";

export default () => {
    const error = useRouteError()
    console.error(error)

    return(
        <>
        <h1>Oops!</h1>
        <p>{error.statusText || error.message}</p>
        </>
    )
}