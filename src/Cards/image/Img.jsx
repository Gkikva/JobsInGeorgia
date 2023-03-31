import React from 'react';
import "./Img.css"


function Img(propsImg) {
    return <img className="defaultImage" src={propsImg.defaultIMG} alt="Company Logo" />
}

export default Img;