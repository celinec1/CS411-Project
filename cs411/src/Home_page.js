import React from 'react';
import './Home_page.css';

const Home_page = () => {
  return (
    <div className="home-container">
      <div className="overlay">
        <h1 className="overlay-text">CommuteBeat</h1>
        {/* <h1 className="overlay-text">CommuteBeat</h1>
        <h1 className="overlay-text">CommuteBeat</h1> */}
      </div>
      <div className="login-container">
        <button className="login-button">Login</button>
      </div>
    </div>
  );
};

export default Home_page;
