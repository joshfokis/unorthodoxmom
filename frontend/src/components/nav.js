import React from 'react';
import { Link } from 'react-router-dom'

function Nav() {
  return (
    <div className="container">
      <div className='container' id="navbar-container">
        <nav className="navbar is-fixed-top">
          <div className="navbar-brand">
            <h3 className="navbar-item"></h3>
          </div>
          <div className="navbar-start">
            <Link to="/blog" className="navbar-item" style={{ textDecoration: 'none' }}>
          <a className="navbar-item">Blog</a>
          </Link>
          <Link to="/products" className="navbar-item" style={{ textDecoration: 'none' }}>
          <a className="navbar-item">Products</a>
          </Link>            
          <Link to="/items" className="navbar-item" style={{ textDecoration: 'none' }}>
          <a className="navbar-item">Items</a>
          </Link>          </div>
          <div className="navbar-end">
          <a className="navbar-item"><i className="far fa-envelope"></i></a>
          <a className="navbar-item"><i className="fab fa-facebook"></i></a>
          <a className="navbar-item"><i className="fab fa-instagram"></i></a>
          <a className="navbar-item"><i className="fab fa-youtube"></i></a>
          <a className="navbar-item"><i className="fab fa-pinterest"></i></a>
          <a className="navbar-item"></a>
          </div>
        </nav>
      </div>
    </div>
  );
}

export default Nav;
