import React, { useEffect, useState } from 'react';
import './Profile.css';

const Profile = () => {
  const [trips, setTrips] = useState([]);

  const handleLogout = () => {
    localStorage.removeItem('spotifyAuthToken');
    window.location.href = "http://localhost:3000/";
  };

  const handleHome = () => {
    window.location.href = "http://localhost:3000/webpage";
  };

  useEffect(() => {
    // Fetch the past trips from your backend API
    fetch('/api/past_trips')
      .then(response => response.json())
      .then(data => setTrips(data.trips))
      .catch(error => console.log(error));
  }, []);

  return (
    <div className="navbar">
      <h1>CommuteBeat</h1>
      <div className="button-wrapper">
        <button className="home-button" onClick={handleHome}>Home</button>
        <button className="logout-button" onClick={handleLogout}>Logout</button>
      </div>

      <div className="past-trips">
        <h2>Past Trips</h2>
        <ul>
          {trips.map((trip, index) => (
            <li key={index}>
              <p>Transportation: {trip.transportation}</p>
              <p>Link: {trip.link}</p>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Profile;
