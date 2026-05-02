import React, { useState, useEffect, useCallback } from 'react';
import axios from 'axios';
import { Sliders, RefreshCw, WifiOff } from 'lucide-react';
import {
  AreaChart, Area, XAxis, YAxis, Tooltip, ResponsiveContainer,
  CartesianGrid, ReferenceLine
} from 'recharts';

const API_URL = '/api';

const DEFAULTS = {
  CreditScore: 600, Geography: 'France', Gender: 'Male',
  Age: 45, Tenure: 3, Balance: 100000,
  NumOfProducts: 1, HasCrCard: 1, IsActiveMember: 0, EstimatedSalary: 90000,
};

const SliderField = ({ label, name, value, min, max, step = 1, format, onChange }) => (
  <div className="space-y-2">
    <div className="flex justify-between items-center">
      <label className="text-xs font-semibold text-gray-400 uppercase tracking-wider">{label}</label>
      <span className="text-sm font-bold text-indigo-300 tabular-nums">{format ? format(value) : value}</span>
    </div>
    <div className="relative">
      <input
        type="range"
        name={name}
        min={min}
        max={max}
        step={step}
        value={value}
        onChange={onChange}
        className="w-full h-1.5 bg-gray-700 rounded-full appearance-none cursor-pointer accent-indigo-500"
        style={{
          background: `linear-gradient(to right, #6366f1 0%, #6366f1 ${((value - min) / (max - min)) * 100}%, #334155 ${((value - min) / (max - min)) * 100}%, #334155 100%)`
        }}
      />
    </div>
    <div className="flex justify-between text-[10px] text-gray-600">
      <span>{format ? format(min) : min}</span>
      <span>{format ? format(max) : max}</span>
    </div>
  </div>
);

const ToggleButton = ({ label, active, onClick, activeClass }) => (
  <button
    type="button"
    onClick={onClick}
    className={`flex-1 py-2.5 px-3 rounded-xl text-xs font-semibold transition-all border ${
      active
        ? activeClass
        : 'bg-gray-800/80 text-gray-500 border-gray-700 hover:bg-gray-700/80 hover:text-gray-300'
    }`}
  >
    {label} {active ? '✓' : ''}
  </button>
);

