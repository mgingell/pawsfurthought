# 3. Home page

**Pages → Home → Edit with Elementor.** To see the target layout, open [preview/home.html](../preview/home.html).

How to paste text: click a **Text Editor** widget, then in the left panel switch the editor from **Visual** to **Text** (the tab at the top-right of the box). Select everything, paste the HTML below, and switch back to Visual to check it.

### Current layout → new layout

| # | Section now | Change |
|---|---|---|
| 1 | Hero "Paws Fur Thought" + 3 buttons | **Edit**: new background, heading, text and buttons |
| 2 | — | **New**: numbers band |
| 3 | Who We Are | **Edit**: fix text |
| 4 | What Is a Service Dog | **Edit**: fix text |
| 5 | Our Process | **Replace** the long text with 4 steps + "what's covered" |
| 6 | — | **New** (optional): Our teams photos |
| 7 | — | **New**: Partners |
| 8 | We are a not-for-profit (bally photo) | **Edit**: clearer text, button → new Donate page |

Click **Update** after each section. Elementor keeps revisions, so you can roll back.

---

## Section 1: Hero

**Section → Style → Background → Image**: replace with `hero-service-dog-ceremony.jpg`. Set **Position: Center Center**. Keep the dark gradient overlay so white text stays readable. (Optional alternative: `hero-alt-dogs-illustrated.jpg`.)

**Heading widget** (currently "Paws Fur Thought", 75px)
- Text: `Service Dogs for Veterans with PTSD`
- **HTML Tag: H1**. The logo already shows the name, and this tells visitors and Google what you do.
- On **Responsive → Mobile**, set the font size to about **40px**. 75px wraps badly on phones.

**Text Editor widget** (currently "Proudly serving the Atlantic Canadian provinces.")
```html
Paws Fur Thought pairs Canadian Military and RCMP veterans and serving members living with an Operational Stress Injury (OSI) or PTSD with fully trained, certified service dogs. Proudly serving Atlantic Canada since 2013.
```

**Buttons** (three now: CONTACT, INTAKE FORM, DONATE)

| Button | New text | Link |
|---|---|---|
| INTAKE FORM | `Apply for a Service Dog` | `/application-process/in-take/` (unchanged) |
| DONATE | `Donate` | `/donate/` (the new page from guide 7, not straight to WWC) |
| CONTACT | `Contact Us` | `/contact/`. Advanced → CSS Classes: `pft-btn-outline` (white outline, so it reads as secondary) |

Put **Apply** first. Drag the widgets to reorder.

---

## Section 2 (new): Numbers band

Right-click the Hero section → **Add New Section** below → 1 row, 3 columns. On the section: Advanced → CSS Classes → `pft-band-cream`, with Padding about 40px top/bottom.

In each column add a **Counter** widget, with Advanced → CSS Classes → `pft-stat`:

| Column | Start | End | Prefix / Suffix | Title |
|---|---|---|---|---|
| 1 | 0 | 100 | suffix `+` | Service dogs paired since 2013 |
| 2 | 0 | 2000 | prefix `Nearly ` | Dogs placed by CARES since 1993 |
| 3 | 0 | 5 | — | Days of hands-on training with your dog |

Turn on Thousand Separator for column 2. Update the "100+" figure each year.

---

## Section 3: Who We Are

Heading: keep **WHO WE ARE** (H2).

Text Editor:
```html
<p>Paws Fur Thought is a not-for-profit organization that pairs Canadian Military and RCMP veterans and serving members diagnosed with an Operational Stress Injury (OSI) or PTSD with fully trained, certified service dogs.</p>
<p>We are proud to be a recognized service dog provider in the <strong>Wounded Warriors Canada Service Dog Program</strong>, and we coordinate the pairing of veterans with dogs trained and certified by <a href="https://www.caresks.com/" target="_blank" rel="noopener">CARES, Inc.</a></p>
```

Image: replace with `pft-patch-red.png` (the "Paws-itive Outcomes" emblem), as in the preview. Or keep the current group-of-dogs photo and set its **Alternative Text** to *A group of service dogs in vests resting in a row* (Media → click → Alternative Text).

---

## Section 4: What Is a Service Dog

Heading: keep (H2).

