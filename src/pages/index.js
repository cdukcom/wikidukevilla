import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import styles from './index.module.css';

const products = [
  { name: 'VPNdukevilla', logo: '/img/dukevilla-docs-card.png', logoClass: 'vpn', text: 'Secure control plane for IPsec and VPN operations.', href: '/docs/vpndukevilla', status: 'Manual 1.0.4' },
  { name: 'traDUKtor', logo: '/img/traduktor-logo.png', logoClass: 'traduktor', text: 'Translation and integration tools engineered for operations.', href: '/docs/traduktor', status: 'Coming soon' },
  { name: 'Facil IoT', logo: '/img/facil-iot-logo.png', logoClass: 'faciliot', text: 'Practical device management and IoT operations.', href: '/docs/facil-iot', status: 'Coming soon' }
];

export default function Home() {
  return (
    <Layout title="Official documentation" description="DukeVilla product manuals and technical documentation">
      <main>
        <section className={styles.hero}>
          <div className="container">
            <span className={styles.eyebrow}>DUKEVILLA · DOCUMENTATION</span>
            <h1>Engineering knowledge,<br />ready for the field.</h1>
            <p>Official manuals, operating procedures, release information, and troubleshooting guidance for DukeVilla products.</p>
            <Link className="button button--primary button--lg" to="/docs/">Explore documentation</Link>
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
          </div>
        </section>
      </main>
    </Layout>
  );
}
