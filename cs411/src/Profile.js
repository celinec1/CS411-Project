import React from 'react';
import './Profile.css';

const Profile = () => {
    const handleLogout = () => {
        localStorage.removeItem('spotifyAuthToken'); // Replace 'spotifyAuthToken' with the key you used to store the Spotify token.
        window.location.href = "http://localhost:3000/"; // Redirect to login page (or whichever page you want the user to be redirected to after logout).
      };

      const handleHome= () => {
        window.location.href = "http://localhost:3000/webpage"; // Redirect to login page (or whichever page you want the user to be redirected to after logout).
      };
    
  return (
    <div className="navbar">
      <h1>CommuteBeat</h1>
      <div className="button-wrapper">
      <button className="home-button" onClick={handleHome}>Home</button>
      <button className="logout-button" onClick={handleLogout}>Logout</button>
      </div>
    </div>
  );
};

export default Profile;
