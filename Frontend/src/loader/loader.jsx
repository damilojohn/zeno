import React from 'react'
import ScaleLoader from "react-spinners/ScaleLoader";
import '../loader/loader.css'




const Loader = ({ loading, color = 'black' }) => {
    const override = {
        // display: "block",
        // margin: "0 auto",
        // borderColor: "red",
    };

    return (
        <div className="sweet-loading">
            <ScaleLoader
                color={color}
                loading={loading}
                cssOverride={override}
                size={150}
                aria-label="Loading Spinner"
                data-testid="loader"
            />
        </div>
    )
}

export default Loader
