import React from 'react';
import './login.css';

const LoginPage = () => {
  return (
    <div className="login-container">
      <form className="login-form">
        <input type="email" placeholder="Email" required />
        <input type="password" placeholder="Password" required />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default LoginPage;
