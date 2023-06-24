import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home_page from './Home_page';
import WebPage from './WebPage';
import Profile from './Profile'
import "./App.css";

function App() {
    return (
      <Router>
        <div className="App">
          <Routes>
            <Route path="/" element={<Home_page />} />
            <Route path="/webpage" element={<WebPage />} />
            <Route path="/profile" element={<Profile />} />
          </Routes>
        </div>
      </Router>
    );
}

export default App;
