import axios from 'axios';
import store from '../store';
import thunk from 'redux-thunk';
import * as actions from '../actions/fridges';
import * as types from '../actions/types';
import fridgesMock from '../assests/fridges-mock';

const middlewares = [thunk];
jest.mock('store');
jest.mock('axios');

// test to redux create action for fridges-mock with fetch-mock
describe('async actions & api fetch', () => {
    afterEach(() => {
      jest.clearAllMocks()
    })

    it('should create action for fridges', async () => {
        axios.get.mockImplementationOnce(fridgesMock, () => {
          
        });
        const expectedActions = [
          { 
            type: types.GET_FRIDGES, 
            body: { fridgesMock } 
          }
        ];
      
          return store.dispatch(actions.GET_FRIDGES()).then(() => {
            // return of async actions
            await expect(store.getActions()).toEqual(expectedActions);
          });
    });
});