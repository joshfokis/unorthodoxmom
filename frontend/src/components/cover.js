import React, { Component } from 'react';

function Cover() {
    
    return (
        <section className="hero is-fullheight-with-navbar">
        <div className="hero-body cover">
            <div className="container">
            <h1 className="title has-text-white custom-font">Unorthodox Mom</h1>
            <h2 className="subtitle has-text-white">Subtitle</h2>
            </div>
        </div>
        <div className="next-arrow pulse">
            <a href="#about"><i class="fas fa-angle-double-down has-text-white is-size-1"></i></a>
        </div>
        </section>
    );
}

export default Cover;