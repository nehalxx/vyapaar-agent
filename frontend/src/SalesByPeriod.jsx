import { useEffect, useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

function SalesByPeriod() {
  const [period, setPeriod] = useState('day');
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch(`http://localhost:8000/api/sales-by-period?period=${period}`)
      .then((res) => res.json())
      .then((data) => setData(data))
      .catch((err) => console.error('Failed to fetch sales by period:', err));
  }, [period]);

  return (
    <div style={{ padding: '20px' }}>
      <h2>Low vs High Sales</h2>

      <div style={{ marginBottom: '10px' }}>
        {['day', 'month', 'year'].map((p) => (
          <button
            key={p}
            onClick={() => setPeriod(p)}
            style={{
              marginRight: '8px',
              padding: '6px 12px',
              background: period === p ? '#2563eb' : '#e5e7eb',
              color: period === p ? 'white' : 'black',
              border: 'none',
              borderRadius: '4px',
              cursor: 'pointer'
            }}
          >
            {p.charAt(0).toUpperCase() + p.slice(1)}
          </button>
        ))}
      </div>

      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="label" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="total_sales" fill="#2563eb" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default SalesByPeriod;