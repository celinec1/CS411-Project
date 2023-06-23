// import React from 'react';
// import Home_page from './Home_page';
// import "./App.css";
// import LoginPage from './login'; // import the login component
// import WebPage from './WebPage'

// //home page works!
// function App() {
//     return (
//       <div className="App">
//         <Home_page />
//         {/* <WebPage /> */}
//         <header className="App-header"> </header>
//       </div>
//     );
//   }




// export default App;

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home_page from './Home_page';
import WebPage from './WebPage';
import "./App.css";

function App() {
    return (
      <Router>
        <div className="App">
          <Routes>
            <Route path="/" element={<Home_page />} />
            <Route path="/webpage" element={<WebPage />} />
          </Routes>
        </div>
      </Router>
    );
}

export default App;
