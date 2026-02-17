import React, { useState } from "react";
import axios from "axios";

function App() {
  const [ticker, setTicker] = useState("SPY");
  const [data, setData] = useState(null);

  const fetchData = async () => {
    try {
      const res = await axios.get(`https://faro-quant-system.vercel.app/analisis/${ticker}`);
      setData(res.data);
    } catch (err) {
      alert("Error al obtener datos: " + err.message);
    }
  };

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">FARO Quant Dashboard</h1>
      <input
        className="border p-2 mr-2"
        type="text"
        value={ticker}
        onChange={(e) => setTicker(e.target.value.toUpperCase())}
      />
      <button className="bg-blue-500 text-white px-4 py-2" onClick={fetchData}>
        Analizar
      </button>

      {data && (
        <div className="mt-6 p-4 border rounded">
          <h2 className="font-bold">{data.faro_status} ({data.faro_score})</h2>
          <p className={`mt-2 ${data.color_type === "success" ? "text-green-600" : data.color_type === "warning" ? "text-yellow-600" : "text-red-600"}`}>
            {data.signal}
          </p>
          <h3 className="mt-4 font-semibold">Últimos 30 precios:</h3>
          <ul className="mt-2">
            {data.history.map((h) => (
              <li key={h.date}>{h.date}: {h.price}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
Añadir App.js para consumir API FARO
