import React, { useEffect, useState } from 'react';
import './Profile.css';
import { Space, Table, Tag } from 'antd';

const { Column, ColumnGroup } = Table;

const Profile = () => {
  const [trips, setTrips] = useState([]);

  const handleLogout = () => {
    localStorage.removeItem('spotifyAuthToken');
    window.location.href = 'http://localhost:3000/';
  };

  const handleHome = () => {
    window.location.href = 'http://localhost:3000/webpage';
  };

  useEffect(() => {
    // Fetch the past trips from your backend API
    fetch('/api/past_trips')
      .then((response) => response.json())
      .then((data) => setTrips(data.trips))
      .catch((error) => console.log(error));
      console.log('trip data:', trips);
  }, []);

  return (
    <div className="navbar">
      <h1>CommuteBeat</h1>
      <div className="button-wrapper">
        <button className="home-button" onClick={handleHome}>
          Home
        </button>
        <button className="logout-button" onClick={handleLogout}>
          Logout
        </button>
      </div>

      <div className="past-trips">
        <h2>Past Trips</h2>
        <Table dataSource={trips}>
          <Column title="Transportation" dataIndex="transportation" key="transportation" />
          <Column title="Link" dataIndex="link" key="link" />
        </Table>
      </div>
    </div>
  );
};

export default Profile;
