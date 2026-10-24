# Paws Fur Thought — website update kit

This kit updates **pawsfurthought.ca** without leaving GoDaddy Managed WordPress.
Everything here is applied by hand in WP admin. Nothing is uploaded automatically.

## What the site is built with (found on the live site, Oct 2026)

| Piece | Used for | Where you edit it |
|---|---|---|
| **Zakra** theme | Header, logo, menu, footer | Appearance → Customize, Appearance → Widgets |
| **Elementor** page builder | Home, Intake, Contact pages | Pages → (page) → *Edit with Elementor* |
| Block editor | Resources page | Pages → Resources → Edit |
| **Ninja Forms** | Contact page form | Ninja Forms menu |
| **Modula** | Gallery grid | Modula menu → (gallery) |
| WP Content Copy Protector | Blocks text selection (adds a hidden "error:" message) | Plugins |

## Biggest problems this kit fixes

1. **Button text fails contrast.** Black text on red buttons (#16181A on #C50000) is about 3.3:1, and the minimum is 4.5:1. Hard to read, especially for older eyes.
2. **Copy errors:** "facilitates coordinates the pairing", "OSI's", OSI never spelled out, a mis-bolded "i**s**".
3. **Intake page** still says applications are paused until early 2027. The online intake form arrives in late October 2026.
4. **Donating is confusing:** the only instruction is "leave a comment".
5. **Resources page** isn't in the menu. There's no FAQ, and the email address isn't on the home page.
6. **Gallery:** 12 of 26 photos have no description for screen readers, one says "Get In Touch", and one photo appears twice.
7. **Copy protection plugin** stops visitors from copying the email address. It doesn't stop anyone determined to copy photos.
8. **Elementor global colours** are still the default teal theme colours, not the brand red/black/taupe.

## Order of work (about 2–3 hours total)

Work top to bottom. Each step is safe to stop after.

| # | Guide | Time |
|---|---|---|
| 1 | [guide/1-before-you-start.md](guide/1-before-you-start.md): backup, upload images | 15 min |
| 2 | [guide/2-site-styles.md](guide/2-site-styles.md): logo, colours, fonts, button fix, CSS | 20 min |
| 3 | [guide/3-home.md](guide/3-home.md): Home page | 45 min |
| 4 | [guide/4-intake.md](guide/4-intake.md): Intake page and form link | 15 min |
| 5 | [guide/5-contact.md](guide/5-contact.md): Contact page and form test | 10 min |
| 6 | [guide/6-resources.md](guide/6-resources.md): Resources page | 10 min |
| 7 | [guide/7-donate-new.md](guide/7-donate-new.md): **new** Donate page | 15 min |
| 8 | [guide/8-faq-new.md](guide/8-faq-new.md): **new** FAQ page | 20 min |
| 9 | [guide/9-gallery.md](guide/9-gallery.md): gallery descriptions | 20 min |
| 10 | [guide/10-menu-footer-checks.md](guide/10-menu-footer-checks.md): menu, footer, final checks | 20 min |

**Want to practise safely first?** [docker/README.md](docker/README.md) sets up a private copy of the whole site on this computer. Apply the guides there, check the result, then repeat on the live site.

**Want to see the target look first?** Open [preview/home.html](preview/home.html) in a browser, or http://localhost:8080/preview/ if the Docker copy is running. It's a clickable mock-up of the whole proposed site (Home, Apply, FAQ, Resources, Gallery, Donate, Contact). It's for reviewing the look and wording, not for uploading.

## Things only you can confirm

Search the guides for **`[CONFIRM]`**. These are facts the current site doesn't state, and I didn't want to guess them:
- Is the rental car (Wichita → Concordia) reimbursed, or does the veteran pay?
- Are meals in Concordia covered?
- Typical wait between acceptance and the training trip.
- Do the people in the team photos (assets/team-1..3.jpg) agree to appear on the home page?

## Files

```
assets/   images ready to upload to the WordPress Media Library
guide/    step-by-step instructions + text to paste
theme/additional-css.css   paste into Appearance → Customize → Additional CSS
preview/                   clickable mock-up of the whole proposed site (start at home.html)
```
