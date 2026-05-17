import { useEffect, useState } from "react";

import { apiGet } from "../api/client";

type Props<T> = {
  title: string;
  path: string;
  renderRow: (item: T) => string;
};

export function SimpleListPage<T>({ title, path, renderRow }: Props<T>) {
  const [data, setData] = useState<T[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    apiGet<T[]>(path)
      .then((rows) => {
        setData(rows);
        setError(null);
      })
      .catch((e: unknown) => {
        setError(e instanceof Error ? e.message : "Unknown error");
      })
      .finally(() => setLoading(false));
  }, [path]);

  return (
    <section>
      <h2>{title}</h2>
      {loading ? <p>Loading...</p> : null}
      {error ? <p style={{ color: "crimson" }}>{error}</p> : null}
      {!loading && !error ? (
        <ul>
          {data.map((item, idx) => (
            <li key={idx}>{renderRow(item)}</li>
          ))}
        </ul>
      ) : null}
    </section>
  );
}
