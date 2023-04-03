import React from 'react';
import ReactDOM from 'react-dom/client';
import { App, Navbar } from './app';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ToBackEnd from './navTobackEnd';




// In this case Brings  Jobs In georgia tittle
// const navbar = ReactDOM.createRoot(document.getElementById("banner"))
// navbar.render(<Navbar />)

// // // App bring Cards
// const root = ReactDOM.createRoot(document.getElementById("root"))
// root.render(<App />)

function MainPage() {
    return <div>
        <ToBackEnd />
        <Navbar />
        <App />
    </div>
}

export default function Routing() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<MainPage />}>
                </Route>
            </Routes>
        </BrowserRouter>
    );
}


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Routing />);