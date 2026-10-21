# WikiDukeVilla Documentation Guide

Read this file before creating, importing, or updating any documentation in
this repository.

## Purpose

WikiDukeVilla is the public, official documentation portal for DukeVilla and
its products. The homepage represents DukeVilla as the parent brand; product
identity belongs inside each product card and manual.

Public URL: `https://wiki.duke-villa.com`

## Language and audience

- Write all DukeVilla product documentation in clear technical English.
- Write for operators, installers, administrators, and support technicians.
- Prefer short procedures, explicit field descriptions, safety notes, and
  verifiable outcomes.
- Do not publish customer-specific delivery reports in this public portal.
- Do not expose internal deployment procedures, infrastructure details,
  credentials, PSKs, private keys, tokens, customer data, or unsanitized logs.

## Source of truth

- The approved manual in the corresponding product repository is the primary
  source of truth.
- WikiDukeVilla contains the public web edition and its downloadable PDF.
- Never edit production files directly on the VPS.
- Keep internal publishing notes under `internal/`, outside the Docusaurus
  documentation tree.

## Repository structure

- `docs/`: public Markdown documentation rendered by Docusaurus.
- `static/img/`: logos and images used by pages and manuals.
- `static/downloads/`: versioned downloadable manuals and related public files.
- `sidebars.js`: public documentation navigation.
- `src/pages/index.js`: homepage and product cards.
- `docusaurus.config.js`: site metadata, navigation, footer, and branding.
- `internal/`: non-public maintainer documentation.

Use lowercase, stable, descriptive paths. Group new product assets when the
number of files grows, for example:

```text
docs/facil-iot/
static/img/facil-iot/
static/downloads/facil-iot/
```

## Adding a new manual

1. Confirm the product name, manual title, public version, and approved source.
2. Convert or adapt the approved content to Markdown without changing its
   technical meaning.
3. Add Docusaurus front matter with a stable slug, title, and sidebar order.
4. Place screenshots and diagrams in `static/img/<product>/` and use meaningful
   English alternative text.
5. Place the approved PDF in `static/downloads/<product>/` with a versioned
   filename. Never silently replace a PDF belonging to an older release.
6. Add an obvious PDF download link near the beginning of the web manual.
7. Add the manual to `sidebars.js` and update the product card on the homepage.
8. Verify links, images, headings, tables, warnings, mobile layout, and PDF
   download behavior.

## Updating an existing manual

1. Compare the approved source against the current Markdown edition.
2. Preserve stable URLs unless a redirect is intentionally added.
3. Update only content supported by the new product release.
4. Update every visible version reference consistently: page title, manual
   metadata, homepage card, documentation center, PDF filename, and links.
5. Retain older release artifacts when required for traceability; do not label
   an unverified draft as the current manual.
6. Rebuild and inspect the affected pages before publication.

## Writing conventions

- Use sentence case for headings and interface labels exactly as displayed.
- Introduce a feature before listing its fields.
- For each configurable field, explain purpose, accepted value, default or
  expected behavior, and operational consequence when relevant.
- Number procedures that must be followed in order.
- Use bullets for options and independent facts.
- Use notes and warnings sparingly and only when they help prevent mistakes,
  service interruption, data loss, or insecure configuration.
- Describe observable results so the reader can confirm that a step worked.
- Use IPsec capitalization. Preserve official product capitalization:
  DukeVilla, VPNdukevilla, traDUKtor, and Fácil IoT.

## Brand rules

- The portal is corporate DukeVilla documentation, not a VPNdukevilla site.
- Use the DukeVilla corporate logo and favicon for the portal shell.
- Use each product logo only for its card, section, and manual.
- Preserve the established black, warm white, and gold visual system.
- Optimize large raster images before adding them when quality is not affected.

## Required validation

Run from the repository root:

```bash
npm ci
npm run build
git diff --check
```

Before considering a documentation change complete:

- Open the affected public pages in a browser.
- Check desktop and narrow/mobile layouts.
- Confirm that navigation contains only public documentation.
- Confirm that every new image and download returns successfully.
- Confirm that no secret or customer-specific data is present.

## Release and publication workflow

1. Commit the reviewed source changes with a concise English commit message.
2. Push to the `main` branch of `cdukcom/wikidukevilla`.
3. Confirm that the GitHub Actions image build completes successfully.
4. On the VPS, pull the new image and recreate only the WikiDukeVilla
   container from `/opt/wikidukevilla`.
5. Confirm container health and verify `https://wiki.duke-villa.com`.

Do not claim publication based only on a successful local build or Git push.
The public site must be checked after deployment.

## Completion record

When handing off a manual update, report:

- Product and manual version.
- Markdown and PDF paths.
- Pages or sections changed.
- Build and browser verification performed.
- Git commit identifier.
- Public URL verified after deployment.

