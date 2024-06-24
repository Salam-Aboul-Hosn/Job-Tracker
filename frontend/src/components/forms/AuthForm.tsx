// src/AuthForm.tsx

import React, { useState, useEffect, FormEvent } from 'react';
import axios from 'axios';

interface AuthFormProps {}

const AuthForm: React.FC<AuthFormProps> = () => {
  const [email, setEmail] = useState<string>('');
  const [username, setUsername] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [csrfToken, setCsrfToken] = useState<string>('');

  useEffect(() => {
    const getCsrfToken = async () => {
      try {
        const response = await axios.get<{ csrfToken: string }>(
          'http://localhost:8000/api/csrf/'
        );
        setCsrfToken(response.data.csrfToken);
      } catch (error) {
        console.error('Error fetching CSRF token', error);
      }
    };
    getCsrfToken();
  }, []);
  console.log(csrfToken);
  const handleRegister = async (e: FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        'http://localhost:8000/api/register/',
        {
          email,
          username,
          password,
        },
        {
          headers: {
            'X-CSRFToken': csrfToken,
          },
        }
      );
      console.log(response.data);
    } catch (error) {
      console.error('Error during registration', error);
    }
  };

  const handleLogin = async (e: FormEvent) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        'http://localhost:8000/api/login/',
        {
          email,
          password,
        },
        {
          headers: {
            'X-CSRFToken': csrfToken,
          },
        }
      );
      console.log(response.data);
    } catch (error) {
      console.error('Error during login', error);
    }
  };

  return (
    <div>
      <h2>Register</h2>
      <form onSubmit={handleRegister}>
        <input
          type='email'
          placeholder='Email'
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type='text'
          placeholder='Username'
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <input
          type='password'
          placeholder='Password'
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type='submit'>Register</button>
      </form>

      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <input
          type='email'
          placeholder='Email'
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type='password'
          placeholder='Password'
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type='submit'>Login</button>
      </form>
    </div>
  );
};

export default AuthForm;
