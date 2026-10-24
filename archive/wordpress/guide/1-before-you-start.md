# 1. Before you start

## 1a. Back up the site (do not skip)

1. Log in at **godaddy.com → My Products → Managed WordPress → pawsfurthought.ca → Settings**.
2. Open **Backups** and click **Create backup** (the wording may be *Back up now*).
3. Wait for it to finish before changing anything. If something goes wrong later, **Restore** this backup.

Also in Elementor: each Elementor page has its own **History → Revisions** panel (clock icon, bottom-left of the editor). You can roll back a single page without restoring the whole site.

## 1b. Upload the new images

**Media → Add New**, then drag in everything from the `assets/` folder:

| File | Used for | Alt text to enter (Media → click image → *Alternative Text*) |
|---|---|---|
| `pft-logo.png` | Header logo (from `Marketing\Ready\paws_logo.svg`, the maple-leaf paw) | Paws Fur Thought |
| `pft-site-icon.png` | Browser tab icon | *(leave blank — decorative)* |
| `pft-patch-red.png` | Home page emblem | Paws Fur Thought patch: "Paws-itive Outcomes" with a maple leaf in a paw print |
| `hero-service-dog-ceremony.jpg` | Home page top banner | A black Labrador service dog in a Legion vest lies calmly at a veterans' ceremony |
| `hero-alt-dogs-illustrated.jpg` | *Alternative* banner (optional) | Illustration of several service dogs in vests resting together |
| `team-1.jpg` | Home "Our teams" | A veteran in a red shirt sits with a black Labrador service dog |
| `team-2.jpg` | Home "Our teams" | A veteran in a green shirt hugs a golden retriever service dog |
| `team-3.jpg` | Home "Our teams" | A veteran in a tan cap sits with a yellow Labrador service dog |
| `cares-logo.png` | Home "Partners" | CARES Inc. |
| `wwc-service-dog.png` | Home "Partners" | Wounded Warriors Canada Supported Service Dog |

> **[CONFIRM]** Get the veterans' OK before putting team-1..3 on the site. If they agree and want first names shown, add them to the alt text, e.g. "Andre with service dog Rone".

Notes:
- The current home page banner (a person and a black dog in front of a silver Jeep) is a friendly photo, but it doesn't say "veterans + service dogs" at a glance. The ceremony photo does. Your call.
- `wwc-service-dog.png` is the WWC "Supported Service Dog" badge (from `Marketing\WWC SERVICE DOG.svg`), saved as a PNG because WordPress blocks SVG uploads by default. `wwc-service-dog.svg` is also in `assets/` for the mock-up; you don't need to upload it.
