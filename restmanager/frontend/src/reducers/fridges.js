import {
  GET_FRIDGES,
  DELETE_FRIDGE,
  ADD_FRIDGE,
  BOT_NOTIFY
} from "../actions/types.js";

const initialState = {
  fridges: []
};

/*
Switch statements to determine what action.type client does

*/

export default function(state = initialState, action) {
  switch (action.type) {
    case GET_FRIDGES:
      return {
        ...state,
        fridges: action.payload
      };
    case DELETE_FRIDGE:
      return {
        ...state,
        fridges: state.fridges.filter(fridge => fridge.id !== action.payload)
      };
    case ADD_FRIDGE:
      return {
        ...state,
        fridge: [...state.fridges, action.payload]
      };
    case BOT_NOTIFY:
      return {
        ...state,
        fridge: action.payload
      };

    default:
      return state;
  }
}
