import './App.css';
import Home from './pages/Home';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import SignUp from './pages/SignUp';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />} /> {/* For Home page */}
        <Route path='/sign-up' element={<SignUp />} /> {/* For Signup page */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
