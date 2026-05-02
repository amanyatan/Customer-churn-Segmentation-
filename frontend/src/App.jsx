import React, { useState } from 'react';
import { BrowserRouter, Routes, Route, NavLink } from 'react-router-dom';
import { LayoutDashboard, Users, BrainCircuit, Activity, Menu, X } from 'lucide-react';
import Dashboard from './pages/Dashboard';
import Segmentation from './pages/Segmentation';
import Prediction from './pages/Prediction';
import Simulator from './pages/Simulator';

function App() {
  const [mobileOpen, setMobileOpen] = useState(false);

  const navItems = [
    { to: '/',          icon: <LayoutDashboard className="w-5 h-5" />, label: 'Overview' },
    { to: '/segments',  icon: <Users className="w-5 h-5" />,           label: 'Segmentation' },
    { to: '/predict',   icon: <BrainCircuit className="w-5 h-5" />,    label: 'Predict Churn' },
    { to: '/simulator', icon: <Activity className="w-5 h-5" />,        label: 'What-If Simulator' },
  ];

  const activeClass = 'bg-white/10 text-white border border-white/20 shadow-[0_0_15px_rgba(255,255,255,0.1)]';
  const inactiveClass = 'text-gray-400 hover:bg-white/5 hover:text-white';
  const linkBase = 'flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-200 font-medium text-sm';

  const Sidebar = () => (
    <aside className="w-64 glass-panel border-r border-gray-700/50 flex flex-col">
      {/* Logo */}
      <div className="p-6 border-b border-gray-700/40">
        <div className="flex items-center gap-2">
          <div className="p-2 bg-white/10 rounded-xl border border-white/20">
            <BrainCircuit className="w-5 h-5 text-white" />
          </div>
          <div>
            <h1 className="text-base font-bold text-white leading-tight">
              Churn Model Predictor
            </h1>
            <p className="text-[10px] text-gray-400 uppercase tracking-widest">AI Dashboard</p>
          </div>
        </div>
      </div>

      {/* Nav */}
      <nav className="flex-1 px-3 py-4 space-y-1">
        {navItems.map(({ to, icon, label }) => (
          <NavLink
            key={to}
            to={to}
            end={to === '/'}
            className={({ isActive }) => `${linkBase} ${isActive ? activeClass : inactiveClass}`}
            onClick={() => setMobileOpen(false)}
          >
            {icon}
            {label}
          </NavLink>
        ))}
      </nav>

      {/* Footer */}
      <div className="p-4 border-t border-gray-700/40">
        <p className="text-xs text-gray-600 text-center">European Bank Dataset · XGBoost</p>
      </div>
    </aside>
  );

  return (
    <BrowserRouter>
      <div className="flex h-screen bg-black text-white overflow-hidden font-sans relative">

        {/* Desktop Sidebar */}
        <div className="hidden md:flex m-4">
          <Sidebar />
        </div>

        {/* Mobile hamburger */}
        <button
          className="md:hidden fixed top-4 left-4 z-50 p-2 glass-panel rounded-xl text-gray-300"
          onClick={() => setMobileOpen(!mobileOpen)}
        >
          {mobileOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
        </button>

        {/* Mobile sidebar overlay */}
        {mobileOpen && (
          <div className="md:hidden fixed inset-0 z-40 flex">
            <div className="w-64 m-4">
              <Sidebar />
            </div>
            <div className="flex-1 bg-black/60 backdrop-blur-sm" onClick={() => setMobileOpen(false)} />
          </div>
        )}

        {/* Background glow removed for B&W theme */}
        <div className="absolute top-0 left-1/3 w-[600px] h-[400px] bg-white/5 blur-[140px] rounded-full pointer-events-none" />
        <div className="absolute bottom-0 right-1/4 w-[400px] h-[300px] bg-white/5 blur-[120px] rounded-full pointer-events-none" />

        {/* Main Content */}
        <main className="flex-1 overflow-y-auto relative z-10">
          <div className="p-4 pt-16 md:pt-4 md:p-8 max-w-7xl mx-auto">
            <Routes>
              <Route path="/"          element={<Dashboard />} />
              <Route path="/segments"  element={<Segmentation />} />
              <Route path="/predict"   element={<Prediction />} />
              <Route path="/simulator" element={<Simulator />} />
            </Routes>
          </div>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
