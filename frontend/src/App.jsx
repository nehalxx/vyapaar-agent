import { useEffect, useState } from 'react';

function App() {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/transactions')
      .then((res) => res.json())
      .then((data) => setTransactions(data))
      .catch((err) => console.error('Failed to fetch:', err));
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>Transactions</h1>
      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>ID</th>
            <th>Timestamp</th>
            <th>Type</th>
            <th>Amount</th>
            <th>Day</th>
          </tr>
        </thead>
        <tbody>
          {transactions.map((t) => (
            <tr key={t.transaction_id}>
              <td>{t.transaction_id}</td>
              <td>{t.timestamp}</td>
              <td>{t.transaction_type}</td>
              <td>{t.amount}</td>
              <td>{t.day_of_week}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;