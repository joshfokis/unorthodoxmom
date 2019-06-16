import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Nav from './components/nav';
import Footer from './components/footer';
import Homev2 from './components/homev2';
import Blog from './components/blog';
import Post from './components/post';


import './App.css';


function App() {
    
    return (
    <Router>
      <div className="App">
        <header className="App-header">
        </header>
        <Nav />
        {/* <Switch> */}
        <section className="main-content">
          <Route path="/" exact component={Homev2} />
          <Route path="/blog" exact component={Blog} />
          <Route path="/blog/:id" component={Post} />
        </section>
        {/* </Switch> */}
        <Footer />
      </div>
    </Router>
  );
}

export default App;
