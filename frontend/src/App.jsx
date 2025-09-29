import { useEffect, useState } from "react";
import api from "./api/client";

export default function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    console.log("VITE_API_BASE =", import.meta.env.VITE_API_BASE); // 👈 consola
    api.get("/health/").then(r => setData(r.data)).catch(e => setData({ error: String(e) }));
  }, []);

  return (
    <div style={{ padding: 16 }}>
      <h2>Health (API)</h2>
      <div><b>BASE:</b> {import.meta.env.VITE_API_BASE}</div> {/* 👈 visible en pantalla */}
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
