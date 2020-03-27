import React, { Fragment } from "react";
import Form from "./Form";
import Fridges from "./Fridges";

/*
Dasboard includes:
Form.js
Fridges.js 
*/

export default function Dashboard() {
  return (
    <Fragment>
      <Form />
      <Fridges />
    </Fragment>
  );
}
