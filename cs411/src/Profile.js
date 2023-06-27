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
    setTimeout(() => {
      console.log('setTrips data', trips);
    }, 1000); // Delay for 1 second to allow time for state update
  }, [trips]);
  
  useEffect(() => {
    fetch('http://localhost:8000/past_trips', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log('trips response', data.trips);
        if (Array.isArray(data.trips) && data.trips.length > 0) {
          setTrips(data.trips); // Assuming the inner array is the desired array of dictionaries
        }
        console.log('updated trips', trips);
      })
      .catch((error) => console.log(error));
  }, []);

  const renderLink = (text) => (
    <a href={text} target="_blank" rel="noopener noreferrer">
      {text}
    </a>
  );


  return (
    <div>
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
      </div>

      <div className="content">
        <h2>Past Trips</h2>
        <Table dataSource={trips}>
            <Column title="Location" dataIndex="location" key="location" />
            <Column title="Destination" dataIndex="destination" key="destination" />
            <Column title="Transportation" dataIndex="transportation" key="transportation" />
            <Column title="Link" dataIndex="link" key="link" render={renderLink} />
        </Table>
      </div>
    </div>
  );
};

export default Profile;
