// Mobile menu toggle
document.querySelectorAll('.menu-btn').forEach(btn => {
	btn.addEventListener('click', () => {
		const open = btn.closest('header').classList.toggle('open');
		btn.setAttribute('aria-expanded', open);
		btn.textContent = open ? 'Close' : 'Menu';
	});
});

// Gallery lightbox
const box = document.querySelector('dialog.lightbox');
if (box) {
	const img = box.querySelector('img'), cap = box.querySelector('p');
	document.querySelectorAll('.gallery button').forEach(b => {
		b.addEventListener('click', () => {
			const thumb = b.querySelector('img');
			img.src = b.dataset.full;
			img.alt = thumb.alt;
			cap.textContent = thumb.alt;
			box.showModal();
		});
	});
	box.querySelector('.close').addEventListener('click', () => box.close());
	box.addEventListener('click', e => { if (e.target === box) box.close(); });
}

// Contact form: preview only, nothing is sent
const form = document.querySelector('form.mock');
if (form) {
	form.addEventListener('submit', e => {
		e.preventDefault();
		const msg = document.querySelector('.form-msg');
		msg.classList.add('show');
		msg.focus();
		form.reset();
	});
}
