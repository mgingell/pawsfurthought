# 10. Menu, footer, and final checks

## 10a. Menu

**Appearance → Menus** → select the main (primary) menu.

New order:
1. Home
2. Intake. Optionally change its *Navigation Label* to `Apply`.
3. FAQ *(new page: Add menu items → Pages → tick it)*
4. Resources *(existing page, not in the menu today)*
5. Gallery
6. Contact Us
7. Donate *(new page)*

To make **Donate** a red button: **Screen Options** (top-right) → tick **CSS Classes**. Expand the Donate item and enter `pft-menu-donate` in *CSS Classes*. The styling comes from the Additional CSS in guide 2.

**Save Menu.** Check on a phone that the hamburger menu shows all seven items.

> The menu uses the "WP Menu Icons" plugin. If an item shows an odd icon, expand it and clear the icon.

## 10b. Footer widgets

**Appearance → Widgets** (or Customize → Widgets) → the Zakra **Footer** areas. Today they contain:
- "Paws Fur Thought": one sentence
- "Contact Information": a single "Contact Us" link
- "Intake Information": a single "Intake" link

Replace them with **two** widgets.

**Footer 1** (Paragraph/Custom HTML), title `Paws Fur Thought`:
```html
<p>Pairing Canadian Military and RCMP veterans living with OSI or PTSD with fully trained, certified service dogs. Serving Atlantic Canada since 2013.</p>
<p><a href="mailto:info.pawsfurthought@gmail.com">info.pawsfurthought@gmail.com</a></p>
```

**Footer 2** (Custom HTML), title `Quick Links`:
```html
<ul>
  <li><a href="/application-process/in-take/">Apply for a service dog</a></li>
  <li><a href="/faq/">FAQ</a></li>
  <li><a href="/resources/">OSI &amp; PTSD resources</a></li>
  <li><a href="/donate/">Donate</a></li>
  <li><a href="/contact/">Contact us</a></li>
</ul>
<p><strong>In crisis?</strong> Call or text 9-8-8, 24/7.</p>
```

Delete the old "Contact Information" and "Intake Information" widgets. If Zakra is set to 3 or 4 footer columns, set it to 2: **Customize → Footer → Footer Widgets → Columns**.

**Copyright line:** "Copyright © 2026 Paws Fur Thought." updates automatically, so leave it.

## 10c. Page titles (what shows in browser tabs and Google)

Check each page title is plain and clear:

| Page | Title |
|---|---|
| Home | Home *(the site title "Paws Fur Thought" is added automatically)* |
| Intake | Apply for a Service Dog |
| FAQ | Frequently Asked Questions |
| Resources | OSI and PTSD Resources |
| Gallery | Gallery |
| Donate | Donate |
| Contact | Contact Us |

**Settings → General → Tagline:** `Service Dogs for Veterans with PTSD`.

## 10d. Final checks (open the site in a private window)

- [ ] Every menu link opens the right page, on desktop and on a phone
- [ ] All buttons have **white** text and darken on hover
- [ ] No more "facilitates coordinates", "OSI's" or "early 2027" anywhere
- [ ] "Operational Stress Injury" is spelled out on Home, Intake, Resources and FAQ
- [ ] Contact form test email received (guide 5)
- [ ] Donate page link → WWC works, and the steps match WWC's current form
- [ ] Gallery duplicate removed; hover a few photos and spot-check their alt text (or use a free checker such as https://wave.webaim.org/)
- [ ] Email address can be selected and copied (copy-protect plugin off)
- [ ] When the intake form link arrives: Intake page switched to Version B (guide 4) and the button tested

### Optional: accessibility score
In Chrome: right-click the page → **Inspect → Lighthouse** tab → tick *Accessibility* → **Analyze page load**. Aim for 90+. The report lists anything left to fix.
