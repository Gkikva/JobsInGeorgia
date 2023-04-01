import React from "react";
import ReactDOM from "react-dom";
import Advertisement from "../../Ads/Ads";
import "./ShowJobFullDescriptionDesktopVersion.css"


function ShowJobFullDescriptionDesktopVersion(properties) {
  const return_JobFullDescription_DesktopVersion =
  
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
  ReactDOM.render(return_JobFullDescription_DesktopVersion, document.getElementById("show_full_job"))
}


export default ShowJobFullDescriptionDesktopVersion;