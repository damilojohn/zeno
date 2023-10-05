import React from 'react'
import { useState, } from "react";
import ClipLoader from "react-spinners/ClipLoader";
import '../loader/loader.css'




const Loader = ({ loading, color = 'red' }) => {
    const override = {
        // display: "block",
        // margin: "0 auto",
        // borderColor: "red",
    };
    // let [color, setColor] = useState("");
    return (
        <div className="sweet-loading">
            <ClipLoader
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
