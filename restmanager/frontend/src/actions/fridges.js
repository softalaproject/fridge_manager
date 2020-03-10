import axios from "axios";

import { GET_FRIDGES, DELETE_FRIDGE, ADD_FRIDGE, BOT_NOTIFY } from "./types";

// get fridges
export const getFridges = () => dispatch => {
  axios
    .get("/api/fridges/")
    .then(res => {
      dispatch({
        type: GET_FRIDGES,
        payload: res.data
      });
    })
    .catch(err => console.log(err));
};

// delete fridges
export const deleteFridge = id => dispatch => {
  axios
    .delete(`/api/fridges/${id}/`)
    .then(res => {
      dispatch({
        type: DELETE_FRIDGE,
        payload: id
      });
    })
    .catch(err => console.log(err));
};

// add fridge
export const addFridge = fridge => dispatch => {
  axios
    .post("/api/fridges/", fridge)
    .then(res => {
      dispatch({
        type: ADD_FRIDGE,
        payload: res.data
      });
    })
    .catch(err => console.log(err));
};
//general notify function to #general in test_slack_env
export function botNotification() {
  axios.get("/api/beer").then(function(response) {
    console.log(response);
  });
}

export const botNotify = id => dispatch => {
  axios
    .get(`/api/fridges/${id}/`)
    .then(res => {
      dispatch({
        type: BOT_NOTIFY,
        payload: id
      });
    })
    .catch(err => console.log(err));
};
