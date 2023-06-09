import React from 'react';
import { useHistory } from 'react-router-dom';
import './Home_page.css';

const Home_page = () => {
  const history = useHistory();

  const handleLoginClick = () => {
    history.push('/login'); // replace '/login' with the path to your login page
  }

  return (
    <div className="home-container">
      <div className="overlay">
        <h1 className="overlay-text">CommuteBeat</h1>
        <h1 className="body-text">Find the best route to your destination and a personalized Spotify playlist as you head over! </h1>
      </div>
      <div className="login-container">
        <button className="login-button" onClick={handleLoginClick}>Login</button>
      </div>
    </div>
  );
};

export default Home_page;
