import React from 'react';
import Header from '../components/layout/Header';
import {create, act} from 'react-test-renderer';
import fridges from '../assests/fridges-mock';

/*
let container = null;
beforeEach(() => {
  // setup a DOM element as a render target
});

afterEach(() => {
  // cleanup on exiting
  container.remove();
  container = null;
});
*/

it('dashboard renders correctly', () => {
    let layout = null;
    act(() => {
        layout = create(<Header />);
    });
    expect(layout.toJSON()).toMatchSnapshot();
    layout.unmount();
});