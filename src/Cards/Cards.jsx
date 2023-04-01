import React, { useState, useEffect } from 'react';
import ReactDOM from "react-dom"
import "./Cards.css"
import Img from "./image/Img.jsx"
import Name from './CompanyName/Name';
import JobDescription from './CompanyJobdescription/JobDescription';
import CompanyJobTittle from './CompanyJobTittle/CompanyJobTittle';
import JobPlace from './JobPlace/JobPlace';
import ShowJobFullDescriptionDesktopVersion from './CompanyJobFullDescription/ShowJobFullDescriptionDesktopVersion';
import CompanyDescription from './CompanyDescription/CompanyDescription';


//  There is Vacancy Card full stucture
function Cards(properties) {
  //--> I have described colors when mouse is over the button 
  const [is_mouse_over, setMouseOver] = useState(false);
  const mouseOverButton = () => { setMouseOver(true); }
  const mouseOutOfButton = () => { setMouseOver(false) }
  const [pressButton, setpressButton] = useState(false);
  // <--

  // 

  // -->  logic for mobile version, when screen width is less than (in this case 700)
  const [isMobile, setIsMobile] = useState(false);  // {isMobile?  and continue logic}
  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth <= 700) {
        setIsMobile(true);
      } else {
        setIsMobile(false);
      }
    };
    handleResize();
    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);
  // <--


  function DesktopVersion() {
    return <ShowJobFullDescriptionDesktopVersion
      vacancyID={properties.vacancyID}
      jobTittle={properties.jobTittle}
      companyName={properties.companyName}
      jobPlace={properties.jobPlace}
      companyEmail={properties.companyEmail}
      jobFullDescription={properties.jobFullDescription}
      CompanyJobSalary={properties.CompanyJobSalary}
      customSalary={properties.customSalary}
    />
  }

  function MobileVersion() {
    return (
      <div className="backgroundGrandContainer">
        <div className="grandContainer">
          <div>
            <button id="buttonStyle" onClick={() => setpressButton(false)}
              style={{ display: "flex", justifyContent: "flex-end", backgroundColor: is_mouse_over ? "#f5ba13" : "#3A98B9", borderStyle: "none", borderRadius: "5px" }}
              onMouseOver={mouseOverButton}
              onMouseOut={mouseOutOfButton}
            >დახურე ფანჯარა</button>
            <div className="containerForJobDescription">
              <Advertisement />
              <ul class="list-group">
                <li class="list-group-item"><h5>{properties.jobTittle}</h5></li>
                <li class="list-group-item">კომპანია : {properties.companyName}</li>
                <li class="list-group-item">სამუშაო ადგილი 🗺: {properties.jobPlace}</li>
                <li class="list-group-item">{properties.companyEmail}</li>
                <li class="list-group-item">ხელფასი 💰 {properties.CompanyJobSalary} </li>
                <li class="list-group-item">მომხმარებლების ხელფასი 💰:  {properties.customSalary} <a type="button" className="btn btn-warning btn-sm" href="https://calm-crag-71620.herokuapp.com/home">◀ მიანიჭე ხელფასი შენ</a></li>
                <li class="list-group-item">ვაკანსიის ID: {properties.vacancyID}</li>
              </ul>
              <hr />
              <div><h3>სამუშაო აღწერილობა</h3></div>
              <div>{properties.jobFullDescription}</div>
            </div>
          </div>
        </div>
      </div>
  )}




  // --> show company description to work just uncomment
  // const [showOrNotShow, setshowOrNotShow] = useState(false)
  // function CompanyDescripionMain(){
  //   return <div>
  //     <CompanyDescription
  //               companyName={properties.companyName} 
  //               img={properties.img}/>
  //     </div>
  // }
  // <--

  // console.log(isMobile + "  isMobile")
  // console.log(pressButton + "  pressButton")
  return (
          <div className='cards'>
            <div className='CompanyJobTittle'>
              <CompanyJobTittle jobTittle={properties.jobTittle} />
            </div>
            <div className='companyName'>
              {/* this commented button trigers show description logic, so with another comments uncomment this */}
              {/* <button onClick={() => setshowOrNotShow(true)} style={{borderStyle:"none"}}> */}
              <button onClick="" style={{ borderStyle: "none" }}>
                <Name name={properties.companyName} /></button>
            </div>
            <div className='JobLocation'>
              <JobPlace jobPlace={properties.jobPlace} />
            </div>
            <div className='CompanyJobDescription'>
              <JobDescription description={properties.description} />
            </div>
            <div className='companyImg'>
              <Img defaultIMG={properties.img} />
            </div>
            <div className='companyRating'
              style={{
                display: "flex",
                justifyContent: 'center'
              }}
            >⭐4.5</div>
            <div className='WhenWasPublished'>🎯 {properties.companyJobStartDate} 🏁{properties.companyJobEndDate} </div>
            <button className='SeeFullDescription'
              onClick={() => {
                setpressButton(true);
                {/* this commented setshowOrNotShow trigers show description logic, so with another comments uncomment this */ }
                // setshowOrNotShow(false);
              }}
              style={{
                backgroundColor: is_mouse_over ? "#f5ba13" : "white",
                borderStyle: "none",
                borderRadius: "5px"
              }}
              onMouseOver={mouseOverButton}
              onMouseOut={mouseOutOfButton}
            >ნახე მეტი</button>
            {/* bello is the logic thet shows company description when pushed on company name, so just uncomment it */}
            {/* {isMobile ? 
    <>{pressButton ? <MobileVersion /> : ""}</> : 
    <>{showOrNotShow? 
            <CompanyDescripionMain />:<>{pressButton ? <DesktopVersion /> : ""}</> 
            }</>
      } */}
            {isMobile ? <>{pressButton ? <MobileVersion /> : ""}</> : <>{pressButton ? <DesktopVersion /> : ""}</>}
          </div>)
}


          export {Cards};

