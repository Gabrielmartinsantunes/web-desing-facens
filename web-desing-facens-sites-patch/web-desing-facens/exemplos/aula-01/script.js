(() => {
  'use strict';

  const countInput = document.querySelector('#member-count');
  const status = document.querySelector('#group-status');
  const decrease = document.querySelector('#decrease');
  const increase = document.querySelector('#increase');

  if (!countInput || !status) return;

  function updateGroupStatus() {
    const count = Number.parseInt(countInput.value, 10);

    if (!Number.isInteger(count) || count < 1 || count > 10) {
      status.textContent = 'Informe uma quantidade entre 1 e 10 para conferir.';
      status.classList.add('invalid');
      return;
    }

    if (count < 3 || count > 5) {
      status.textContent = `${count} integrante(s): fora da orientação de 3 a 5 integrantes dos slides.`;
      status.classList.add('invalid');
      return;
    }

    status.textContent = `${count} integrantes: dentro da orientação dos slides.`;
    status.classList.remove('invalid');
  }

  countInput.addEventListener('input', updateGroupStatus);

  decrease?.addEventListener('click', () => {
    const current = Number.parseInt(countInput.value, 10) || 1;
    countInput.value = String(Math.max(1, current - 1));
    updateGroupStatus();
  });

  increase?.addEventListener('click', () => {
    const current = Number.parseInt(countInput.value, 10) || 1;
    countInput.value = String(Math.min(10, current + 1));
    updateGroupStatus();
  });

  updateGroupStatus();
})();
