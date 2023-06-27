import { render, screen } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import App from './App';

test('renders learn react link', () => {
  console.log('Rendering App component in test:', App);
  
  render(
    <BrowserRouter>
      <App />
    </BrowserRouter>
    );
  
  const linkElement = screen.getByTestId('learn-react-link');
  expect(linkElement).toBeInTheDocument();
});
