// Footer.js
import React from "react";

const Footer = () => {
  return (
    <footer>
      <div className="logo">
        <img src="/images/Footer.png" alt="Footer Logo" />
      </div>
      <nav>
        <ul>
          <li>
            <a href="#">Home</a>
          </li>
          <li>
            <a href="#">About</a>
          </li>
          <li>
            <a href="#">Services</a>
          </li>
          <li>
            <a href="#">Contact</a>
          </li>
        </ul>
      </nav>
      <div className="social-links">
        <a href="#">
          <i className="fab fa-facebook-f"></i>
        </a>
        <a href="#">
          <i className="fab fa-twitter"></i>
        </a>
        {/* Add more social media icons as needed */}
      </div>
      <p>&copy; 2024 Weather wise. All rights reserved.</p>
    </footer>
  );
};

export default Footer;
