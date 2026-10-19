document.addEventListener('DOMContentLoaded', () => {
  const article = document.querySelector('main.content');
  const title = document.querySelector('#title-block-header');
  if (!article || !title || !/^\d{2}-/.test(location.pathname.split('/').pop())) return;
  const words = (article.textContent || '').trim().split(/\s+/).length;
  const label = document.createElement('p');
  label.className = 'chapter-reading-time';
  label.textContent = `About ${Math.max(5, Math.ceil(words / 150))} minutes to read · allow extra time for derivations`;
  title.after(label);
});