Text Editor:
```html
<p>There is often confusion about what makes a true service dog. Every service dog is trained and tested for public access <strong>and</strong> task-trained to help their handler with a specific disability. That can include diabetic and seizure alerting, mobility assistance, autism support, hearing assistance, and OSI/PTSD intervention.</p>
<p>In Nova Scotia, service dogs and their handlers are protected under the <a href="https://novascotia.ca/servicedogs/" target="_blank" rel="noopener">Service Dog Act</a>.</p>
```

Image (soldier hugging dog by helicopter): set the alt text to *A Canadian Armed Forces member in uniform hugs a yellow Labrador service dog in front of a Sea King helicopter*.

---

## Section 5: How It Works (replaces "Our Process")

1. Change the Heading to `How It Works` (H2).
2. **Delete** the long Text Editor in this section. Keep the image (Gander airport photo) or delete it. The steps carry the section.
3. Add an **inner section with 4 columns**. In each column, an **Icon Box** widget (Icon: a number or a paw; Title HTML tag: **H3**):

| # | Title | Description |
|---|---|---|
| 1 | Apply | Complete our online intake form. It helps us confirm your eligibility. |
| 2 | Hear back | If you're accepted, we'll contact you within a week to continue the process. |
| 3 | Train together | Spend 5 days training with your new service dog at CARES in Concordia, Kansas. Training is mandatory for new and successor dogs. |
| 4 | Go home as a team | Return home with a fully trained, certified service dog, with Paws Fur Thought behind you. |

4. Below the columns, add a **Text Editor**:
```html
<h3>What's covered</h3>
<p>Paws Fur Thought funds the cost of your service dog, your flights, and your accommodation in Concordia. You'll need to rent a car for the drive from the Wichita airport to Concordia (about 2 hours 15 minutes).</p>
<p>New to OSI and PTSD? See our <a href="/resources/">OSI/PTSD resources</a>, or read the <a href="/faq/">frequently asked questions</a>.</p>
```
> **[CONFIRM]** If the rental car or meals are reimbursed, say so here. It's a common question.

5. Add a **Button**: `Start Your Application` → `/application-process/in-take/`.

---

## Section 6 (new, optional): Our Teams

> **[CONFIRM]** Only if the people pictured agree.

New section, 3 columns, Advanced → CSS Classes → `pft-team`. A heading above (H2): `Our Teams`.
In each column, an **Image** widget: `team-1.jpg`, `team-2.jpg`, `team-3.jpg` (alt text comes from the Media Library, see guide 1). Optional caption: first names of the handler and dog.

---

## Section 7 (new): Partners

New section, class `pft-band-cream`, 2 columns:
- **Column 1:** Image `cares-logo.png` (class `pft-partner`, link `https://www.caresks.com/`) + Text:
```html
<p><strong>CARES, Inc.</strong> (Canine Assistance, Rehabilitation and Education Services) in Concordia, Kansas, trains and certifies every dog we place. CARES has placed nearly 2,000 assistance dogs since 1993.</p>
```
- **Column 2:** Image `wwc-service-dog.png` (class `pft-partner`, link `https://woundedwarriors.ca/`) + Text:
```html
<p><strong>Wounded Warriors Canada</strong> supports Paws Fur Thought through its <a href="https://woundedwarriors.ca/" target="_blank" rel="noopener">Service Dog Program</a>. Your donations to WWC help fund the dogs, training and travel for our veterans.</p>
```
Heading above both columns (H2): `Our Partners`.

---

## Section 8: We Are a Not-for-Profit (photo band)

Heading: `Help Pair a Veteran with a Service Dog` (H2). On mobile, reduce the font size from 68px to about 36px.

Text Editor:
```html
<p>Paws Fur Thought is a not-for-profit supported by Wounded Warriors Canada. Every donation helps cover a service dog, training, and travel for a Canadian veteran.</p>
```

Button: text `How to Donate` → link `/donate/`.

---

## Check

- Exactly **one H1** on the page (the hero heading). Every other section heading is H2, and the step titles are H3.
- Preview on mobile: Elementor's bottom-left **Responsive Mode** icon → Mobile. Nothing should overflow, and headings shouldn't be giant.
- All buttons show white text.
