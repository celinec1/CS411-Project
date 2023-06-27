import React, { useState, useEffect } from 'react';
import './WebPage.css';

const WebPage = () => {
  const [isFormSubmitted, setIsFormSubmitted] = useState(false);
  const [selectedTransportation, setSelectedTransportation] = useState('');
  const [isTransportationSubmitted, setIsTransportationSubmitted] = useState(false);
  const [backendResponse, setBackendResponse] = useState('');

  useEffect(() => {
    console.log('backendResponse:', backendResponse);
  }, [backendResponse]);

  const[driving, setDriving] = useState(null);
  const[bicycling, setBicycling] = useState(null);
  const[transit, setTransit] = useState(null);
  const[walking, setWalking] = useState(null);
  const [recommended, setRecommended] = useState(null);
  const [temp, setTemp] = useState(null);
  const [condition, setCondition] = useState(null);
  const [isRestarted, setIsRestarted] = useState(false);

  const handleRestart = () => {
    setIsFormSubmitted(false);
    setIsTransportationSubmitted(false);
    setIsRestarted(true);
  };

  //log out
  const handleLogout = () => {
    localStorage.removeItem('spotifyAuthToken'); // Replace 'spotifyAuthToken' with the key you used to store the Spotify token.
    window.location.href = "http://localhost:3000/"; // Redirect to login page (or whichever page you want the user to be redirected to after logout).
  };

  //profile
  const handleprofile = () => {
    window.location.href = "http://localhost:3000/profile"; 
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
        setDriving(data.driving);
        setBicycling(data.bicycling);
        setTransit(data.transit);
        setWalking(data.walking);
        setRecommended(data.recommended);
        setTemp(data.temp);
        setCondition(data.condition);
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
        setBackendResponse(data.link); // Store the backend response in a state variable

        console.log('backendResponse:', backendResponse);
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
          <div className="button-wrapper">
          <button className="profile-button" onClick={handleprofile}>Profile</button>
          <button className="logout-button" onClick={handleLogout}>Logout</button>

        </div>
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
        <div className="navbar2">
          <h1>CommuteBeat</h1>
          <div className="button-wrapper">
            <button className="profile-button" onClick={handleprofile}>Profile</button>
            <button className="logout-button" onClick={handleLogout}>Logout</button>
          </div>
        </div>
  
        <div className="transportation-selection">
          <h2>Select mode of transportation:</h2>
  
          {driving && driving.length > 0 ? (
            <div className="transportation-buttons">
              <div>
                <button
                  className={`transportation-button ${selectedTransportation === 'driving' ? 'selected' : ''}`}
                  onClick={() => handleTransportationSelect('driving')}
                >
                  Driving
                </button>
                <p>{driving}</p>
              </div>
            </div>
          ) : (
            <div>
              <p>{!driving ? 'Driving mode not available' : 'No valid modes of transportation found'}</p>
            </div>
          )}
  
          {bicycling && bicycling.length > 0 ? (
            <div className="transportation-buttons">
              <div>
                <button
                  className={`transportation-button ${selectedTransportation === 'bicycling' ? 'selected' : ''}`}
                  onClick={() => handleTransportationSelect('bicycling')}
                >
                  Bicycling
                </button>
                <p>{bicycling}</p>
              </div>
            </div>
          ) : (
            <div>
              <p>{!bicycling ? 'Bicycling mode not available' : 'No valid modes of transportation found'}</p>
            </div>
          )}
  
          {transit && transit.length > 0 ? (
            <div className="transportation-buttons">
              <div>
                <button
                  className={`transportation-button ${selectedTransportation === 'transit' ? 'selected' : ''}`}
                  onClick={() => handleTransportationSelect('transit')}
                >
                  Transit
                </button>
                <p>{transit}</p>
              </div>
            </div>
          ) : (
            <div>
              <p>{!transit ? 'Transit mode not available' : 'No valid modes of transportation found'}</p>
            </div>
          )}
  
          {walking && walking.length > 0 ? (
            <div className="transportation-buttons">
              <div>
                <button
                  className={`transportation-button ${selectedTransportation === 'walking' ? 'selected' : ''}`}
                  onClick={() => handleTransportationSelect('walking')}
                >
                  Walking
                </button>
                <p>{walking}</p>
              </div>
            </div>
          ) : (
            <div>
              <p>{!walking ? 'Walking mode not available' : 'No valid modes of transportation found'}</p>
            </div>
          )}
  
          

{temp && (
          <div className="weather-report">
            <h3>Weather Forecast:</h3>
            <p>{`Temperature: ${temp}`}</p>
            <p>{`Condition: ${condition}`}</p>
          </div>
        )}

        <div className="recommended">
        <h3>Our Recommendation:</h3>
            <p>{recommended}</p>
          </div>

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
          <div className="button-wrapper">
          <button className="profile-button" onClick={handleprofile}>Profile</button>
          <button className="logout-button" onClick={handleLogout}>Logout</button>
        </div>
        </div>

        {/* <div className="playlist-section">
          <h2>Here is the Spotify playlist!</h2>
          {backendResponse && <p>{backendResponse}</p>} */}
         
          <div className="playlist-section">
  <h2>Here is the Spotify playlist!</h2>
  {backendResponse && (
    <p>
      <a href={backendResponse} target="_blank" rel="noopener noreferrer">
        {backendResponse}
      </a>
    </p>
  )}
          <button className="restart-button" onClick={handleRestart}>
        Restart
      </button>
        </div>
      </div>
    );
  }
};

export default WebPage;