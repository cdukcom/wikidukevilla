const config = {
  title: 'DukeVilla Documentation',
  tagline: 'Official product manuals and technical documentation',
  favicon: 'img/favicon.ico',
  url: 'https://wiki.duke-villa.com',
  baseUrl: '/',
  organizationName: 'cdukcom',
  projectName: 'wikidukevilla',
  onBrokenLinks: 'throw',
  i18n: { defaultLocale: 'en', locales: ['en'] },
  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: 'docs',
          sidebarPath: require.resolve('./sidebars.js'),
          showLastUpdateAuthor: true,
          showLastUpdateTime: true
        },
        blog: false,
        theme: { customCss: require.resolve('./src/css/custom.css') }
      }
    ]
  ],
  themeConfig: {
    image: 'img/dukevilla-docs-card.png',
    colorMode: { defaultMode: 'light', respectPrefersColorScheme: true },
    navbar: {
      title: 'DukeVilla Docs',
      logo: { alt: 'DukeVilla', src: 'img/dukevilla-icon.png' },
      items: [
        { to: '/docs/vpndukevilla', label: 'VPNdukevilla', position: 'left' },
        { to: '/docs/traduktor', label: 'traDUKtor', position: 'left' },
        { to: '/docs/facil-iot', label: 'Facil IoT', position: 'left' },
        { href: 'https://duke-villa.com', label: 'DukeVilla', position: 'right' }
      ]
    },
    footer: {
      style: 'dark',
      links: [
        { title: 'Products', items: [
          { label: 'VPNdukevilla', to: '/docs/vpndukevilla' },
          { label: 'traDUKtor', to: '/docs/traduktor' },
          { label: 'Facil IoT', to: '/docs/facil-iot' }
        ]},
        { title: 'Company', items: [
          { label: 'duke-villa.com', href: 'https://duke-villa.com' }
        ]}
      ],
      copyright: `Copyright © ${new Date().getFullYear()} DukeVilla. Official product documentation.`
    }
  }
};

module.exports = config;
