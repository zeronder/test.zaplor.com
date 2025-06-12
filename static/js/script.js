document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', () => {
        const target = card.getAttribute('data-target');
        if (target) {
            window.location.href = target;
        }
    });
});