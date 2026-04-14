import React, { useEffect, useState } from 'react';

function App() {
  const [networks, setNetworks] = useState([]);
  const [selectedSSID, setSelectedSSID] = useState('');
  const [password, setPassword] = useState('');

  useEffect(() => {
    fetch('http://localhost:5000/scan')
      .then(res => res.json())
      .then(data => setNetworks(data));
  }, []);

  const handleGetPassword = (ssid) => {
    fetch(`http://localhost:5000/get_password/${ssid}`)
      .then(res => res.json())
      .then(data => {
        setSelectedSSID(ssid);
        setPassword(data.password);
      });
  };

  return (
    <div className="App">
      <h1>WiFi Scanner</h1>
      <table>
        <thead>
          <tr>
            <th>SSID</th>
            <th>Signal</th>
            <th>Security</th>
            <th>Aksi</th>
          </tr>
        </thead>
        <tbody>
          {networks.map((net, idx) => (
            <tr key={idx}>
              <td>{net.SSID}</td>
              <td>{net.Signal}</td>
              <td>{net.Security || '-'}</td>
              <td>
                <button onClick={() => handleGetPassword(net.SSID)}>Lihat Password</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {selectedSSID && (
        <div className="password-box">
          <h2>Password untuk {selectedSSID}</h2>
          <p>{password || 'Tidak dapat ditemukan'}</p>
        </div>
      )}
    </div>
  );
}

export default App;