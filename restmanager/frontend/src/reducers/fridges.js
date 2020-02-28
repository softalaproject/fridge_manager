import { GET_FRIDGES, DELETE_FRIDGE, ADD_FRIDGE } from "../actions/types.js";

const initialState = {
  fridges: []
};

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

    default:
      return state;
  }
}
