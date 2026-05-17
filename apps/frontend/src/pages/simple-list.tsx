type Props = { title: string };

export function SimpleListPage({ title }: Props) {
  return (
    <section>
      <h2>{title}</h2>
      <p>MVP placeholder page for {title}.</p>
    </section>
  );
}
