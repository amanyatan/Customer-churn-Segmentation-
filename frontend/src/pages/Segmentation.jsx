import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
  BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer,
  Cell, LineChart, Line, CartesianGrid, Legend
} from 'recharts';
import { RefreshCw, WifiOff } from 'lucide-react';

const API_URL = '/api';
const COLORS  = ['#8b5cf6', '#3b82f6', '#ec4899', '#f59e0b', '#10b981'];

const ChartCard = ({ title, sub, children }) => (
  <div className="glass-panel p-6">
    <h3 className="text-base font-semibold text-gray-200 mb-1">{title}</h3>
    {sub && <p className="text-xs text-gray-500 mb-5">{sub}</p>}
    {children}
  </div>
);

export default function Segmentation() {
  const [segments, setSegments] = useState(null);
  const [loading,  setLoading]  = useState(true);
  const [error,    setError]    = useState(null);

  const fetchData = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await axios.get(`${API_URL}/segments`);
      setSegments(res.data);
    } catch (err) {
      setError('Cannot reach backend. Is the FastAPI server running on port 8000?');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { fetchData(); }, []);

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh] gap-4">
        <div className="relative">
          <div className="w-16 h-16 rounded-full border-2 border-indigo-500/20 animate-ping absolute inset-0" />
          <div className="w-16 h-16 rounded-full border-t-2 border-indigo-500 animate-spin" />
        </div>
        <p className="text-gray-400 text-sm animate-pulse">Loading segmentation data…</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh] gap-4 text-center">
        <div className="p-4 bg-rose-500/10 rounded-full border border-rose-500/30">
          <WifiOff className="w-10 h-10 text-rose-400" />
        </div>
        <p className="text-gray-400 text-sm max-w-md">{error}</p>
        <button onClick={fetchData}
          className="flex items-center gap-2 px-5 py-2.5 bg-white/10 hover:bg-white/20 border border-white/20 rounded-xl text-white text-sm font-medium transition-all">
          <RefreshCw className="w-4 h-4" /> Retry
        </button>
      </div>
    );
  }

  const tooltipStyle = { backgroundColor: '#1e293b', border: '1px solid #334155', borderRadius: '10px', color: '#f1f5f9', fontSize: 12 };

  return (
    <div className="space-y-6 pb-10">
      <header className="mb-8">
        <h2 className="text-3xl font-black text-white tracking-tight">Segmentation Analytics</h2>
        <p className="text-gray-400 mt-1 text-sm">Customer demographics, behaviour patterns, and churn drivers</p>
      </header>

      <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">

        {/* Balance vs Churn */}
        <ChartCard title="Churn by Account Balance" sub="Churn rate and customer count per balance tier">
          <div className="h-72">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={segments.balance}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
                <XAxis dataKey="BalanceSegment" stroke="#64748b" fontSize={11} tickLine={false} />
                <YAxis yAxisId="left"  stroke="#64748b" fontSize={11} tickLine={false} axisLine={false}
                  tickFormatter={(v) => `${(v * 100).toFixed(0)}%`} />
                <YAxis yAxisId="right" orientation="right" stroke="#334155" fontSize={11} tickLine={false} axisLine={false} />
                <Tooltip contentStyle={tooltipStyle}
                  formatter={(v, name) => name === 'ChurnRate' ? [`${(v * 100).toFixed(2)}%`, 'Churn Rate'] : [v.toLocaleString(), 'Customers']} />
                <Legend formatter={(v) => <span style={{ color: '#94a3b8', fontSize: 11 }}>{v === 'ChurnRate' ? 'Churn Rate' : 'Total Customers'}</span>} />
                <Bar yAxisId="left"  dataKey="ChurnRate"      name="ChurnRate"      fill="#8b5cf6" radius={[5, 5, 0, 0]} />
                <Bar yAxisId="right" dataKey="TotalCustomers" name="TotalCustomers" fill="#334155" radius={[5, 5, 0, 0]} opacity={0.6} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </ChartCard>

        {/* Credit Score vs Churn */}
        <ChartCard title="Churn by Credit Score Band" sub="Higher credit scores don't always mean lower churn">
          <div className="h-72">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={segments.credit_score} layout="vertical" barSize={22}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" horizontal={false} />
                <XAxis type="number" stroke="#64748b" fontSize={11} tickLine={false} axisLine={false}
                  tickFormatter={(v) => `${(v * 100).toFixed(0)}%`} />
                <YAxis dataKey="CreditScoreBand" type="category" stroke="#64748b" fontSize={11} tickLine={false} width={78} />
                <Tooltip contentStyle={tooltipStyle}
                  formatter={(v) => [`${(v * 100).toFixed(2)}%`, 'Churn Rate']} />
                <Bar dataKey="ChurnRate" radius={[0, 5, 5, 0]}>
                  {segments.credit_score.map((_, i) => (
                    <Cell key={i} fill={COLORS[i % COLORS.length]} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </ChartCard>

        {/* Age Group Churn Rate */}
        <ChartCard title="Churn Rate by Age Group" sub="51–60 age bracket carries the highest churn risk">
          <div className="h-72">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={segments.age} barSize={36}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
                <XAxis dataKey="AgeGroup" stroke="#64748b" fontSize={12} tickLine={false} />
                <YAxis stroke="#64748b" fontSize={11} tickLine={false} axisLine={false}
                  tickFormatter={(v) => `${(v * 100).toFixed(0)}%`} />
                <Tooltip contentStyle={tooltipStyle}
                  formatter={(v) => [`${(v * 100).toFixed(2)}%`, 'Churn Rate']} />
                <Bar dataKey="ChurnRate" radius={[6, 6, 0, 0]}>
                  {segments.age.map((_, i) => (
                    <Cell key={i} fill={COLORS[i % COLORS.length]} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </ChartCard>

        {/* Tenure Line Chart */}
        <ChartCard title="Tenure vs Churn Rate" sub="Churn risk across years of customer tenure (0–10)">
          <div className="h-72">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={segments.tenure}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                <XAxis dataKey="Tenure" stroke="#64748b" fontSize={12} tickLine={false}
                  label={{ value: 'Years', position: 'insideRight', offset: -4, fill: '#64748b', fontSize: 11 }} />
                <YAxis stroke="#64748b" fontSize={11} tickLine={false} axisLine={false}
                  tickFormatter={(v) => `${(v * 100).toFixed(0)}%`} />
                <Tooltip contentStyle={tooltipStyle}
                  formatter={(v) => [`${(v * 100).toFixed(2)}%`, 'Churn Rate']} />
                <Line
                  type="monotone"
                  dataKey="ChurnRate"
                  stroke="#3b82f6"
                  strokeWidth={3}
                  dot={{ r: 4, fill: '#3b82f6', strokeWidth: 2, stroke: '#0a0f1e' }}
                  activeDot={{ r: 6, fill: '#60a5fa' }}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </ChartCard>

      </div>
    </div>
  );
}
