# Publishing model

GitHub is the source of truth for WikiDukeVilla. Production files must never be edited directly on the VPS.

1. Product documentation is reviewed in its product repository.
2. An approved Markdown release is synchronized into WikiDukeVilla.
3. The WikiDukeVilla workflow builds a versioned static container image.
4. The VPS pulls the approved image and recreates only the wiki container.
5. Nginx publishes the container through `https://wiki.duke-villa.com`.

Credentials, PSKs, private keys, customer-specific secrets, and unredacted diagnostic reports must not be committed to this repository.
