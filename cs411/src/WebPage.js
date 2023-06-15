import React, { useState } from 'react';
import './WebPage.css';

const WebPage = () => {
  const [isFormSubmitted, setIsFormSubmitted] = useState(false);
  const [selectedTransportation, setSelectedTransportation] = useState('');
  const [isTransportationSubmitted, setIsTransportationSubmitted] = useState(false);
  const [backendResponse, setBackendResponse] = useState(null);
  
  const handleSubmit = async (event) => {
    event.preventDefault();
    const location = event.target.locationInput.value;
    const destination = event.target.destinationInput.value;

    console.log('Location:', location);
    console.log('Destination:', destination);

    event.target.reset();
    setIsFormSubmitted(true);

    // Send the POST request to the backend
    try {
      const response = await fetch('http://localhost:8000/api/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ location, destination }),
      });

      if (response.ok) {
        console.log('Data sent to backend successfully');
        // Optionally, you can do something with the response from the backend
        const data = await response.json();
        console.log('Response from backend:', data);
      } else {
        console.log('Failed to send data to backend');
      }
    } catch (error) {
      console.log('Error:', error);
    }
  };

  const handleTransportationSelect = (transportation) => {
    setSelectedTransportation(transportation);
    setIsTransportationSubmitted(false);
  };

  const handlePrevious = () => {
    setIsFormSubmitted(false);
    setSelectedTransportation('');
    setIsTransportationSubmitted(false);
  };

  const handleTransportationSubmit = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/transportation', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ transportation: selectedTransportation }),
      });
  
      if (response.ok) {
        const data = await response.json();
        console.log('Response from backend:', data);
        setIsTransportationSubmitted(true);
        setBackendResponse(data); // Store the backend response in a state variable
        console.log('backendResponse:', backendResponse); //make sure the variable is being set
      } else {
        console.log('Failed to fetch response from backend');
      }
    } catch (error) {
      console.log('Error:', error);
    }
  };

  return (
    <div>
      <div className="navbar">
        <h1>CommuteBeat</h1>
        <button>Profile</button>
      </div>

      {!isFormSubmitted ? (
        <div className="user-input">
          <h2>Enter your location and destination:</h2>
          <form onSubmit={handleSubmit}>
            <input type="text" id="locationInput" placeholder="Enter location" required />
            <input type="text" id="destinationInput" placeholder="Enter destination" required />
            <button type="submit">Submit</button>
          </form>
        </div>
      ) : (
        <div className="transportation-selection">
          <h2>Select mode of transportation:</h2>
          <div className="transportation-buttons">
            <button
              className={`transportation-button ${selectedTransportation === 'driving' ? 'selected' : ''}`}
              onClick={() => handleTransportationSelect('driving')}
            >
              Driving
            </button>
            <button
              className={`transportation-button ${selectedTransportation === 'bicycling' ? 'selected' : ''}`}
              onClick={() => handleTransportationSelect('bicycling')}
            >
              Bicycling
            </button>
            <button
              className={`transportation-button ${selectedTransportation === 'transit' ? 'selected' : ''}`}
              onClick={() => handleTransportationSelect('transit')}
            >
              Transit
            </button>
            <button
              className={`transportation-button ${selectedTransportation === 'walking' ? 'selected' : ''}`}
              onClick={() => handleTransportationSelect('walking')}
            >
              Walking
            </button>
          </div>
          <div className="button-group">
            <button className="previous-button" onClick={handlePrevious}>
              Previous
            </button>
            <button className="submit-button" onClick={handleTransportationSubmit}>
              Submit
            </button>
          </div>
          {isTransportationSubmitted && (
            <div className="playlist-section">
              <h2>Here is the Spotify playlist!</h2>
              {backendResponse && (
              <p>{backendResponse.message}</p>
              )}  
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default WebPage;

