import { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

function SalesTrend() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/sales-trend')
      .then((res) => res.json())
      .then((data) => setData(data))
      .catch((err) => console.error('Failed to fetch sales trend:', err));
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h2>Sales Trend</h2>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="total_sales" stroke="#2563eb" strokeWidth={2} dot={false} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default SalesTrend;