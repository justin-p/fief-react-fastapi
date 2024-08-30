import { FiefAuthProvider } from '@fief/fief/react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import Callback from './Callback';
import Public from './Public';
import Private from './Private';
import Header from './Header';
import RequireAuth from './RequireAuth';

function App() {
  return (
    <BrowserRouter>
      <FiefAuthProvider 
        baseURL="https://fief.local.test"
        clientId="fK7Qs2Lp9Xm4Nh6Bv3Jt8Ry5Gz1Wd7C"
      >
        <div className="App">
          <h1>Random Pet Name Generator</h1>
          <Header />
          <Routes>
            <Route path="/" element={<Public />} />
            <Route path="/private" element={<RequireAuth><Private /></RequireAuth>} />
            <Route path="/callback" element={<Callback />} />
          </Routes>
        </div>
      </FiefAuthProvider>
    </BrowserRouter>
  );
}

export default App;