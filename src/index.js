import React from 'react';
import ReactDOM from 'react-dom/client';
import { App, Navbar } from './app';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import axios from 'axios';




// In this case Brings  Jobs In georgia tittle
// const navbar = ReactDOM.createRoot(document.getElementById("banner"))
// navbar.render(<Navbar />)

// // // App bring Cards
// const root = ReactDOM.createRoot(document.getElementById("root"))
// root.render(<App />)

function MainPage() {
    return <div>
        <Navbar />
        <App />
    </div>
}

const user = {
    "CompanyJobSalary": "6500-9000 EURO",
    "CompanyJobShortDesciption": "AI data structure inginier",
    "CompanyJobTitle": "AI system developer",
    "CompanyName": "AI Company",
    "JobPlace": "თბილისი",
    "companyJobEndDate": "2023-03-30",
    "companyJobStartDate": "2023-03-26",
    "companyPhone": 987654321,
}

function CompanyDescription() {
    return axios.post("/api/data", user)
}
console.log(CompanyDescription)

export default function Routing() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<MainPage />}>
                </Route>
                <Route path="/" element={<CompanyDescription />}>
                </Route>
            </Routes>
        </BrowserRouter>
    );
}


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Routing />);