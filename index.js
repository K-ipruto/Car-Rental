// (API Calls)
import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export const signup = async (username, password) => {
  const response = await axios.post(`${API_URL}/signup`, { username, password });
  return response.data;
};

export const login = async (username, password) => {
  const response = await axios.post(`${API_URL}/login`, { username, password });
  return response.data;
};

export const getCars = async () => {
  const response = await axios.get(`${API_URL}/cars`);
  return response.data;
};

export const reserveCar = async (carId, token) => {
  const response = await axios.post(`${API_URL}/reserve`, { car_id: carId }, {
    headers: { Authorization: `Bearer ${token}` }
  });
  return response.data;
};
// (Display Cars)
import React, { useState, useEffect } from 'react';
import { getCars } from '../api';

const CarList = () => {
  const [cars, setCars] = useState([]);
  useEffect(() => { getCars().then(setCars); }, []);

  return (
    <div>
      <h2>Available Cars</h2>
      <ul>
        {cars.map(car => (
          <li key={car.id}>
            {car.model} - ${car.price_per_day}/day
            <button>Reserve</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CarList;
// (Main App)
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import CarList from './components/CarList';
import Login from './components/Login';
import Signup from './components/Signup';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/login" component={Login} />
        <Route path="/signup" component={Signup} />
        <Route path="/" exact component={CarList} />
      </Switch>
    </Router>
  );
}

export default App;
// (Login Component)
import React, { useState } from 'react';
import { login } from '../api';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const data = await login(username, password);
      localStorage.setItem('token', data.access_token);
      window.location.href = '/';
    } catch (err) {
      setError('Invalid credentials');
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Username" value={username} onChange={e => setUsername(e.target.value)} />
        <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
        <button type="submit">Login</button>
      </form>
      {error && <p>{error}</p>}
    </div>
  );
};

export default Login;
