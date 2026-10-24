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
- **Add a gallery photo:** put a JPG in `src/static/img/gallery/` (about 1600 px wide is plenty) and add a line to `src/gallery.json` with its file name and a short description of what's in the photo. Optionally add a 600×600 square copy with the same name in `gallery/thumbs/` so the grid loads faster. Without one, the full photo is used.
- **Update the "100+ dogs paired" figure:** it's in `src/pages/index.html` and `src/pages/donate.html`.

## Settings (`src/site.json`)

| Setting | What it does |
|---|---|
| `email` | Shown across the site and used by the contact form. |
| `intake_form_url` | **Paste the intake form link here when it arrives.** While it's empty, the Apply page says "available in late October 2026" and the button is greyed out. Once it's filled in, the page says applications are open and the button goes to the form. |
| `contact_form_endpoint` | Where the contact form sends messages. While empty, pressing **Send** opens the visitor's email app with the message filled in, which works with no setup. To have messages sent directly, create a free form at [formspree.io](https://formspree.io) using the organization's email and paste its URL here (looks like `https://formspree.io/f/abcdwxyz`). |
| `site_url` | The public address. Used for search engines and link previews. |

Rebuild after changing settings (automatic if `--watch` is running).

## Things to confirm before going live

Search `src/pages/` for **`[CONFIRM]`**. These show as yellow tags on the pages until you fill them in:
- FAQ: typical wait between acceptance and the training trip
- FAQ: is the rental car reimbursed, and are meals covered?
- Contact: realistic reply time
- Home "Our Teams": do the people in `team-1..3.jpg` agree to appear on the site?
- Donate: walk through WWC's donation form once to check "PTSD Service Dogs" and the comment box still exist under those names

## Publishing: Cloudflare Pages (connected to GitHub)

The source lives at https://github.com/mgingell/pawfurthought. Cloudflare Pages builds and publishes the site automatically every time you push to `main`.

**One-time setup** in the Cloudflare dashboard (**Workers & Pages → Create → Pages → Connect to Git**):
1. Choose the `mgingell/pawfurthought` repository.
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
