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

// Chart tooltips: each bar/column carries its own data-tip; shown on hover and keyboard focus
const tip = document.querySelector('.chart-tip');
if (tip) {
	const show = (el, x, y) => {
		tip.textContent = el.dataset.tip;
		tip.hidden = false;
		const r = tip.getBoundingClientRect();
		tip.style.left = Math.min(window.innerWidth - r.width - 8, Math.max(8, x - r.width / 2)) + 'px';
		tip.style.top = Math.max(8, y - r.height - 12) + 'px';
	};
	const hide = () => { tip.hidden = true; };
	document.querySelectorAll('[data-tip]').forEach(el => {
		el.addEventListener('pointermove', e => show(el, e.clientX, e.clientY));
		el.addEventListener('pointerleave', hide);
		el.addEventListener('focus', () => {
			const r = el.getBoundingClientRect();
			show(el, r.left + r.width / 2, r.top);
		});
		el.addEventListener('blur', hide);
	});
}

// Contact form
// With data-endpoint (e.g. a Formspree URL) the message is posted there.
// Without one, the visitor's email app opens with the message filled in.
const form = document.querySelector('form.contact');
if (form) {
	const msg = document.querySelector('.form-msg');
	const show = (text, isError) => {
		msg.textContent = text;
		msg.classList.add('show');
		msg.classList.toggle('error', !!isError);
		msg.focus();
	};

	form.addEventListener('submit', async e => {
		e.preventDefault();
		if (!form.reportValidity()) return;
		const data = new FormData(form);
		if (data.get('_gotcha')) return; // spam trap filled in

		const endpoint = form.dataset.endpoint;
		if (!endpoint) {
			const subject = `Website message: ${data.get('topic')}`;
			const body = `${data.get('message')}\n\nFrom: ${data.get('name')}\nEmail: ${data.get('email')}` +
				(data.get('phone') ? `\nPhone: ${data.get('phone')}` : '');
			window.location.href = `mailto:${form.dataset.email}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
			show(`Your email app should open with your message ready to send. If it doesn't, email us at ${form.dataset.email}.`);
			return;
		}

		data.append('_subject', `Website message: ${data.get('topic')}`);
		const button = form.querySelector('button[type="submit"]');
		button.disabled = true;
		try {
			const res = await fetch(endpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } });
			if (!res.ok) {
				const detail = await res.json().catch(() => ({}));
				console.error('Contact form rejected:', res.status, detail);
				throw new Error(res.status);
			}
			form.reset();
			show('Thank you! Your message has been sent. We\'ll get back to you as soon as we can.');
		} catch {
			show(`Sorry, your message couldn't be sent. Please email us at ${form.dataset.email}.`, true);
		} finally {
			button.disabled = false;
		}
	});
}
