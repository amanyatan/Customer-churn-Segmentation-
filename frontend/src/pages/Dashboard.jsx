import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
  Users, AlertTriangle, Activity, TrendingUp,
  TrendingDown, RefreshCw, Wifi, WifiOff
} from 'lucide-react';
import {
  BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer,
  Cell, PieChart, Pie, Legend
} from 'recharts';

const API_URL = '/api';

const COLORS = ['#3b82f6', '#8b5cf6', '#ec4899', '#f43f5e', '#10b981'];

const KPICard = ({ label, value, icon: Icon, color, sub }) => (
  <div className={`glass-panel p-6 border-t-4 ${color} hover:-translate-y-1 transition-transform duration-300 group`}>
    <div className="flex justify-between items-start">
      <div className="flex-1">
        <p className="text-gray-400 text-xs font-semibold uppercase tracking-widest">{label}</p>
        <h3 className="text-3xl font-black text-white mt-2 tabular-nums">{value}</h3>
        {sub && <p className="text-xs text-gray-500 mt-1">{sub}</p>}
      </div>
      <div className={`p-3 rounded-xl bg-white/5 border border-white/10 group-hover:scale-110 transition-transform duration-300`}>
        <Icon className="w-6 h-6 text-gray-300" />
      </div>
    </div>
  </div>
);

export default function Dashboard() {
  const [metrics, setMetrics]   = useState(null);
  const [segments, setSegments] = useState(null);
  const [loading, setLoading]   = useState(true);
  const [error, setError]       = useState(null);

  const fetchData = async () => {
    setLoading(true);
    setError(null);
    try {
      const [metricsRes, segmentsRes] = await Promise.all([
        axios.get(`${API_URL}/metrics`),
        axios.get(`${API_URL}/segments`),
      ]);
      setMetrics(metricsRes.data);
      setSegments(segmentsRes.data);
    } catch (err) {
      setError('Cannot reach the backend API. Make sure the FastAPI server is running on port 8000.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { fetchData(); }, []);

  if (loading) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh] gap-4">
        <div className="relative">
          <div className="w-16 h-16 rounded-full border-2 border-blue-500/20 animate-ping absolute inset-0" />
          <div className="w-16 h-16 rounded-full border-t-2 border-blue-500 animate-spin" />
        </div>
        <p className="text-gray-400 text-sm animate-pulse">Loading dashboard data…</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[60vh] gap-4 text-center">
        <div className="p-4 bg-rose-500/10 rounded-full border border-rose-500/30">
          <WifiOff className="w-10 h-10 text-rose-400" />
        </div>
        <div>
          <h3 className="text-lg font-semibold text-rose-400 mb-2">Backend Offline</h3>
          <p className="text-gray-400 text-sm max-w-md">{error}</p>
        </div>
        <button
          onClick={fetchData}
          className="flex items-center gap-2 px-5 py-2.5 bg-blue-600/20 hover:bg-blue-600/30 border border-blue-500/30 rounded-xl text-blue-400 text-sm font-medium transition-all"
        >
          <RefreshCw className="w-4 h-4" /> Retry
        </button>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <header className="mb-8">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-3xl font-black text-white tracking-tight">Dashboard Overview</h2>
            <p className="text-gray-400 mt-1 text-sm">European banking customer churn intelligence</p>
          </div>
          <button
            onClick={fetchData}
            className="flex items-center gap-2 px-4 py-2 glass-panel hover:bg-gray-700/50 rounded-xl text-gray-300 text-sm transition-all"
          >
            <RefreshCw className="w-4 h-4" /> Refresh
          </button>
        </div>
      </header>

      {/* KPI Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
        <KPICard
          label="Total Customers"
          value={metrics.total_customers.toLocaleString()}
          icon={Users}
          color="border-t-blue-500"
          sub="European bank dataset"
        />
        <KPICard
          label="Overall Churn Rate"
          value={`${metrics.overall_churn_rate}%`}
          icon={AlertTriangle}
          color="border-t-rose-500"
          sub="Customers who exited"
        />
        <KPICard
          label="Active Members"
          value={metrics.active_users.toLocaleString()}
          icon={Activity}
          color="border-t-emerald-500"
          sub={`${((metrics.active_users / metrics.total_customers) * 100).toFixed(1)}% of total`}
        />
      </div>

      {/* Charts */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-2">
        {/* Geography Bar */}
        <div className="glass-panel p-6">
          <h3 className="text-base font-semibold text-gray-200 mb-1">Churn Rate by Geography</h3>
          <p className="text-xs text-gray-500 mb-6">% of customers who exited per region</p>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={segments.geography} barSize={40}>
                <XAxis dataKey="Geography" stroke="#64748b" fontSize={12} tickLine={false} />
                <YAxis stroke="#64748b" fontSize={11} tickLine={false} axisLine={false}
                  tickFormatter={(v) => `${(v * 100).toFixed(0)}%`} />
                <Tooltip
                  cursor={{ fill: 'rgba(255,255,255,0.03)' }}
                  contentStyle={{ backgroundColor: '#1e293b', border: '1px solid #334155', borderRadius: '10px', color: '#f1f5f9', fontSize: 12 }}
                  formatter={(v) => [`${(v * 100).toFixed(2)}%`, 'Churn Rate']}
                />
                <Bar dataKey="ChurnRate" radius={[6, 6, 0, 0]}>
                  {segments.geography.map((_, i) => (
                    <Cell key={i} fill={COLORS[i % COLORS.length]} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Age Pie */}
        <div className="glass-panel p-6">
          <h3 className="text-base font-semibold text-gray-200 mb-1">Customers by Age Group</h3>
          <p className="text-xs text-gray-500 mb-4">Distribution across demographic segments</p>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={segments.age}
                  dataKey="TotalCustomers"
                  nameKey="AgeGroup"
                  cx="50%"
                  cy="50%"
                  outerRadius={90}
                  innerRadius={55}
                  paddingAngle={3}
                >
                  {segments.age.map((_, i) => (
                    <Cell key={i} fill={COLORS[i % COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip
                  contentStyle={{ backgroundColor: '#1e293b', border: '1px solid #334155', borderRadius: '10px', color: '#f1f5f9', fontSize: 12 }}
                />
                <Legend
                  iconType="circle"
                  iconSize={8}
                  formatter={(val) => <span style={{ color: '#94a3b8', fontSize: 11 }}>{val}</span>}
                />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* Insight Strip */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mt-2">
        {segments.geography.map((g, i) => {
          const rate = (g.ChurnRate * 100).toFixed(1);
          const isHigh = g.ChurnRate > 0.25;
          return (
            <div key={g.Geography} className="glass-panel px-5 py-4 flex items-center justify-between">
              <div>
                <p className="text-xs text-gray-500 uppercase tracking-wide">{g.Geography}</p>
                <p className="text-lg font-bold text-white mt-0.5">{rate}% churn</p>
                <p className="text-xs text-gray-500">{g.TotalCustomers.toLocaleString()} customers</p>
              </div>
              <div className={`p-2 rounded-xl ${isHigh ? 'bg-rose-500/15 text-rose-400' : 'bg-emerald-500/15 text-emerald-400'}`}>
                {isHigh ? <TrendingUp className="w-5 h-5" /> : <TrendingDown className="w-5 h-5" />}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
