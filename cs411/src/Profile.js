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
    // Function to fetch past trips
    const fetchPastTrips = async () => {
        try {
            const response = await fetch('http://localhost:3000/api/past_trips');
            const data = await response.json();

            // Convert the response to an array
            const tripsArray = Object.values(data);
            setTrips(tripsArray);

        } catch (error) {
            console.log(error);
        }
    };
    
    // Call the fetch function
    fetchPastTrips();
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
              <div>
                <p>Transportation: {trip[0]}</p>
                <p>Link: <a href={trip[1]} target="_blank" rel="noopener noreferrer">Spotify Playlist</a></p>
                <p>From: {trip[2]}</p>
                <p>To: {trip[3]}</p>
            </div>
        </li>
      ))}

          
        </ul>
      </div>
    </div>
  );
};

export default Profile;
