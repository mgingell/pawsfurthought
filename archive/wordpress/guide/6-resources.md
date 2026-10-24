# 6. Resources page

The Resources page uses the normal WordPress editor, not Elementor.
**Pages → Resources & References → Edit.**

1. Click the **⋮** (top-right) → **Code editor**.
2. Select all, delete, and paste the block below.
3. Click **⋮ → Visual editor** to check it, then **Update**.

Changes from the current page:
- Leads with crisis lines.
- Fixes "OSI's".
- Removes the fragile `#:~:text=` link ending.
- Adds peer support (OSISS).
- Sorts the content into headings.

```html
<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">OSI and PTSD Resources</h1>
<!-- /wp:heading -->

<!-- wp:group {"style":{"spacing":{"padding":{"top":"20px","right":"20px","bottom":"20px","left":"20px"}},"border":{"left":{"color":"#C50000","width":"5px"}}},"backgroundColor":"white"} -->
<div class="wp-block-group has-white-background-color has-background" style="border-left-color:#C50000;border-left-width:5px;padding-top:20px;padding-right:20px;padding-bottom:20px;padding-left:20px"><!-- wp:paragraph -->
<p><strong>Need help now?</strong> Call or text <strong>9-8-8</strong>, the Suicide Crisis Helpline, any time, 24/7. Veterans, former RCMP members and their families can also call the <strong>VAC Assistance Service at 1-800-268-7708</strong>, free and confidential, 24/7. In an emergency, call 9-1-1.</p>
<!-- /wp:paragraph --></div>
<!-- /wp:group -->

<!-- wp:heading -->
<h2 class="wp-block-heading">What is an Operational Stress Injury (OSI)?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Veterans Affairs Canada defines an Operational Stress Injury (OSI) as "any persistent psychological difficulty resulting from operational duties performed while serving with the Canadian Forces or as a member of the RCMP." These difficulties can include post-traumatic stress disorder (PTSD), depression, anxiety, and addictions. An OSI can result from exposure to a traumatic incident, cumulative exposure to human atrocities, or simply sustained exposure to intense military operations. (<a href="https://www.veterans.gc.ca/eng/health-support/mental-health-and-wellness/understanding-mental-health" target="_blank" rel="noopener">VAC: Understanding mental health</a>)</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">How is an OSI different from PTSD?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>An OSI can have symptoms similar to PTSD, but it may be caused by a series of smaller traumas or stressful events over a long period of time. People with an OSI may have diagnoses other than PTSD, including acute stress disorder, adjustment disorder, or an anxiety or depressive disorder. (<a href="https://www.addictionresource.ca/concurrent-disorders/trauma-ptsd-and-osi/" target="_blank" rel="noopener">Addiction Resource: Trauma, PTSD and OSI</a>)</p>
<!-- /wp:paragraph -->

<!-- wp:heading -->
<h2 class="wp-block-heading">More support</h2>
<!-- /wp:heading -->

<!-- wp:list -->
<ul class="wp-block-list"><!-- wp:list-item -->
<li><a href="https://www.veterans.gc.ca/en/contact" target="_blank" rel="noopener">Veterans Affairs Canada: contact and support lines</a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="https://www.canada.ca/en/department-national-defence/programs/osiss.html" target="_blank" rel="noopener">Operational Stress Injury Social Support (OSISS)</a>: peer support for CAF members, veterans and their families</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="https://www.veterans.gc.ca/eng/health-support/physical-health-and-wellness/compensation-illness-injury/disability-benefits/benefits-determined/entitlement-eligibility-guidelines/ptsd" target="_blank" rel="noopener">VAC: PTSD entitlement eligibility guidelines</a></li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="https://woundedwarriors.ca/" target="_blank" rel="noopener">Wounded Warriors Canada</a>: mental health programs for veterans, first responders and their families</li>
<!-- /wp:list-item -->

<!-- wp:list-item -->
<li><a href="https://novascotia.ca/servicedogs/" target="_blank" rel="noopener">Nova Scotia Service Dog Act</a></li>
<!-- /wp:list-item --></ul>
<!-- /wp:list -->

<!-- wp:paragraph -->
<p>Interested in a service dog? Visit our <a href="/application-process/in-take/">Intake page</a> or read the <a href="/faq/">FAQ</a>.</p>
<!-- /wp:paragraph -->
```

Then add this page to the menu (guide 10).
