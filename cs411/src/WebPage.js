import React, { useState } from 'react';
import './WebPage.css';

const WebPage = () => {
  const [isFormSubmitted, setIsFormSubmitted] = useState(false);
  const [selectedTransportation, setSelectedTransportation] = useState('');
  const [isTransportationSubmitted, setIsTransportationSubmitted] = useState(false);
  const [backendResponse, setBackendResponse] = useState(null);
  const [durations, setDurations] = useState(null);
  const [recommended, setRecommended] = useState(null);
  const [weather, setWeather] = useState(null);
  const [isRestarted, setIsRestarted] = useState(false);

  const handleRestart = () => {
    setIsFormSubmitted(false);
    setIsTransportationSubmitted(false);
    setIsRestarted(true);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const location = event.target.locationInput.value;
    const destination = event.target.destinationInput.value;
    console.log('Location:', location);
    console.log('Destination:', destination);
    event.target.reset();
    setIsFormSubmitted(true);
    

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
        const data = await response.json();
        console.log('Response from backend:', data);
        setDurations(data.durations);  // Store the durations
        setRecommended(data.recommended);
        setWeather(data.forecast);
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
        console.log('backendResponse:', backendResponse); // Make sure the variable is being set
      } else {
        console.log('Failed to fetch response from backend');
      }
    } catch (error) {
      console.log('Error:', error);
    }
  };


  if (!isFormSubmitted) {
    return (
      <div>
        <div className="navbar">
          <h1>CommuteBeat</h1>
          <button>Profile</button>
        </div>

        <div className="user-input">
          <h2>Enter your location and destination:</h2>
          <form onSubmit={handleSubmit}>
            <input type="text" id="locationInput" placeholder="Enter location" required />
            <input type="text" id="destinationInput" placeholder="Enter destination" required />
            <button type="submit">Submit</button>
          </form>
        </div>
      </div>
    );
  } else if (!isTransportationSubmitted) {
    return (
      <div>
        <div className="navbar">
          <h1>CommuteBeat</h1>
          <button>Profile</button>
        </div>

        <div className="transportation-selection">
          <h2>Select mode of transportation:</h2>

          {durations && (
            <div className="transportation-buttons">
              <div>
                <button
                  className={`transportation-button ${selectedTransportation === 'driving' ? 'selected' : ''}`}
                  onClick={() => handleTransportationSelect('driving')}
                >
                  Driving
                </button>
                <p>{durations.driving[0]}</p>
              </div>

              <div>
                <button
                  className={`transportation-button ${selectedTransportation === 'bicycling' ? 'selected' : ''}`}
                  onClick={() => handleTransportationSelect('bicycling')}
                >
                  Bicycling
                </button>
                <p>{durations.bicycling[0]}</p>
              </div>

              <div>
                <button
                  className={`transportation-button ${selectedTransportation === 'transit' ? 'selected' : ''}`}
                  onClick={() => handleTransportationSelect('transit')}
                >
                  Transit
                </button>
                <p>{durations.transit[0]}</p>
              </div>

              <div>
                <button
                  className={`transportation-button ${selectedTransportation === 'walking' ? 'selected' : ''}`}
                  onClick={() => handleTransportationSelect('walking')}
                >
                  Walking
                </button>
                <p>{durations.walking[0]}</p>
              </div>
            </div>
          )}

{weather && (
          <div className="weather-report">
            <h3>Weather Forecast:</h3>
            <p>{`Temperature: ${weather.temperature}`}</p>
            <p>{`Condition: ${weather.condition}`}</p>
          </div>
        )}

          <div className="button-group">
            <button className="previous-button" onClick={handlePrevious}>
              Previous
            </button>
            <button className="submit-button" onClick={handleTransportationSubmit}>
              Submit
            </button>
          </div>
        </div>
      </div>
    );
  } else {
    return (
      <div>
        <div className="navbar">
          <h1>CommuteBeat</h1>
          <button>Profile</button>
        </div>

        <div className="playlist-section">
          <h2>Here is the Spotify playlist!</h2>
          {backendResponse && <p>{backendResponse.message}</p>}
          <button className="restart-button" onClick={handleRestart}>
        Restart
      </button>
        </div>
      </div>
    );
  }
};

export default WebPage;