export default function Simulator() {
  const [baseData,       setBaseData]       = useState(DEFAULTS);
  const [currentResult,  setCurrentResult]  = useState(null);
  const [simulationData, setSimulationData] = useState([]);
  const [simVar,         setSimVar]         = useState('Balance');
  const [loading,        setLoading]        = useState(false);
  const [error,          setError]          = useState(null);

  const SIM_VARS = {
    Balance:     { label: 'Account Balance', range: [0, 250000], step: 25000, fmt: (v) => `$${(v/1000).toFixed(0)}k` },
    Age:         { label: 'Age',             range: [18, 80],    step: 5,     fmt: (v) => `${v}yr` },
    CreditScore: { label: 'Credit Score',    range: [300, 850],  step: 50,    fmt: (v) => `${v}` },
  };

  const runSimulation = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const currentRes = await axios.post(`${API_URL}/predict`, baseData);
      setCurrentResult(currentRes.data);

      const cfg    = SIM_VARS[simVar];
      const values = [];
      for (let v = cfg.range[0]; v <= cfg.range[1]; v += cfg.step) values.push(v);

      const promises = values.map((v) => axios.post(`${API_URL}/predict`, { ...baseData, [simVar]: v }));
      const results  = await Promise.all(promises);

      setSimulationData(values.map((v, i) => ({
        [simVar]:   v,
        ChurnRisk:  parseFloat((results[i].data.churn_probability * 100).toFixed(2)),
        RiskLevel:  results[i].data.risk_level,
      })));
    } catch (err) {
      setError('Backend unreachable. Ensure FastAPI is running on port 8000.');
    } finally {
      setLoading(false);
    }
  }, [baseData, simVar]);

  // debounce to avoid hammering API on every slider tick
  useEffect(() => {
    const timer = setTimeout(runSimulation, 300);
    return () => clearTimeout(timer);
  }, [runSimulation]);

  const handleSlider = (e) => {
    const { name, value } = e.target;
    setBaseData((prev) => ({ ...prev, [name]: parseFloat(value) }));
  };

  const handleToggle = (name) => {
    setBaseData((prev) => ({ ...prev, [name]: prev[name] === 1 ? 0 : 1 }));
  };

  const handleGeoGender = (e) => {
    const { name, value } = e.target;
    setBaseData((prev) => ({ ...prev, [name]: value }));
  };

  const riskColor = currentResult?.risk_level === 'High'
    ? 'text-rose-400' : currentResult?.risk_level === 'Medium'
    ? 'text-amber-400' : 'text-emerald-400';

  const riskBg = currentResult?.risk_level === 'High'
    ? 'bg-rose-500/15 border-rose-500/30' : currentResult?.risk_level === 'Medium'
    ? 'bg-amber-500/15 border-amber-500/30' : 'bg-emerald-500/15 border-emerald-500/30';

  const tooltipStyle = { backgroundColor: '#1e293b', border: '1px solid #334155', borderRadius: '10px', color: '#f1f5f9', fontSize: 12 };

  return (
    <div className="space-y-6 pb-10">
      <header className="mb-8">
        <h2 className="text-3xl font-black text-white tracking-tight">What-If Simulator</h2>
        <p className="text-gray-400 mt-1 text-sm">Adjust customer parameters and watch churn risk update in real-time</p>
      </header>

      {error && (
        <div className="glass-panel border border-rose-500/30 bg-rose-500/10 px-5 py-4 rounded-xl flex items-center gap-3 text-rose-400 text-sm">
          <WifiOff className="w-5 h-5 flex-shrink-0" /> {error}
        </div>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">

        {/* ── Controls ── */}
        <div className="glass-panel p-6 space-y-6">
          <div className="flex items-center gap-2 pb-4 border-b border-gray-700/50">
            <div className="p-1.5 bg-white/10 rounded-lg border border-white/20">
              <Sliders className="w-4 h-4 text-indigo-400" />
            </div>
            <h3 className="text-sm font-semibold text-white uppercase tracking-wider">Adjust Variables</h3>
          </div>

          {/* Geography & Gender */}
          <div className="grid grid-cols-2 gap-3">
            {[
              { name: 'Geography', opts: ['France', 'Germany', 'Spain'] },
              { name: 'Gender',    opts: ['Male', 'Female'] },
            ].map(({ name, opts }) => (
              <div key={name} className="space-y-1.5">
                <label className="text-[10px] font-semibold text-gray-400 uppercase tracking-wider">{name}</label>
                <select
                  name={name}
                  value={baseData[name]}
                  onChange={handleGeoGender}
                  className="w-full bg-gray-900/60 border border-gray-700/60 text-white rounded-xl px-3 py-2 text-xs focus:ring-2 focus:ring-white/50 outline-none"
                >
                  {opts.map((o) => <option key={o}>{o}</option>)}
                </select>
              </div>
            ))}
          </div>

          {/* Sliders */}
          <SliderField label="Age"           name="Age"         value={baseData.Age}         min={18}  max={80}    onChange={handleSlider} />
          <SliderField label="Balance"       name="Balance"     value={baseData.Balance}     min={0}   max={250000} step={5000} format={(v) => `$${(v/1000).toFixed(0)}k`} onChange={handleSlider} />
          <SliderField label="Credit Score"  name="CreditScore" value={baseData.CreditScore} min={300} max={850}   onChange={handleSlider} />
          <SliderField label="Tenure (yrs)"  name="Tenure"      value={baseData.Tenure}      min={0}   max={10}    onChange={handleSlider} />
          <SliderField label="Num Products"  name="NumOfProducts" value={baseData.NumOfProducts} min={1} max={4}  onChange={handleSlider} />

          {/* Toggle buttons */}
          <div className="flex gap-2 pt-2 border-t border-gray-700/50">
            <ToggleButton
              label="Active Member"
              active={!!baseData.IsActiveMember}
              onClick={() => handleToggle('IsActiveMember')}
              activeClass="bg-emerald-500/15 text-emerald-400 border-emerald-500/40"
            />
            <ToggleButton
              label="Credit Card"
              active={!!baseData.HasCrCard}
              onClick={() => handleToggle('HasCrCard')}
              activeClass="bg-blue-500/15 text-blue-400 border-blue-500/40"
            />
          </div>
        </div>

        {/* ── Right Panel ── */}
        <div className="lg:col-span-2 space-y-5">

          {/* Current Risk Score */}
          <div className="glass-panel p-6 flex items-center justify-between">
            <div>
              <p className="text-xs text-gray-400 uppercase tracking-widest font-semibold mb-1">Live Churn Risk</p>
              <div className={`text-5xl font-black tabular-nums ${riskColor} transition-all duration-500`}>
                {loading
                  ? <span className="text-gray-600 animate-pulse text-4xl">–.–%</span>
                  : currentResult
                  ? `${(currentResult.churn_probability * 100).toFixed(1)}%`
                  : '–%'
                }
              </div>
            </div>
            <div className="flex flex-col items-end gap-3">
              {currentResult && (
                <div className={`px-4 py-2 rounded-full text-sm font-bold border ${riskBg} ${riskColor}`}>
                  {currentResult.risk_level} Risk
                </div>
              )}
              {loading && (
                <div className="flex items-center gap-1.5 text-xs text-gray-500">
                  <RefreshCw className="w-3 h-3 animate-spin" /> Updating…
                </div>
              )}
            </div>
          </div>

          {/* Simulation Variable Picker */}
          <div className="glass-panel p-6">
            <div className="flex items-center justify-between mb-5">
              <div>
                <h3 className="text-base font-semibold text-gray-200">Impact Simulation</h3>
                <p className="text-xs text-gray-500 mt-0.5">How churn risk changes as one variable sweeps its range</p>
              </div>
              <div className="flex gap-2">
                {Object.keys(SIM_VARS).map((key) => (
                  <button
                    key={key}
                    onClick={() => setSimVar(key)}
                    className={`px-3 py-1.5 rounded-lg text-xs font-semibold border transition-all ${
                      simVar === key
                        ? 'bg-white/10 text-white border-white/20'
                        : 'bg-gray-800/60 text-gray-500 border-gray-700 hover:text-gray-300'
                    }`}
                  >
                    {SIM_VARS[key].label}
                  </button>
                ))}
              </div>
            </div>

            <div className="h-72">
              <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={simulationData} margin={{ top: 5, right: 5, bottom: 5, left: 5 }}>
                  <defs>
                    <linearGradient id="colorRisk" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%"  stopColor="#8b5cf6" stopOpacity={0.35} />
                      <stop offset="95%" stopColor="#8b5cf6" stopOpacity={0} />
                    </linearGradient>
                  </defs>
                  <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
                  <XAxis
                    dataKey={simVar}
                    stroke="#64748b"
                    fontSize={11}
                    tickLine={false}
                    tickFormatter={SIM_VARS[simVar].fmt}
                  />
                  <YAxis
                    stroke="#64748b"
                    fontSize={11}
                    tickLine={false}
                    axisLine={false}
                    tickFormatter={(v) => `${v}%`}
                    domain={[0, 100]}
                  />
                  <ReferenceLine y={40} stroke="#f59e0b" strokeDasharray="4 4" strokeOpacity={0.5}
                    label={{ value: 'Med', fill: '#f59e0b', fontSize: 10, position: 'insideTopRight' }} />
                  <ReferenceLine y={70} stroke="#ef4444" strokeDasharray="4 4" strokeOpacity={0.5}
                    label={{ value: 'High', fill: '#ef4444', fontSize: 10, position: 'insideTopRight' }} />
                  <Tooltip
                    contentStyle={tooltipStyle}
                    formatter={(v) => [`${v}%`, 'Churn Risk']}
                    labelFormatter={(l) => `${SIM_VARS[simVar].label}: ${SIM_VARS[simVar].fmt(l)}`}
                  />
                  <Area
                    type="monotone"
                    dataKey="ChurnRisk"
                    stroke="#8b5cf6"
                    strokeWidth={3}
                    fillOpacity={1}
                    fill="url(#colorRisk)"
                    activeDot={{ r: 6, fill: '#8b5cf6', stroke: '#fff', strokeWidth: 2 }}
                  />
                </AreaChart>
              </ResponsiveContainer>
            </div>

            {/* Threshold legend */}
            <div className="flex gap-5 mt-4 pt-4 border-t border-gray-700/40">
              {[
                { color: 'bg-emerald-500', label: 'Low risk',    range: '< 40%' },
                { color: 'bg-amber-500',   label: 'Medium risk', range: '40–70%' },
                { color: 'bg-rose-500',    label: 'High risk',   range: '> 70%' },
              ].map(({ color, label, range }) => (
                <div key={label} className="flex items-center gap-2">
                  <span className={`w-2.5 h-2.5 rounded-full ${color}`} />
                  <span className="text-xs text-gray-400">{label} <span className="text-gray-600">({range})</span></span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
