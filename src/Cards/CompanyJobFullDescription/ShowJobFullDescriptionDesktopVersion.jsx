import React from "react";
import ReactDOM from "react-dom";
import Advertisement from "../../Ads/Ads";
import "./ShowJobFullDescriptionDesktopVersion.css"


function ShowJobFullDescriptionDesktopVersion(properties) {
  const return_JobFullDescription_DesktopVersion =
  
      <div className="containerForJobDescription">
      <Advertisement />
        {/* <div className='CompanyJobTittle'>ვაკანსიის ID 📜: {properties.vacancyID}</div>
          <div className='CompanyJobTittle'>ვაკანსია 📜: {properties.jobTittle}</div>
          <div className='companyName'>კომპანია 🏠: {properties.companyName}</div>
          <div>სამუშაო ადგილი 🗺: {properties.jobPlace}</div>
          <div>Email 📧: {properties.companyEmail}</div> */}
          {/* <div className="row"> */}
          {/* <div>ხელფასი 💰: <div type="button" className="btn btn-light btn-sm" data-toggle="tooltip" data-placement="top" title="კომპანიის მიერ შეთავაზებული ხელფასი"> {properties.CompanyJobSalary} </div></div>
          <div>დათვლილი ხელფასი 💰: 
            <div type="button" className="btn btn-light btn-sm" data-toggle="tooltip" data-placement="top" title="მომხმარებლების მიერ განსაზღვრული ხელფასი"> {properties.customSalary}₾ </div>
            <a type="button" className="btn btn-warning btn-sm" href="/">◀ მიანიჭე</a>
          </div> */}
          {/* </div> */}
          {/* <hr />
          <div>{properties.jobFullDescription}</div> */}
          <ul class="list-group">
            <li class="list-group-item"><h5>{properties.jobTittle}</h5></li>
            <li class="list-group-item">კომპანია : {properties.companyName}</li>
            <li class="list-group-item">სამუშაო ადგილი 🗺: {properties.jobPlace}</li>
            <li class="list-group-item">{properties.companyEmail}</li>
            <li class="list-group-item">ხელფასი 💰 {properties.CompanyJobSalary} </li>
            <li class="list-group-item">მომხმარებლების ხელფასი 💰:  {properties.customSalary} <a type="button" className="btn btn-warning btn-sm" href="http://localhost:5000/">◀ მიანიჭე ხელფასი შენ</a></li>
            <li class="list-group-item">ვაკანსიის ID: {properties.vacancyID}</li>
          </ul>
          <hr />
          <div><h3>სამუშაო აღწერილობა</h3></div>
          <div>{properties.jobFullDescription}</div>
      </div>
  ReactDOM.render(return_JobFullDescription_DesktopVersion, document.getElementById("show_full_job"))
}


export default ShowJobFullDescriptionDesktopVersion;