(() => {
  const search = document.querySelector('#lesson-search');
  const links = [...document.querySelectorAll('.nav-list li')];
  const empty = document.querySelector('.empty-search');

  if (search) {
    search.addEventListener('input', () => {
      const term = search.value.trim().toLocaleLowerCase('pt-BR');
      let visible = 0;
      links.forEach((item) => {
        const match = item.textContent.toLocaleLowerCase('pt-BR').includes(term);
        item.hidden = !match;
        if (match) visible += 1;
      });
      if (empty) empty.style.display = visible === 0 ? 'block' : 'none';
    });
  }

  const printButton = document.querySelector('[data-print-page]');
  if (printButton) printButton.addEventListener('click', () => window.print());
})();
