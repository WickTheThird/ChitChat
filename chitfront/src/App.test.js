import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  console.log('Rendering App component in test:', App);
  render(<App />);
  const linkElement = screen.getByTestId('learn-react-link');
  expect(linkElement).toBeInTheDocument();
});
