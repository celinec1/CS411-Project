import React from 'react';
import Home_page from './Home_page';
import "./App.css";
import LoginPage from './login'; // import the login component
import WebPage from './WebPage'

//home page works!
function App() {
    return (
      <div className="App">
        {/* <Home_page /> */}
        <WebPage />
        <header className="App-header"> </header>
      </div>
    );
  }


export default App;
