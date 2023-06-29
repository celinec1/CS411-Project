import React, { useState } from 'react';

function App() {
  const handleLogin = () => {
    console.log('Login button clicked');
    fetch('/callback')
      .then((res) => {
        if (res.ok) {
          return res.json();
        } else {
          throw new Error('Failed to initiate Spotify login');
        }
      })
      .then((data) => {
        window.location.href = data.url;
      })
      .catch((err) => {
        console.error('Failed to initiate Spotify login:', err);
      });
  };

  return (
    <div>
      <button onClick={handleLogin}>Spotify Login</button>
    </div>
  );
}

export default App;
