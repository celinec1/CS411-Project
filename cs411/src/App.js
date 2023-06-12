// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// import React from 'react';
// import "./App.css";
// import Home_page from './Home_page';

// function App() {
//   return (
//     <div className="App">
//       <Home_page />
//       <header className="App-header"> </header>
//     </div>
//   );
// }

// export default App;

import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import HomePage from './Home_page';
import LoginPage from './login'; // import the login component

const App = () => {
  return (
    <Router>
      <Route path="/" exact component={HomePage} />
      <Route path="/login" component={LoginPage} />  // set the path to your login component
    </Router>
  );
};

export default App;
