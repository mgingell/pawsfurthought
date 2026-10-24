# 4. Intake page

**Pages → Intake → Edit with Elementor.** The page has one Heading ("Intake Process") and one Text Editor.

The online intake form link arrives in **late October 2026**. There are two versions below:
- **Version A:** use now, until you have the link.
- **Version B:** switch to it the day you get the form link.

Everything except the status box and button stays the same.

## Heading
`Apply for a Service Dog` (HTML Tag: **H1**)

## Text Editor: replace with Version A or B

### Version A (before the form link is ready)
```html
<p><strong>Our online intake form will be available in late October 2026.</strong> Please check back soon. For questions about successor dogs or general inquiries, email <a href="mailto:info.pawsfurthought@gmail.com">info.pawsfurthought@gmail.com</a>.</p>

<h2>Who can apply</h2>
<ul>
  <li>Canadian Armed Forces and RCMP veterans and serving members</li>
  <li>Diagnosed with an Operational Stress Injury (OSI) or PTSD as a result of military or policing service</li>
  <li>Living in Atlantic Canada (Nova Scotia, New Brunswick, Prince Edward Island, or Newfoundland and Labrador)</li>
</ul>

<h2>What to expect</h2>
<ol>
  <li><strong>Apply.</strong> Complete the intake form. It helps us confirm your eligibility.</li>
  <li><strong>Hear back.</strong> If you're accepted, we'll contact you within a week to continue the process.</li>
  <li><strong>Train together.</strong> Attend a mandatory 5-day training session with your service dog at <a href="https://www.caresks.com/" target="_blank" rel="noopener">CARES</a> in Concordia, Kansas. This applies to both new and successor dogs.</li>
</ol>

<h2>What's covered</h2>
<p>Paws Fur Thought funds the cost of your service dog, your flights, and your accommodation in Concordia. You'll need to rent a car for the drive from the Wichita airport to Concordia (about 2 hours 15 minutes).</p>

<p>Have questions first? See our <a href="/faq/">FAQ</a> or <a href="/contact/">contact us</a>.</p>
```

### Version B (once you have the form link)
1. Replace the first paragraph of Version A with:
```html
<p><strong>Applications are open.</strong> Complete our online intake form to get started. For questions about successor dogs or general inquiries, email <a href="mailto:info.pawsfurthought@gmail.com">info.pawsfurthought@gmail.com</a>.</p>
```
2. Under the Heading, add a **Button** widget: text `Start the Intake Form`, link = **the form URL**. Tick *Open in new window* if the form is on another site (e.g. Google Forms or Microsoft Forms).
3. Add a second identical button at the bottom of the page, after "What's covered", so people don't have to scroll back up.

> **[CONFIRM]** The "Who can apply" list combines what the current site says ("Military and RCMP veterans and serving members… diagnosed with OSI/PTSD… Atlantic Canada"). If a referral or doctor's letter is required, add it as a bullet.

## Page title
In Elementor ⚙ (Page Settings) → **Title**: `Intake`. The menu already links here, and the URL stays `/application-process/in-take/`. No change needed.
