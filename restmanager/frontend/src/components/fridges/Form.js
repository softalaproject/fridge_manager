import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { addFridge } from "../../actions/fridges";

export class Form extends Component {
  state = {
    name: "",
    fridge_is_empty: false
  };

  static propTypes = {
    addFridge: PropTypes.func.isRequired
  };

  handleFridgeStatus = e => {
    const fridge_is_empty = e.target.checked;
    this.setState({ fridge_is_empty });
  };

  onChange = e => this.setState({ [e.target.name]: e.target.value });

  onSubmit = e => {
    e.preventDefault();
    const { name, fridge_is_empty } = this.state;
    const fridge = { name, fridge_is_empty };
    this.props.addFridge(fridge);
  };

  render() {
    const { name, fridge_is_empty } = this.state;
    return (
      <div className="card card-body mt-4 mb-4">
        <h2>Add Lead</h2>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>Name</label>
            <input
              className="form-control"
              type="text"
              name="name"
              onChange={this.onChange}
              value={name}
            />
          </div>
          <div className="form-group">
            <label>Fridge is empty</label>
            <input
              name="fridge_is_empty"
              type="checkbox"
              checked={fridge_is_empty}
              onChange={this.handleFridgeStatus}
            />
          </div>
          <div className="form-group">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
        </form>
      </div>
    );
  }
}
//Since we dont need to bring any state back to this component,
// so we can have "null" as first parameter and only include the method that we are calling
export default connect(null, { addFridge })(Form);
