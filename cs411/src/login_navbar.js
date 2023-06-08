import React from 'react';
import './login_navbar.css';

function LoginNavbar() {
  return (
    <nav className="navbar">
      <div className="navbar-left">
        <span className="website-name">CommuteBeat</span>
      </div>
      <div className="navbar-right">
        <button className="login-button">Login</button>
      </div>
    </nav>
  );
}

export default LoginNavbar;
