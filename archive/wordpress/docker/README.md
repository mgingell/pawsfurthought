# Local practice copy (Docker)

A private copy of pawsfurthought.ca that runs only on this computer. Use it to work through the guides in `../guide/` and see the result **before** touching the live site.

| What | Address |
|---|---|
| Local site | http://localhost:8080 |
| Local WP admin | http://localhost:8080/wp-admin |
| Site mock-up (all pages) | http://localhost:8080/preview/ (served straight from `..\preview` and `..\assets`, so edits show on refresh) |
| Mail trap | http://localhost:8025. Every email the local site sends (e.g. contact form) shows up here, and **nothing is delivered to real inboxes**. |

The local copy is locked to `localhost:8080`, so it can't accidentally change or link back to the live site.

---

## 1. Start it (first time: about 2 minutes)

Docker Desktop must be running. Then, in PowerShell:

```powershell
cd C:\Working\WebPage\docker
.\setup.ps1
```

This starts WordPress, a database and the mail trap. It also installs the same theme and plugins as the live site: Zakra, Elementor, Ninja Forms, Modula, and All-in-One WP Migration (used for the import below).

At this point it's an **empty** WordPress (login `admin` / `admin`). Step 2 fills it with your real site.

## 2. Copy the live site into it

### 2a. Export from the live site
1. Log in to the **live** WP admin.
2. **Plugins → Add New**, search **All-in-One WP Migration**, then **Install** and **Activate**. (This adds a plugin to the live site. It doesn't change anything visitors see, and you can delete it afterwards.)
3. **All-in-One WP Migration → Export → Advanced options**, and tick:
   - **Do not export must-use plugins.** GoDaddy's hosting plugins don't work outside GoDaddy.
   - Do not export spam comments
   - Do not export post revisions
   - Do not export cache files
4. **Export To → File**, wait, then **Download**. You get a `.wpress` file.

> **Keep this file private.** It contains everything in the site, including any **Ninja Forms submissions** (names, emails, and possibly veterans' personal details). Don't email it or put it in a shared folder, and delete it when you're done.

### 2b. Import into the local copy
1. Go to http://localhost:8080/wp-admin and log in with `admin` / `admin`.
2. **All-in-One WP Migration → Import →** drag in the `.wpress` file **→ Proceed**.
3. When it finishes, you'll be logged out. Log in again with your **live site** username and password, since the import replaced the users.
4. **Settings → Permalinks → Save Changes** (click it twice, as the plugin suggests).
5. **Elementor → Tools → Regenerate Files & Data → Regenerate.** This rebuilds page styles for the new address.
6. Open http://localhost:8080. It should look like the live site.

If a page still looks unstyled: **Elementor → Tools → Replace URL**, from `https://pawsfurthought.ca` to `http://localhost:8080`, then regenerate again.

## 3. Practise the changes

Work through `..\guide\1-…` to `10-…` on the **local** admin (http://localhost:8080/wp-admin), exactly as written. Skip the backup step, since you don't need one locally.

- Contact form test: submit the form at http://localhost:8080/contact/ and check http://localhost:8025.
- Check on a phone-sized screen: in Chrome or Edge, press F12, then the phone icon (Toggle device toolbar).

Things that behave differently locally:
- **reCAPTCHA** on the contact form (if turned on) will fail, because its keys are tied to pawsfurthought.ca. That's expected.
- GoDaddy's page caching isn't present, so changes show up immediately.

## 4. Moving the finished changes to the live site

**Recommended:** repeat the steps on the live site using the same guides. Now that you've done them once, it's quick, and nothing else on the live site is touched.

**Shortcut for Elementor pages** (Home, Intake, Contact):
1. Local: open the page in Elementor → arrow next to **Update** → **Save as Template** → name it.
2. Local: **Templates → Saved Templates →** hover → **Export Template** to get a `.json` file.
3. Live: **Templates → Saved Templates → Import Templates →** upload the `.json`.
4. Live: open the page in Elementor → folder icon (**Add Template**) → **My Templates → Insert**. Delete the old sections, preview, then **Update**.
5. Check the images. Templates point to images by address, so re-select any image that shows as missing from the live Media Library.

**Don't** import the whole local copy back onto the live site with All-in-One WP Migration. That would overwrite everything on live, including form submissions received since the export.

## Everyday commands

Run these in `C:\Working\WebPage\docker`:

| Task | Command |
|---|---|
| Stop (keeps everything) | `docker compose stop` |
| Start again | `docker compose start` |
| **Wipe and start over** (deletes the local copy) | `docker compose down -v` then `.\setup.ps1` |
| See what's running | `docker compose ps` |
