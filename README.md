# WikiDukeVilla

Official source for `wiki.duke-villa.com`.

## Local development

```bash
npm ci
npm start
```

## Production build

```bash
npm run build
docker build -t dukevilla-wiki:local .
```

GitHub is the source of truth. Production content must never be edited directly on the VPS.
