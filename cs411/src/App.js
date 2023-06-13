import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
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

// const App = () => {
//   return (
//     <Router>
//       <Route path="/" exact component={HomePage} />
//       <Route path="/login" component={LoginPage} />  // set the path to your login component
//     </Router>
//   );
// };

export default App;
