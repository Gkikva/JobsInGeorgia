import React from 'react';
import ReactDOM from "react-dom";

import Img from '../image/Img';
import "./CompanyDescription.css"



function CompanyDescription(properties) {
    const what_to_return =
            <div className='containerCompanyDescription'>
                <div className="container">
                    <div className="row">
                        <div className="col-lg-4"></div>
                        <div className="col-lg-4" style={{ display: 'flex', justifyContent: 'center' }}>
                            <Img defaultIMG={properties.img} />
                        </div>
                        <div className="col-lg-4"></div>
                    </div>
                </div>
                <h3>{properties.companyName}</h3>
                <div className="container">
                    <div className="row">
                        <div className="col-lg-4">
                            <button type="button" class="btn btn-outline-warning" data-toggle="tooltip" data-placement="top" title="რამდენად ბედნიერად გრძნობს თავს დასაქმებული">67 ბედნიერების ინდექსი ☺</button>
                        </div>
                        <div className="col-lg-4">
                            <button type="button" class="btn btn-outline-warning" data-toggle="tooltip" data-placement="top" title="რამდენად მიმზიდველი სამუშაო გარემოა">67 სამუშაო გარემოს      ☺</button>
                        </div>
                        <div className="col-lg-4">
                            <button type="button" class="btn btn-outline-warning" data-toggle="tooltip" data-placement="top" title="რამდენად აფასებენ თქვენს სამუშაოს ან თქვენ">67 დაფასების ინდექს ☺</button>
                        </div>
                    </div>
                </div>
                <hr />
                <div className="container">
                    <div className="row">
                        <div class="card border-success mb-3">
                            <div class="card-body text-secondary">
                                <p class="card-text">აქ გაუშვი კიდევ რა ვაკანსიები აქვს</p>
                            </div>
                        </div>
                    </div>
                </div>
                <hr />
                <form action='/sendData' method='POST'>
                    <div className="container">
                        <div className="row">
                            <input type="text" name='sendCommentData'></input>
                            <button className='btn btn-primary' type='submit'>submit</button>
                        </div>
                    </div>
                </form>
            </div>
    ReactDOM.render(what_to_return, document.getElementById("show_full_job"))
}

export default CompanyDescription;