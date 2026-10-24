# 5. Contact page

**Pages → Contact Us → Edit with Elementor.** Current widgets: "Get In Touch with Us" heading, "CONTACT INFO" heading, an email icon, a Text Editor (email), a "SEND A MESSAGE" heading, and a **Shortcode** widget (the Ninja Forms form).

## 5a. Test the form first (most important)

The form is drawn by JavaScript, so I couldn't check it from outside.
1. Open https://pawsfurthought.ca/contact/ in a private window.
2. Fill it in with your own name and email, and in the message write `Test, please ignore`.
3. Confirm that (a) the page says the message was sent, and (b) the email arrives at **info.pawsfurthought@gmail.com**. Check Spam too.

If it doesn't arrive: **Ninja Forms → (your form) → Emails & Actions → Admin Email**. Check that the *To* address is `info.pawsfurthought@gmail.com`. Website email from GoDaddy Managed WP often lands in spam. If it keeps failing, install the free **WP Mail SMTP** plugin and connect it to the Gmail account.

Also in the form: give every field a visible **label** (not only placeholder text) and turn on the built-in **reCAPTCHA** or honeypot to reduce spam.

## 5b. Text changes

- Heading "Get In Touch with Us" → `Contact Us` (H1).
- "CONTACT INFO" → `Email Us` (H2).
- Text Editor (email): use a real link so it opens the mail app:
```html
<p><a href="mailto:info.pawsfurthought@gmail.com">info.pawsfurthought@gmail.com</a></p>
<p>We're a volunteer-run organization. We do our best to reply within a few days.</p>
```
  > **[CONFIRM]** Change "within a few days" to whatever's realistic.
- "SEND A MESSAGE" → `Send Us a Message` (H2).
- Add a short Text Editor above the form:
```html
<p>Interested in a service dog? Please start with the <a href="/application-process/in-take/">Intake page</a>. Have a question about successor dogs, donations or anything else? Send us a note.</p>
```

## 5c. If you're in crisis

Add a small Text Editor at the bottom of the page. People contacting a PTSD service-dog program may be struggling, so give them somewhere to turn right away:
```html
<p><strong>Need help now?</strong> Call or text <strong>9-8-8</strong> (Suicide Crisis Helpline, 24/7). Veterans and families can also call the <strong>VAC Assistance Service at 1-800-268-7708</strong>, free and confidential, 24/7.</p>
```
