import React, { useState } from 'react';
import axios from 'axios';
import {
  ShieldAlert, ShieldCheck, Activity, RotateCcw,
  User, MapPin, CreditCard, Briefcase, DollarSign
} from 'lucide-react';

const API_URL = '/api';

const fieldGroups = [
  {
    title: 'Personal Info',
    icon: User,
    fields: [
      { name: 'Geography',  label: 'Geography',  type: 'select', options: ['France', 'Germany', 'Spain'] },
      { name: 'Gender',     label: 'Gender',     type: 'select', options: ['Female', 'Male'] },
      { name: 'Age',        label: 'Age',        type: 'number', min: 18,  max: 100 },
    ],
  },
  {
    title: 'Financial Profile',
    icon: DollarSign,
    fields: [
      { name: 'CreditScore',     label: 'Credit Score',       type: 'number', min: 300, max: 850 },
      { name: 'Balance',         label: 'Account Balance ($)', type: 'number', min: 0,   step: 1000 },
      { name: 'EstimatedSalary', label: 'Estimated Salary ($)',type: 'number', min: 0,   step: 1000 },
    ],
  },
  {
    title: 'Banking Behaviour',
    icon: Briefcase,
    fields: [
      { name: 'Tenure',        label: 'Tenure (Years)',    type: 'number', min: 0, max: 20 },
      { name: 'NumOfProducts', label: 'No. of Products',   type: 'number', min: 1, max: 4 },
      { name: 'HasCrCard',     label: 'Has Credit Card',   type: 'select', options: ['1', '0'], labels: ['Yes', 'No'] },
      { name: 'IsActiveMember',label: 'Is Active Member',  type: 'select', options: ['1', '0'], labels: ['Yes', 'No'] },
    ],
  },
];

const DEFAULTS = {
  CreditScore: 650, Geography: 'France', Gender: 'Female',
  Age: 40, Tenure: 5, Balance: 60000, NumOfProducts: 2,
  HasCrCard: 1, IsActiveMember: 1, EstimatedSalary: 80000,
};

