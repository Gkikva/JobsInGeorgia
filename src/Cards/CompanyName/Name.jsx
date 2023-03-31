import React, { useState } from 'react';
import "./Name.css"


function Name(propsName){
    const [text, setText] = useState(propsName.name)
    let shortText = text.substring(0,17)
    return <div className='Name'>{shortText} ...</div>

}

export default Name;