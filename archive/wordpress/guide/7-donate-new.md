# 7. New page: Donate

Today the Donate buttons send people straight to Wounded Warriors Canada with only "leave a comment" as guidance. This page explains the steps first.

**Pages → Add New.**
- Title: `Donate`
- Check the URL is **/donate/** (Page sidebar → *Link* / *URL*).
- Use the normal editor (no Elementor needed): **⋮ → Code editor**, paste the block below, then **Publish**.

```html
<!-- wp:paragraph {"fontSize":"large"} -->
<p class="has-large-font-size">Paws Fur Thought is a not-for-profit supported by <strong>Wounded Warriors Canada (WWC)</strong>. Donations are made through WWC, a registered Canadian charity.</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">How to donate</h2>
<!-- /wp:heading -->

<!-- wp:list {"ordered":true} -->
<ol class="wp-block-list"><!-- wp:list-item -->
<li>Go to the <a href="https://woundedwarriors.ca/donate/" target="_blank" rel="noopener">Wounded Warriors Canada donation page</a>.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Choose the <strong>PTSD Service Dogs</strong> program as the designation for your gift.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>To support Paws Fur Thought specifically, write <strong>"For Paws Fur Thought"</strong> in the comment or message box.</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li>Complete your donation.</li>
<!-- /wp:list-item --></ol>
<!-- /wp:list -->

<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button {"backgroundColor":"vivid-red","textColor":"white"} -->
<div class="wp-block-button"><a class="wp-block-button__link has-white-color has-vivid-red-background-color has-text-color has-background wp-element-button" href="https://woundedwarriors.ca/donate/" target="_blank" rel="noopener">Donate through Wounded Warriors Canada</a></div>
<!-- /wp:button --></div>
<!-- /wp:buttons -->

<!-- wp:heading -->
<h2 class="wp-block-heading">Where your donation goes</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Donations help Paws Fur Thought pair Canadian veterans and serving members with fully trained, certified service dogs. We cover the cost of the dog, flights, and accommodation for the mandatory 5-day training in Concordia, Kansas. Since 2013, we've paired over 100 service dogs with veterans in Atlantic Canada.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Questions about giving, or interested in fundraising for us? <a href="/contact/">Contact us</a>.</p>
<!-- /wp:paragraph -->
```

> **[CONFIRM]** Go through WWC's donation form once yourself and check that "PTSD Service Dogs" and a comment box still exist under those names. WWC updates their form from time to time. Adjust steps 2–3 to match what you see. Also confirm how WWC handles tax receipts, and add a line about it if useful.

After publishing, update all Donate buttons to link to `/donate/` (home hero, home photo band, and the menu in guide 10).
