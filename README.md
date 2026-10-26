# Paws Fur Thought website

A plain static website for **pawsfurthought.ca**: HTML, one stylesheet, a small script, and images. There's no WordPress, database or plugins. It can be hosted for free almost anywhere.

## Run it locally

You need Docker Desktop and Python 3 (both already on this PC). From this folder, in PowerShell:

```powershell
docker compose up -d          # start the local web server (once; it keeps running)
python build.py --watch       # build the site, then rebuild whenever you save a change
```

Open **http://localhost:8080**. Edit anything in `src/`, save, and refresh the browser.

| Task | Command |
|---|---|
| Build once (no watching) | `python build.py` |
| Stop the web server | `docker compose stop` |
| Start it again | `docker compose start` |

## Where things are

```
src/
  site.json        settings: email, intake form link, contact form service, site address
  layout.html      header, menu and footer shared by every page
  pages/           one file per page (index = Home, apply, faq, resources, gallery, donate, contact, 404)
  partials/        snippets reused on several pages (crisis-line box)
  gallery.json     the gallery photos, in order, with their descriptions
  static/          copied into the site as-is
    css/site.css   all styling (brand colours are at the top)
    js/site.js     phone menu, gallery viewer, contact form
    img/           logo, photos, partner logos, icons
build.py           turns src/ into site/
site/              the finished website: this is what you upload (rebuilt every time, so don't edit it)
docker-compose.yml, nginx-dev.conf   the local web server
archive/wordpress/ the earlier WordPress update guides, kept for reference
```

### Common edits

- **Change text on a page:** edit `src/pages/<page>.html`. The comment at the top sets the browser-tab title and the description search engines show.
- **Change the menu or footer:** edit `src/layout.html`. The menu order lives in `NAV` at the top of `build.py`.
- **Add gallery photos:** put the originals (JPG, PNG or iPhone HEIC, any size) in `photos-incoming/` and run `python add_photos.py`. It fixes sideways photos, saves a web-sized copy and a square thumbnail, adds each photo to the end of `src/gallery.json`, and moves the originals to `photos-incoming/done/`. Then open `src/gallery.json` and replace each `DESCRIBE THIS PHOTO` with a short description of what's in the picture; screen readers read it aloud to blind visitors, and the build warns about any you've missed. To reorder photos, move their lines in `gallery.json`; to remove one, delete its line.
- **Update the "dogs paired" and CARES figures:** they appear in `src/pages/index.html`, `src/pages/donate.html` and `src/pages/faq.html`.

## Settings (`src/site.json`)

| Setting | What it does |
|---|---|
| `email` | Shown across the site and used by the contact form. |
| `intake_form_url` | **Paste the intake form link here when it arrives.** While it's empty, the Apply page says "available in late October 2026" and the button is greyed out. Once it's filled in, the page says applications are open and the button goes to the form. |
| `contact_form_endpoint` | Where the contact form sends messages. While empty, pressing **Send** opens the visitor's email app with the message filled in, which works with no setup. To have messages sent directly, create a free form at [formspree.io](https://formspree.io) using the organization's email and paste its URL here (looks like `https://formspree.io/f/abcdwxyz`). |
| `site_url` | The public address. Used for search engines and link previews. |

Rebuild after changing settings (automatic if `--watch` is running).

## Before going live

- **Contact form:** set up Formspree (below) or keep the email-app fallback.
- **Team photos:** three veteran-and-dog photos are in `archive/unpublished-photos/`. They aren't published, pending consent. To feature teams again, copy approved photos to `src/static/img/` and add a section to `src/pages/index.html`.
- **Gallery:** add new photos (see *Common edits*).

### Contact form with Formspree

1. Sign up at [formspree.io](https://formspree.io) with the email that should receive messages, and verify it.
2. Create a **New Form** (e.g. "Website contact"), and copy its endpoint, which looks like `https://formspree.io/f/abcdwxyz`.
3. Paste it into `src/site.json` as `contact_form_endpoint`, then rebuild.
4. Test at http://localhost:8080/contact/. The first submission may ask you to confirm the form by email.
5. Optional, after testing: in the form's settings, restrict submissions to `pawsfurthought.ca`. Doing this earlier blocks your local tests.

Messages arrive with the subject "Website message: <topic>", and the visitor's address is set as reply-to, so you can just hit Reply. The form also has a hidden spam trap (`_gotcha`) that Formspree recognizes.

## Publishing: Cloudflare Pages (connected to GitHub)

The source lives at https://github.com/mgingell/pawsfurthought. Cloudflare Pages builds and publishes the site automatically every time you push to `main`.

**One-time setup** in the Cloudflare dashboard (**Workers & Pages → Create → Pages → Connect to Git**):
1. Choose the `mgingell/pawsfurthought` repository.
2. Production branch: `main`.
3. Framework preset: **None**.
4. Build command: `python build.py`
5. Build output directory: `site`
6. **Save and Deploy.** The site appears at `<project>.pages.dev`.

**Day to day:** edit, check locally, then:
```powershell
git add -A
git commit -m "Describe the change"
git push
```
Cloudflare rebuilds within a minute or two. Pushing to any other branch makes a separate preview address, which is handy for trying a change before it goes live.

Cloudflare automatically uses `site/_redirects` (old WordPress links) and `site/404.html`.

### Other free hosts

Run `python build.py`, then upload the **contents of `site/`**:

| Host | How | Notes |
|---|---|---|
| **Netlify** | Sign up, then drag the `site` folder onto app.netlify.com/drop | Easiest. Honours `site/_redirects`, so old WordPress links get proper redirects. |
| **Cloudflare Pages** | Create a project → *Direct upload* → upload `site` | Also honours `_redirects`. |
| **GitHub Pages** | Put `site/` contents in a repository and enable Pages | Old links still work through the small redirect pages `build.py` generates. |

**Moving the domain.** Once the new site is up on the host's free address and checked, add `pawsfurthought.ca` as a custom domain in that host. Then change the domain's DNS records at the registrar (likely GoDaddy) as the host instructs.
- **Keep the domain registration.** Cancel only the Managed WordPress *hosting*, and only after the new site is live on the domain.
- The organization's email is Gmail, so changing the website DNS won't affect email.

**Old addresses** (`/contact/`, `/gallery/`, `/resources/`) are the same on the new site. `/application-process/in-take/` and a few other old WordPress pages redirect to the matching new page. The list is `REDIRECTS` in `build.py`.
