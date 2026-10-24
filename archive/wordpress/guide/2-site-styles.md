# 2. Site-wide styles: logo, colours, fonts, buttons

## 2a. Logo and browser icon (Zakra)

**Appearance → Customize → Header → Header Main Area → Site Identity** (in some Zakra versions it's **Site Identity** directly in the Customize menu)
1. **Logo** → *Change logo* → choose `pft-logo.png`. Skip cropping.
2. Set the logo width/height so it reads clearly. About **200–240 px wide** on desktop is a good start.
3. Untick **Display Site Title and Tagline**, since the logo already says the name. Keep the title text filled in anyway, because it's used in browser tabs.
4. **Site Icon** → `pft-site-icon.png`.
5. **Tagline:** change "Helping Veterans In Need" to **Service Dogs for Veterans with PTSD** to match the banner and brochure.
6. **Publish.**

## 2b. Elementor global colours and fonts

Open any Elementor page → **☰ (top-left) → Site Settings**.

**Global Colors.** The site still uses Elementor's default teal (#5BDED5). Change to:

| Slot | New value | What it affects |
|---|---|---|
| Primary | `#C50000` | Headings and accents by default |
| Secondary | `#ADA49B` | Taupe (from the banner) |
| Text | `#2B2B2B` | Body text |
| Accent | `#C50000` | Buttons by default |

Then **+ Add Color** for: *Dark red* `#8B0000`, *Cream* `#F6F3EE`, *Ink* `#1E1E1E`.

> Many existing widgets set their colour directly (e.g. headings set to #000000), so they won't change. That's fine, since black headings on white look good. Only the teal showed through in a few places.

**Global Fonts.** Keep **Poppins** (bold, close to the logo lettering) for Primary and Secondary. Optionally switch **Text** from Merriweather to **Open Sans** 400, which is easier to read on phones. Your call; Merriweather is acceptable.

**Buttons** (Site Settings → Buttons): Text colour **#FFFFFF**, background **#C50000**, hover background **#8B0000**.

Click **Update**.

## 2c. Fix the button text colour on existing buttons

The home page buttons override the global settings with near-black text. The CSS in 2d fixes them all at once, so no per-button work is needed. If you'd rather fix them in Elementor: each Button widget → **Style → Text Color → #FFFFFF**, and on the **Hover** tab set Background **#8B0000**.

## 2d. Additional CSS

**Appearance → Customize → Additional CSS** → paste the whole of [`theme/additional-css.css`](../theme/additional-css.css) → **Publish**.

It fixes button contrast, adds visible keyboard focus outlines, and defines a few optional classes (`pft-band-cream`, `pft-stat`, `pft-team`, `pft-menu-donate`) that the next guides use.

## 2e. Turn off copy protection (recommended)

**Plugins → WP Content Copy Protector → Deactivate.**

Why:
- Visitors **can't select or copy your email address**. That's a real barrier for the people you're trying to reach.
- It's what writes the hidden "error:" text at the bottom of every page, which screen readers can still announce.
- It doesn't actually protect photos. Anyone can screenshot.

If you want to keep it, open its settings and at least allow text selection.

## Check

Open the home page in a private/incognito window. You should see the logo, white text on red buttons, and darker red on hover.
