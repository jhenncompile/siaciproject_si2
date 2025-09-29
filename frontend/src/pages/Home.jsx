import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../api/client";
import "./Home.css";

function StatusDot({ ok }) {
  const color = ok ? "#22c55e" : "#ef4444";
  return (
    <span
      style={{
        display: "inline-block",
        width: 10,
        height: 10,
        borderRadius: "50%",
        background: color,
        marginRight: 6,
      }}
    />
  );
}

export default function Home() {
  const [health, setHealth] = useState(null);

  useEffect(() => {
    api
      .get("/health/")
      .then((r) => setHealth(r.data))
      .catch(() =>
        setHealth({ status: "degraded", dependencies: { postgres: "error" } })
      );
  }, []);

  const ok = health?.status === "ok";

  return (
    <div className="home-container">
      {/* Header con logo */}
      <div className="home-header">
        <div className="logo-container">
          <div className="logo-wrapper">
            {/* Aquí va tu logo - reemplaza el div por tu imagen */}
            <div className="logo-image">
              <img 
                src="/images/logo-siaci.png" 
                alt="SIACI Logo" 
                className="logo-img"
                onError={(e) => {
                  e.target.style.display = 'none';
                  e.target.nextSibling.style.display = 'flex';
                }}
              />
              <div className="logo-fallback">
                🏢
              </div>
            </div>
            <div className="logo-text">
              <h1>SIACI</h1>
              <p>Sistema de Condominio</p>
            </div>
          </div>
        </div>
        
        <div className="welcome-section">
          <h2>Dashboard</h2>
          <p>Bienvenido al sistema SIACI</p>
        </div>
      </div>

      {/* Estado del Sistema */}
      <div className="status-section">
        <div className="status-card">
          <div className="status-header">
            <h3>Estado del Sistema</h3>
            <div className="status-indicator">
              <StatusDot ok={ok} />
              <span>{health ? health.status : "cargando..."}</span>
            </div>
          </div>
          <div className="status-details">
            <div className="status-item">
              <span className="status-label">Base de Datos:</span>
              <span className={`status-value ${ok ? 'success' : 'error'}`}>
                {health?.dependencies?.postgres ?? "..."}
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* Acciones Rápidas */}
      <div className="quick-actions-section">
        <h2>Acciones Rápidas</h2>
        <div className="actions-grid">
          <Link to="/personas" className="action-card">
            <div className="action-icon">👤</div>
            <div className="action-content">
              <h3>Personas</h3>
              <p>Gestionar residentes y propietarios</p>
            </div>
          </Link>
          <Link to="/viviendas" className="action-card">
            <div className="action-icon">🏢</div>
            <div className="action-content">
              <h3>Viviendas</h3>
              <p>Administrar unidades habitacionales</p>
            </div>
          </Link>
          <Link to="/contacto" className="action-card">
            <div className="action-icon">📞</div>
            <div className="action-content">
              <h3>Contacto</h3>
              <p>Información de contacto y soporte</p>
            </div>
          </Link>
        </div>
      </div>
    </div>
  );
}