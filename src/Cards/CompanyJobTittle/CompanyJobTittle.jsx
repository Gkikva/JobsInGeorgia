import React, {useState} from 'react';
import "./CompanyJobTittle.css"


function CompanyJobTittle(propsName){
    const [text, setText] = useState(propsName.jobTittle)
    let shortText = text.substring(0,35)
    return <div className='CompanyJobTittle'>{shortText} ...</div>
}

export default CompanyJobTittle;