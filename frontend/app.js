const API_BASE = "http://127.0.0.1:8000";

async function addExpense() {
  const amount = document.getElementById("amount").value;
  const category = document.getElementById("category").value;
  const date = document.getElementById("date").value;

  if (!amount || !category || !date) {
    alert("Fill all fields");
    return;
  }

  await fetch(`${API_BASE}/expenses`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      amount: parseFloat(amount),
      category,
      date
    })
  });

  loadExpenses();
  loadInsights();
}

async function loadExpenses() {
  const res = await fetch(`${API_BASE}/expenses`);
  const data = await res.json();

  const list = document.getElementById("expenseList");
  list.innerHTML = "";

  data.forEach(e => {
    const li = document.createElement("li");
    li.textContent = `${e.category} - ${e.amount} on ${e.date}`;
    list.appendChild(li);
  });
}

async function loadInsights() {
  const res = await fetch(`${API_BASE}/insights`);
  const data = await res.json();
  document.getElementById("insights").textContent =
    JSON.stringify(data, null, 2);
}

loadExpenses();
loadInsights();
