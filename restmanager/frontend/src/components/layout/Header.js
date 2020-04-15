import React, { Component } from "react";

export class Header extends Component {
  render() {
    /*
        Header from https://getbootstrap.com/docs/4.1/components/navbar/
        */
    return (
      <nav className="navbar navbar-expand-sm navbar-light bg-light">
        <button
          className="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarTogglerDemo01"
          aria-controls="navbarTogglerDemo01"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarTogglerDemo01">
          <a className="navbar-brand" href="#">
            Fridge Management UI
          </a>
          <ul className="navbar-nav mr-auto mt-2 mt-lg-0"></ul>
        </div>
      </nav>
    );
  }
}

export default Header;
