import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import styles from './index.module.css';

const products = [
  { name: 'VPNdukevilla', logo: '/img/dukevilla-docs-card.png', logoClass: 'vpn', text: 'Secure control plane for IPsec and VPN operations.', href: '/docs/vpndukevilla', status: 'User manual' },
  { name: 'traDUKtor', logo: '/img/traduktor-logo.png', logoClass: 'traduktor', text: 'Protocol translation and DVRCP remote management of compatible access equipment.', href: '/docs/traduktor', status: 'Live operational manual' },
  { name: 'Fácil IoT', logo: '/img/facil-iot-logo.png', logoClass: 'faciliot', text: 'LoRaWAN/BLE operations, DVRCP device management and optional WiFi captive portals.', href: '/docs/facil-iot', status: 'Live operational manual' }
];

export default function Home() {
  return (
    <Layout title="Official documentation" description="DukeVilla product manuals and technical documentation">
      <main>
        <section className={styles.hero}>
          <div className="container">
            <div className={styles.heroGrid}>
              <div className={styles.heroCopy}>
                <span className={styles.eyebrow}>DUKEVILLA · DOCUMENTATION</span>
                <h1>Engineering knowledge,<br />ready for the field.</h1>
                <p>Official manuals, operating procedures, release information, and troubleshooting guidance for DukeVilla products.</p>
                <Link className="button button--primary button--lg" to="/docs/">Explore documentation</Link>
              </div>
              <div className={styles.corporateMark}>
                <img src="/img/dukevilla-corporate-dark.png" alt="DukeVilla — Data Transmission & Signal Processing" />
                <span>Official knowledge center</span>
              </div>
            </div>
          </div>
        </section>
        <section className={styles.products}>
          <div className="container">
            <div className={styles.grid}>
              {products.map((product) => (
                <Link className={styles.card} to={product.href} key={product.name}>
                  <div className={styles.cardTop}>
                    <span>{product.status}</span>
                    <div className={`${styles.logoFrame} ${styles[product.logoClass]}`}>
                      <img src={product.logo} alt={`${product.name} logo`} />
                    </div>
                  </div>
                  <h2>{product.name}</h2>
                  <p>{product.text}</p>
                  <strong>Open documentation →</strong>
                </Link>
              ))}
            </div>
            <p className="margin-top--lg">Manuales en español: <Link to="/docs/es/traduktor">traDUKtor</Link> · <Link to="/docs/es/facil-iot">Fácil IoT</Link>.</p>
          </div>
        </section>
      </main>
    </Layout>
  );
}