export default function Prediction() {
  const [formData, setFormData] = useState(DEFAULTS);
  const [result,   setResult]   = useState(null);
  const [loading,  setLoading]  = useState(false);
  const [apiError, setApiError] = useState(null);

  const handleChange = (e) => {
    const { name, value, type } = e.target;
    setFormData({ ...formData, [name]: type === 'number' ? parseFloat(value) : value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setApiError(null);
    setResult(null);
    try {
      const payload = {
        ...formData,
        HasCrCard:      parseInt(formData.HasCrCard),
        IsActiveMember: parseInt(formData.IsActiveMember),
      };
      const res = await axios.post(`${API_URL}/predict`, payload);
      setResult(res.data);
    } catch (err) {
      const msg = err.response?.data?.detail || 'Backend unreachable. Ensure FastAPI is running on port 8000.';
      setApiError(msg);
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setFormData(DEFAULTS);
    setResult(null);
    setApiError(null);
  };

  const riskColors = {
    High:   { bg: 'bg-rose-500/15',    text: 'text-rose-400',    border: 'border-rose-500/40',   bar: 'from-rose-500 to-red-600' },
    Medium: { bg: 'bg-amber-500/15',   text: 'text-amber-400',   border: 'border-amber-500/40',  bar: 'from-amber-400 to-orange-500' },
    Low:    { bg: 'bg-emerald-500/15', text: 'text-emerald-400', border: 'border-emerald-500/40',bar: 'from-emerald-400 to-green-500' },
  };

  return (
    <div className="space-y-6 pb-10">
      <header className="mb-8">
        <h2 className="text-3xl font-black text-white tracking-tight">Predict Churn Risk</h2>
        <p className="text-gray-400 mt-1 text-sm">Enter customer details to get an AI-powered churn probability score</p>
      </header>

      <div className="grid grid-cols-1 lg:grid-cols-5 gap-6 items-start">

        {/* ── Form ── */}
        <div className="lg:col-span-3 space-y-5">
          <form onSubmit={handleSubmit} className="space-y-5">
            {fieldGroups.map(({ title, icon: Icon, fields }) => (
              <div key={title} className="glass-panel p-6">
                <div className="flex items-center gap-2 mb-5 pb-4 border-b border-gray-700/50">
                  <div className="p-1.5 bg-blue-500/15 rounded-lg border border-blue-500/20">
                    <Icon className="w-4 h-4 text-blue-400" />
                  </div>
                  <h3 className="text-sm font-semibold text-gray-200 uppercase tracking-wider">{title}</h3>
                </div>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
                  {fields.map(({ name, label, type, options, labels, ...rest }) => (
                    <div key={name} className="space-y-1.5">
                      <label className="text-xs font-semibold text-gray-400 uppercase tracking-wider">{label}</label>
                      {type === 'select' ? (
                        <select
                          name={name}
                          value={formData[name]}
                          onChange={handleChange}
                          className="w-full bg-gray-900/60 border border-gray-700/60 text-white rounded-xl px-4 py-2.5 text-sm focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500/50 outline-none transition-all"
                        >
                          {options.map((opt, i) => (
                            <option key={opt} value={opt}>{labels ? labels[i] : opt}</option>
                          ))}
                        </select>
                      ) : (
                        <input
                          type="number"
                          name={name}
                          value={formData[name]}
                          onChange={handleChange}
                          {...rest}
                          className="w-full bg-gray-900/60 border border-gray-700/60 text-white rounded-xl px-4 py-2.5 text-sm focus:ring-2 focus:ring-blue-500/50 focus:border-blue-500/50 outline-none transition-all"
                        />
                      )}
                    </div>
                  ))}
                </div>
              </div>
            ))}

            {/* Error banner */}
            {apiError && (
              <div className="glass-panel border border-rose-500/40 bg-rose-500/10 px-5 py-3 rounded-xl text-rose-400 text-sm">
                ⚠️ {apiError}
              </div>
            )}

            {/* Buttons */}
            <div className="flex gap-3">
              <button
                type="submit"
                disabled={loading}
                className="flex-1 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 disabled:opacity-60 text-white font-semibold py-3 px-6 rounded-xl shadow-lg transition-all hover:-translate-y-0.5 flex justify-center items-center gap-2 text-sm"
              >
                {loading
                  ? <><div className="w-4 h-4 border-t-2 border-white rounded-full animate-spin" /> Analysing…</>
                  : <><Activity className="w-4 h-4" /> Analyse Risk Score</>
                }
              </button>
              <button
                type="button"
                onClick={handleReset}
                className="px-4 py-3 glass-panel hover:bg-gray-700/50 rounded-xl text-gray-400 transition-all"
                title="Reset to defaults"
              >
                <RotateCcw className="w-4 h-4" />
              </button>
            </div>
          </form>
        </div>

        {/* ── Result Panel ── */}
        <div className="lg:col-span-2 glass-panel p-6 flex flex-col justify-center items-center text-center min-h-[420px]">
          {result ? (() => {
            const rc = riskColors[result.risk_level];
            const pct = (result.churn_probability * 100);
            return (
              <div className="space-y-6 w-full animate-in fade-in zoom-in duration-500">
                {/* Icon badge */}
                <div className={`inline-flex p-5 rounded-2xl border ${rc.bg} ${rc.border} mx-auto`}>
                  {result.risk_level === 'High'
                    ? <ShieldAlert className={`w-12 h-12 ${rc.text}`} />
                    : <ShieldCheck  className={`w-12 h-12 ${rc.text}`} />
                  }
                </div>

                {/* Risk label */}
                <div className={`inline-block px-4 py-1.5 rounded-full text-sm font-bold border ${rc.bg} ${rc.text} ${rc.border}`}>
                  {result.risk_level} Risk
                </div>

                {/* Probability */}
                <div>
                  <p className="text-gray-400 text-xs uppercase tracking-widest mb-1">Churn Probability</p>
                  <div className="text-6xl font-black mt-1 bg-gradient-to-br from-white to-gray-500 bg-clip-text text-transparent tabular-nums">
                    {pct.toFixed(1)}%
                  </div>
                </div>

                {/* Progress bar */}
                <div className="w-full">
                  <div className="w-full bg-gray-800 rounded-full h-2.5 border border-gray-700 overflow-hidden">
                    <div
                      className={`h-full rounded-full bg-gradient-to-r ${rc.bar} transition-all duration-1000`}
                      style={{ width: `${pct}%` }}
                    />
                  </div>
                  <div className="flex justify-between text-[10px] text-gray-600 mt-1">
                    <span>Low (0%)</span><span>High (100%)</span>
                  </div>
                </div>

                {/* Verdict */}
                <div className="pt-4 border-t border-gray-700/50 text-sm text-gray-400 leading-relaxed">
                  {result.prediction === 1
                    ? '⚠️ Model predicts this customer is likely to exit. Consider proactive retention.'
                    : '✅ Model predicts this customer will be retained.'}
                </div>
              </div>
            );
          })() : (
            <div className="text-gray-600 space-y-3">
              <ShieldCheck className="w-16 h-16 mx-auto opacity-20" />
              <p className="text-sm">Fill in the form and click<br /><span className="text-blue-400 font-medium">Analyse Risk Score</span> to see results.</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
