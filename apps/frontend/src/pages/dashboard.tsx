export function DashboardPage() {
  const cards = [
    { title: "Average GEO Score", value: "72.5" },
    { title: "Brand Visibility", value: "68%" },
    { title: "Competitor Dominance", value: "31%" },
    { title: "Citation Trend", value: "↗ stable" },
    { title: "China vs Global", value: "CN 64 / Global 74" },
    { title: "Desktop vs Mobile", value: "Desktop 76 / Mobile 69" },
  ];

  return (
    <section>
      <h2>Dashboard</h2>
      <p>MVP dashboard for GEO Command Center.</p>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(3, minmax(180px, 1fr))", gap: 12 }}>
        {cards.map((card) => (
          <div key={card.title} style={{ border: "1px solid #ddd", borderRadius: 8, padding: 12 }}>
            <div style={{ fontSize: 12, color: "#555" }}>{card.title}</div>
            <div style={{ fontSize: 20, fontWeight: 700 }}>{card.value}</div>
          </div>
        ))}
      </div>
    </section>
  );
}
