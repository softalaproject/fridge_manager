import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addFridge } from "../../actions/fridges";

export class Form extends Component {
  state = {
    name: "",
    fridge_is_empty: "",
    time_since: ""
  };

  static propTypes = {
    addFridge: PropTypes.func.isRequired
  };

  render() {
    return (
      <div>
        <h1>Add Fridge Form</h1>
      </div>
    );
  }
}

export default Form;
