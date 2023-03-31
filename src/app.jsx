import React, { useState, useEffect } from 'react';
import { Cards } from './Cards/Cards';
import Heading from './Header/Heading';
import './searchBar.css';
import "bootstrap/dist/css/bootstrap.min.css"
import axios from 'axios';


function creatingCard(contacts) {
  return <Cards
    key={contacts.id}
    vacancyID={contacts.id}
    companyName={contacts.CompanyName}
    companyEmail={contacts.CompanyEmail}
    jobTittle={contacts.CompanyJobTitle}
    img={contacts.CompanyImage}
    description={contacts.CompanyJobShortDesciption}
    jobFullDescription={contacts.CompanyJobLongDesciption}
    jobPlace={contacts.JobPlace}
    companyJobStartDate={contacts.companyJobStartDate}
    companyJobEndDate={contacts.companyJobEndDate}
    companyPhone={contacts.companyPhone}
    CompanyJobSalary={contacts.CompanyJobSalary}
    customSalary = {contacts.customSalary}
  />

}


function Navbar() {
  return <Heading />
}


function App() {
  const [search, setsearch] = useState("");
  const [data, setData] = useState([]);
  const [loading, setloading] = useState(true);

  useEffect(() => {
    axios.get('api/data?search=${search}')
      // axios.get('http://localhost:5000/api/data')
      .then(res => {
        const data = res.data;
        setData(data); // ასევე აქ შეგიძლია ჩაწერო setData(data['companyData'])
        setloading(false)
      })
  }, [])


  

  const search_by_job_tittle = data?.filter(contact => contact.CompanyJobTitle.toLowerCase().includes(search)).map(creatingCard)
  // console.log(search_by_job_tittle)
  // const search_by_company = data?.CompanyData?.filter(contact => {return contact.CompanyName.toLowerCase().includes(search)}).map(creatingCard)


  if (loading) return <div className="text-center"><button className="btn btn-primary" type="button" disabled>
    <span className="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
    იტვირთება...
  </button>
  </div>

  return <div>
    <div className='container'>
      <div className="row">
        <div className="col-lg-12"><input type="text" placeholder='მოძებნე ვაკანსია' className='searchBar' onChange={(event) => setsearch(event.target.value)} /></div>
        {/* <div className="col-lg-6"><input  type="text" placeholder='მოძებნე კომპანია' className='searchBar' onChange={(event) => setsearch(event.target.value)}/></div> */}
      </div>
    </div>

    <hr />
    <div className="container">
      <div className="row">
        <div className="col-md-5">
          <>{data && search_by_job_tittle}</>
        </div>
        {/* className="col-md-7 d-none d-md-block" means that when columns goes bellow md it will disappear  */}
        <div className="col-md-7 d-none d-md-block ">
          <div id="show_full_job"></div>
        </div>
      </div>
    </div>

  </div>
}


export { App, Navbar };