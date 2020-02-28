import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getFridges, deleteFridge } from "../../actions/fridges";

export class Fridges extends Component {
  static propTypes = {
    fridges: PropTypes.array.isRequired,
    getFridges: PropTypes.func.isRequired,
    deleteFridge: PropTypes.func.isRequired
  };

  componentDidMount() {
    this.props.getFridges();
  }

  render() {
    return (
      <Fragment>
        <h2>Fridges</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>STATUS</th>
              <th>Time Since</th>
              <th></th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {this.props.fridges.map(fridge => (
              <tr key={fridge.id}>
                <td>{fridge.id}</td>
                <td>{fridge.name}</td>
                <td>{fridge.fridge_is_empty ? "EMPTY" : "NOT EMPTY"}</td>
                <td>{fridge.time_since.split("T")[0]}</td>
                <td>
                  <button
                    onClick={this.props.deleteFridge.bind(this, fridge.id)}
                    className="btn btn-danger btn-sm"
                  >
                    Delete
                  </button>
                </td>
                <td>
                  <button className="btn btn-success btn-sm">Notify</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

const mapStatetoProps = state => ({
  fridges: state.fridges.fridges
});

export default connect(mapStatetoProps, { getFridges, deleteFridge })(Fridges);
