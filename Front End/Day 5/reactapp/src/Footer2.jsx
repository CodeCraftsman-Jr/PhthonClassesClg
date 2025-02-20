import React from 'react'
import './Footer.css'

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <p>&copy; 2025 MyWebsite. All Rights Reserved.</p>
        <div className="social-media">
          <a href="#facebook" className="social-icon">Facebook</a>
          <a href="#twitter" className="social-icon">Twitter</a>
          <a href="#instagram" className="social-icon">Instagram</a>
        </div>
      </div>
    </footer>
  )
}

export default Footer
